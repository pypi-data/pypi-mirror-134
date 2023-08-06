import json
import os
from functools import partial
import shutil
import tarfile
import logging as _logging

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMainWindow)
from PyQt5.QtGui import QMovie

from simsapa.app.types import AppMessage

from ..app.helpers import download_file

from simsapa import ASSETS_DIR, APP_DB_PATH, STARTUP_MESSAGE_PATH
from simsapa.assets import icons_rc  # noqa: F401

logger = _logging.getLogger(__name__)


class DownloadAppdataWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Download Application Assets")
        self.setFixedSize(300, 300)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self._layout = QVBoxLayout()
        self._central_widget.setLayout(self._layout)

        self._msg = QLabel("The application database\nwas not found on this system.\n\nDownload it now?")
        self._msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._msg)

        self._animation = QLabel(self)
        self._animation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._layout.addWidget(self._animation)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 20, 0, 10)

        self._download_button = QPushButton("Download")
        self._download_button.setFixedSize(100, 30)
        self._quit_button = QPushButton("Quit")
        self._quit_button.setFixedSize(100, 30)

        self._download_button.clicked.connect(partial(self._run_download))
        self._quit_button.clicked.connect(partial(self.close))

        buttons_layout.addWidget(self._quit_button)
        buttons_layout.addWidget(self._download_button)

        self._layout.addLayout(buttons_layout)

    def startAnimation(self):
        self._movie.start()

    def stopAnimation(self):
        self._movie.stop()

    def _run_download(self):
        self.thread: QThread = QThread()
        self.worker = DownloadWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        self._msg.setText("Downloading ...")
        self._download_button.setEnabled(False)

        self._movie = QMovie(':simsapa-loading')
        self._animation.setMovie(self._movie)

        self.startAnimation()

        self.thread.finished.connect(self._download_finished)

    def _download_finished(self):
        self.stopAnimation()
        self._animation.deleteLater()

        self._msg.setText("Download completed.\n\nQuit and start the application again.")


class DownloadWorker(QObject):
    finished = pyqtSignal()

    def run(self):
        download_extract_appdata()
        self.finished.emit()


def download_extract_appdata() -> bool:
    tar_file_path = download_file(
        'https://ssp.a-buddha-ujja.hu/assets/assets.tar.bz2',
        ASSETS_DIR
    )

    tar = tarfile.open(tar_file_path, "r:bz2")
    temp_dir = ASSETS_DIR.joinpath('extract_temp')
    tar.extractall(temp_dir)
    tar.close()

    os.remove(tar_file_path)

    shutil.move(temp_dir.joinpath("appdata.sqlite3"), ASSETS_DIR)

    # only move the extracted index if there isn't yet an index (first run)
    if not ASSETS_DIR.joinpath("index").exists():
        shutil.move(temp_dir.joinpath("index"), ASSETS_DIR)
    else:
        # on the next run, notify the user to re-index
        msg = AppMessage(
            kind = "warning",
            text = "<p>The sutta and dictionary database was updated. Re-indexing is necessary for the contents to be searchable.</p><p>You can start a re-index operation with <b>File > Re-index database</b>.</p>",
        )
        with open(STARTUP_MESSAGE_PATH, 'w') as f:
            f.write(json.dumps(msg))

    shutil.rmtree(temp_dir)

    if not APP_DB_PATH.exists():
        logger.error(f"File not found: {APP_DB_PATH}")
        return False
    else:
        return True
