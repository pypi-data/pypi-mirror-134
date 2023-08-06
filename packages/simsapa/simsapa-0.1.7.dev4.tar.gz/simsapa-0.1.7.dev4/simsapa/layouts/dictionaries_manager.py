import os
import shutil
import json
import semver
import logging as _logging
from functools import partial
from typing import List, Optional
from pathlib import Path
from zipfile import ZipFile
import pandas
from pyglossary import Glossary
from sqlalchemy.sql import func

from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QLabel, QMainWindow,
                             QMessageBox, QInputDialog, QFileDialog, QLineEdit)

from simsapa import ASSETS_DIR
from simsapa.assets import icons_rc  # noqa: F401

from ..app.db_models import DictionarySource
from ..app.types import AppData, DictWord
from ..app.helpers import download_file
from ..assets.ui.dictionaries_manager_window_ui import Ui_DictionariesManagerWindow

logger = _logging.getLogger(__name__)
Glossary.init()


class DictionarySourceListModel(QAbstractListModel):
    def __init__(self, *args, dictionaries=None, **kwargs):
        super(DictionarySourceListModel, self).__init__(*args, **kwargs)
        self.dictionaries = dictionaries or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.dictionaries[index.row()].title

        if role == Qt.DecorationRole:
            if self.dictionaries[index.row()].has_update:
                return QIcon(":sync")

    def rowCount(self, index):
        return len(self.dictionaries)


class DictionariesManagerWindow(QMainWindow, Ui_DictionariesManagerWindow):
    def __init__(self, app_data: AppData, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._app_data: AppData = app_data

        self.model = DictionarySourceListModel(dictionaries=self._get_all_dictionary_sources())

        self.dictionary_sources_list.setModel(self.model)
        self.sel_model = self.dictionary_sources_list.selectionModel()

        self._ui_setup()
        self._connect_signals()

        self.statusbar.showMessage("Ready", 3000)

    def _ui_setup(self):
        self.status_msg = QLabel("")
        self.statusbar.addPermanentWidget(self.status_msg)

        self._show_dictionary_source_clear()

    def _get_all_dictionary_sources(self) -> List[DictionarySource]:
        return self._app_data.user_db_session.query(DictionarySource).all()

    def get_selected_dictionary_source(self) -> Optional[DictionarySource]:
        a = self.dictionary_sources_list.selectedIndexes()
        if not a:
            return None

        item = a[0]
        return self.model.dictionaries[item.row()]

    def remove_selected_dictionary_source(self):
        a = self.dictionary_sources_list.selectedIndexes()
        if not a:
            return None

        # Remove from model
        item = a[0]
        dict_id = self.model.dictionaries[item.row()].id

        del self.model.dictionaries[item.row()]
        self.model.layoutChanged.emit()
        self.dictionary_sources_list.clearSelection()
        self._show_dictionary_source_clear()

        # Remove from database

        db_item = self._app_data.user_db_session \
                                .query(DictionarySource) \
                                .filter(DictionarySource.id == dict_id) \
                                .first()
        self._app_data.user_db_session.delete(db_item)
        self._app_data.user_db_session.commit()

    def _handle_dictionary_source_select(self):
        doc = self.get_selected_dictionary_source()
        if doc:
            self._show_dictionary_source(doc)
        else:
            self._show_dictionary_source_clear()

    def _show_dictionary_source_clear(self):
        self.status_msg.clear()
        self.dict_creator.clear()
        self.dict_cover.clear()
        self.dict_message.clear()
        self.dict_title.clear()
        self.dict_version.clear()
        self.dict_description.clear()
        self.dict_update_button.hide()

    def _show_dictionary_source(self, dict_source: DictionarySource):
        self.status_msg.setText(dict_source.title)
        self.dict_creator.setText(dict_source.creator)
        self.dict_title.setText(dict_source.title)
        self.dict_version.setText(dict_source.version)
        self.dict_description.setText(dict_source.description)

        if dict_source.has_update:
            self.dict_message.setText("An updated version is available.")
            font = QFont()
            font.setItalic(True)
            self.dict_message.setFont(font)
            self.dict_update_button.show()
        else:
            self.dict_message.clear()
            self.dict_update_button.hide()

    def add_words_from_xlsx(self, xlsx_path: Path):
        xlsx_data_df = pandas.read_excel(xlsx_path, sheet_name='Words')
        words_data = xlsx_data_df.to_dict(orient='records')

        def to_word(data) -> DictWord:
            word = DictWord(data['word'])
            word.definition_md = data['definition_md']
            return word

        words: List[DictWord] = list(map(to_word, words_data))

        print(len(words))

    def add_words_from_stardict(self, ifo_path: Path):
        logger.info(f'add_words_from_stardict(): {ifo_path}')
        glos = Glossary()
        if not glos.read(ifo_path, format='Stardict', direct=True, progressbar=False):
            logger.error('Reading StarDict failed')

        words: List[DictWord] = []

        n = 0
        max_words = 100  # FIXME don't stop importing

        # TODO create dictionary for manager from Startdict info

        for entry in glos:
            if n >= max_words:
                break
            n += 1

            # handle entry.defiFormat
            # m is plaintext
            # h is html

            logger.info(entry.s_word)
            word = DictWord(entry.s_word)
            word.definition_md = entry.defi
            words.append(word)

        print(len(words))

    def process_file(self, p: Path):
        # MS Excel Spreadsheet
        if p.suffix == '.xlsx':
            self.add_words_from_xlsx(p)

        # Stardict format
        if p.suffix == '.ifo':
            self.add_words_from_stardict(p)

    def add_words_from_data_zip(self, zip_path: Path, extract_dir: Path):
        try:
            with ZipFile(zip_path, 'r') as z:
                z.extractall(extract_dir)
        except Exception as e:
            logger.error(e)
            return

        for p in extract_dir.glob("*"):
            if p.is_dir():
                for pp in p.glob("*"):
                    self.process_file(pp)
            else:
                self.process_file(p)

    def add_from_file(self, zip_path: Path):
        temp_dir: Path = ASSETS_DIR.joinpath('temp')
        if not temp_dir.exists():
            os.mkdir(temp_dir)

        self.add_words_from_data_zip(zip_path, temp_dir)

        shutil.rmtree(temp_dir)

        # TODO add dictionary entry to manager

    def add_from_url(self, json_url):
        temp_dir: Path = ASSETS_DIR.joinpath('temp')
        if not temp_dir.exists():
            os.mkdir(temp_dir)

        json_path = download_file(json_url, temp_dir)
        with open(json_path, 'r') as f:
            remote_info = json.loads(f.read())

        zip_path = download_file(remote_info['data_zip_url'], temp_dir)

        self.add_words_from_data_zip(zip_path, temp_dir)

        # Remove downloaded files
        shutil.rmtree(temp_dir)

        # Add DictionarySource

        item = self._app_data.user_db_session \
                             .query(DictionarySource) \
                             .filter(DictionarySource.info_json_url == json_url) \
                             .first()

        if item is None:
            logger.info(f"Add new: {remote_info['title']}")
            db_source = DictionarySource(
                title=remote_info['title'],
                creator=remote_info['creator'],
                description=remote_info['description'],
                contact_email=remote_info['contact_email'],
                version=remote_info['version'],
                has_update=False,
                info_json_url=json_url,
                data_zip_url=remote_info['data_zip_url'],
                created_at=func.now(),
            )
            try:
                self._app_data.user_db_session.add(db_source)
                self._app_data.user_db_session.commit()

                # Add to model
                self.model.dictionaries.append(db_source)

            except Exception as e:
                logger.error(e)

        else:
            logger.info(f"Update: {item.title}")

            values = {
                'title': remote_info['title'],
                'creator': remote_info['creator'],
                'description': remote_info['description'],
                'contact_email': remote_info['contact_email'],
                'version': remote_info['version'],
                'has_update': False,
                'info_json_url': json_url,
                'data_zip_url': remote_info['data_zip_url'],
                'updated_at': func.now()
            }
            try:
                self._app_data.user_db_session \
                              .query(DictionarySource) \
                              .filter(DictionarySource.id == item.id) \
                              .update(values)

                self._app_data.user_db_session.commit()

            except Exception as e:
                logger.error(e)

        self._handle_dictionary_source_select()
        self.model.layoutChanged.emit()

    def _add_from_url_dialog(self):
        url, ok = QInputDialog.getText(self,
                                       "Add from URL...",
                                       "URL of JSON info of the dictionary:",
                                       QLineEdit.Normal,
                                       "")
        if ok:
            self.add_from_url(url)

    def _add_from_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open File...",
            "",
            "Zip Files (*.zip)")

        if len(file_path) != 0:
            self.add_from_file(file_path)

    def _remove_dictionary_source_dialog(self):
        dict_source = self.get_selected_dictionary_source()
        if not dict_source:
            return

        reply = QMessageBox.question(self,
                                     'Remove Dictionary Source...',
                                     'Remove this Dictionary source?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.remove_selected_dictionary_source()

    def _check_updates(self):
        temp_dir: Path = ASSETS_DIR.joinpath('temp')
        if not temp_dir.exists():
            os.mkdir(temp_dir)

        for d in self.model.dictionaries:
            json_path = download_file(d.info_json_url, temp_dir)
            with open(json_path, 'r') as f:
                remote_info = json.loads(f.read())
                if semver.compare(remote_info['version'], d.version) == 1:

                    d.has_update = True
                    self._app_data.user_db_session.commit()

        self.model.layoutChanged.emit()

    def _update_selected_dictionary_source(self):
        dict_source = self.get_selected_dictionary_source()
        if dict_source:
            self.add_from_url(dict_source.info_json_url)

    def _connect_signals(self):
        self.action_Close_Window \
            .triggered.connect(partial(self.close))

        self.action_Add_from_URL \
            .triggered.connect(partial(self._add_from_url_dialog))

        self.action_Import_from_File \
            .triggered.connect(partial(self._add_from_file_dialog))

        self.action_Check_Updates \
            .triggered.connect(partial(self._check_updates))

        self.action_Remove \
            .triggered.connect(partial(self._remove_dictionary_source_dialog))

        self.sel_model.selectionChanged.connect(partial(self._handle_dictionary_source_select))

        self.dict_update_button.clicked.connect(partial(self._update_selected_dictionary_source))
