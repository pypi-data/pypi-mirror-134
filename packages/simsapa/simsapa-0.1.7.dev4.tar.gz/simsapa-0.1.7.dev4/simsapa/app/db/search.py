import logging as _logging
import shutil
from typing import Callable, List, Optional, TypedDict, Union
import re

from whoosh.highlight import SCORE, HtmlFormatter
from whoosh.index import FileIndex, create_in, open_dir
from whoosh.fields import SchemaClass, NUMERIC, TEXT, ID
from whoosh.qparser import QueryParser, FuzzyTermPlugin
from whoosh.searching import Results, Hit
from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh.support.charset import accent_map

from simsapa.app.helpers import compactPlainText, compactRichText
from simsapa.app.db import appdata_models as Am
from simsapa.app.db import userdata_models as Um
from simsapa import INDEX_DIR

logger = _logging.getLogger(__name__)

USutta = Union[Am.Sutta, Um.Sutta]
UDictWord = Union[Am.DictWord, Um.DictWord]

# Add an accent-folding filter to the stemming analyzer
folding_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)

class SuttasIndexSchema(SchemaClass):
    index_key = ID(stored = True, unique = True)
    db_id = NUMERIC(stored = True)
    schema_name = TEXT(stored = True)
    uid = ID(stored = True)
    title = TEXT(stored = True, analyzer = folding_analyzer)
    title_pali = TEXT(stored = True, analyzer = folding_analyzer)
    title_trans = TEXT(stored = True, analyzer = folding_analyzer)
    content = TEXT(stored = True, analyzer = folding_analyzer)
    ref = ID(stored = True)

class DictWordsIndexSchema(SchemaClass):
    index_key = ID(stored = True, unique = True)
    db_id = NUMERIC(stored = True)
    schema_name = TEXT(stored = True)
    uid = ID(stored = True)
    word = TEXT(stored = True, analyzer = folding_analyzer)
    synonyms = TEXT(stored = True, analyzer = folding_analyzer)
    content = TEXT(stored = True, analyzer = folding_analyzer)

# TODO same as simsapa.app.types.Labels, but declared here to avoid cirular import
class Labels(TypedDict):
    appdata: List[str]
    userdata: List[str]

class SearchResult(TypedDict):
    # database id
    db_id: int
    # database schema name (appdata or userdata)
    schema_name: str
    # database table name (e.g. suttas or dict_words)
    table_name: str
    uid: Optional[str]
    title: str
    ref: Optional[str]
    author: Optional[str]
    # highlighted snippet
    snippet: str
    # page number in a document
    page_number: Optional[int]

def sutta_hit_to_search_result(x: Hit, snippet: str) -> SearchResult:
    return SearchResult(
        db_id = x['db_id'],
        schema_name = x['schema_name'],
        table_name = 'suttas',
        uid = x['uid'],
        title = x['title'],
        ref = x['ref'],
        author = None,
        snippet = snippet,
        page_number = None,
    )

def dict_word_hit_to_search_result(x: Hit, snippet: str) -> SearchResult:
    return SearchResult(
        db_id = x['db_id'],
        schema_name = x['schema_name'],
        table_name = 'dict_words',
        uid = x['uid'],
        title = x['word'],
        ref = None,
        author = None,
        snippet = snippet,
        page_number = None,
    )

class SearchQuery:
    def __init__(self, ix: FileIndex, page_len: int, hit_to_result_fn: Callable):
        self.ix = ix
        self.searcher = ix.searcher()
        self.all_results: Results
        self.filtered: List[Hit]
        self.hits: int = 0
        self.page_len = page_len
        self.hit_to_result_fn = hit_to_result_fn

    def _compact_plain_snippet(self,
                               content: str,
                               title: Optional[str] = None,
                               ref: Optional[str] = None) -> str:

        s = content

        # AN 3.119 Kammantasutta
        # as added to the content when indexing
        if ref is not None and title is not None:
            s = s.replace(f"{ref} {title}", '')

        # 163–182. (- dash and -- en-dash)
        s = re.sub(r'[0-9\.–-]+', '', s)

        # ... Book of the Sixes 5.123.
        s = re.sub(r'Book of the [\w ]+[0-9\.]+', '', s)

        # Connected Discourses on ... 12.55.
        s = re.sub(r'\w+ Discourses on [\w ]+[0-9\.]+', '', s)

        # ...vagga
        s = re.sub(r'[\w -]+vagga', '', s)

        # ... Nikāya 123.
        s = re.sub(r'[\w]+ Nikāya +[0-9\.]*', '', s)

        # SC 1, (SuttaCentral ref link text)
        s = re.sub('SC [0-9]+', '', s)

        # Remove the title from the content, but only the first instance, so as
        # not to remove a common word (e.g.'kamma') from the entire text.
        if title is not None:
            s = s.replace(title, '', 1)

        return s

    def _oneline(self, content: str) -> str:
        s = content
        # Clean up whitespace so that all text is one line
        s = s.replace("\n", ' ')
        # replace multiple spaces to one
        s = re.sub(r'  +', ' ', s)

        return s

    def _plain_snippet_from_hit(self, x: Hit) -> str:
            s = x['content'][0:500]
            if 'title' in x.keys() and 'ref' in x.keys():
                s = self._compact_plain_snippet(s, x['title'], x['ref'])
            else:
                s = self._compact_plain_snippet(s)
            s = self._oneline(s).strip()
            snippet = s[0:250] + ' ...'

            return snippet

    def _result_with_snippet_highlight(self, x: Hit):
        style = "<style>span.match { background-color: yellow; }</style>"
        fragments = x.highlights(fieldname='content', top=5)

        if len(fragments) > 0:
            snippet = style + fragments
        else:
            snippet = self._plain_snippet_from_hit(x)

        return self.hit_to_result_fn(x, snippet)

    def _result_with_content_no_highlight(self, x: Hit):
        snippet = self._plain_snippet_from_hit(x)
        return self.hit_to_result_fn(x, snippet)

    def _search_field(self, field_name: str, query: str) -> Results:
        parser = QueryParser(field_name, self.ix.schema)
        parser.add_plugin(FuzzyTermPlugin())
        q = parser.parse(query)

        # NOTE: limit=None is fast enough (~1700 hits for 'dhamma'), doesn't
        # hang when doing incremental search while typing.
        #
        # The highlighting _is_ slow, that has to be only done on the
        # displayed results page.

        return self.searcher.search(q, limit=None)

    def highlight_results_page(self, page_num: int) -> List[SearchResult]:
        page_start = page_num * self.page_len
        page_end = page_start + self.page_len
        return list(map(self._result_with_snippet_highlight, self.filtered[page_start:page_end]))

    def new_query(self,
                  query: str,
                  disabled_labels: Optional[Labels] = None) -> List[SearchResult]:

        self.all_results = self._search_field(field_name = 'content', query = query)

        def _not_in_disabled(x: Hit):
            if disabled_labels is not None:
                for schema in disabled_labels.keys():
                    for label in disabled_labels[schema]:
                        if x['schema_name'] == schema and x['uid'].endswith(f'/{label.lower()}'):
                            return False
                return True
            else:
                return True


        if disabled_labels is None:
            self.filtered = list(self.all_results)
        else:
            self.filtered = list(filter(_not_in_disabled, self.all_results))

        # NOTE: r.estimated_min_length() errors on some searches
        self.hits = len(self.filtered)

        if self.hits == 0:
            return []

        # may slow down highlighting with many results
        # r.fragmenter.charlimit = None

        self.all_results.fragmenter.maxchars = 200
        self.all_results.fragmenter.surround = 20
        # FIRST (the default) Show fragments in the order they appear in the document.
        # SCORE Show highest scoring fragments first.
        self.all_results.order = SCORE
        self.all_results.formatter = HtmlFormatter(tagname='span', classname='match')

        # NOTE: highlighting the matched fragments is slow, so only do
        # highlighting on the first page of results.

        return self.highlight_results_page(0)

    def get_all_results(self, highlight: bool = False) -> List[SearchResult]:
        if highlight:
            return list(map(self._result_with_snippet_highlight, self.all_results))
        else:
            return list(map(self._result_with_content_no_highlight, self.all_results))


class SearchIndexed:
    suttas_index: FileIndex
    dict_words_index: FileIndex

    def __init__(self):
        self.open_all()

    def index_all(self, db_session, only_if_empty: bool = False):
        if (not only_if_empty) or (only_if_empty and self.suttas_index.is_empty()):
            print("Indexing suttas ...")

            suttas: List[USutta] = db_session.query(Am.Sutta).all()
            self.index_suttas('appdata', suttas)

            suttas: List[USutta] = db_session.query(Um.Sutta).all()
            self.index_suttas('userdata', suttas)

        if (not only_if_empty) or (only_if_empty and self.dict_words_index.is_empty()):
            print("Indexing dict_words ...")

            words: List[UDictWord] = db_session.query(Am.DictWord).all()
            self.index_dict_words('appdata', words)

            words: List[UDictWord] = db_session.query(Um.DictWord).all()
            self.index_dict_words('userdata', words)

    def open_all(self):
        self.suttas_index: FileIndex = self._open_or_create_index('suttas', SuttasIndexSchema)
        self.dict_words_index: FileIndex = self._open_or_create_index('dict_words', DictWordsIndexSchema)

    def create_all(self, remove_if_exists: bool = True):
        if remove_if_exists and INDEX_DIR.exists():
            shutil.rmtree(INDEX_DIR)
        self.open_all()

    def _open_or_create_index(self, index_name: str, index_schema: SchemaClass) -> FileIndex:
        if not INDEX_DIR.exists():
            INDEX_DIR.mkdir(exist_ok=True)

        try:
            ix = open_dir(dirname = INDEX_DIR, indexname = index_name, schema = index_schema)
            return ix
        except Exception as e:
            logger.info(f"Can't open the index: {index_name}")
            print(e)

        try:
            ix = create_in(dirname = INDEX_DIR, indexname = index_name, schema = index_schema)
        except Exception as e:
            logger.error(f"Can't create the index: {index_name}")
            print(e)
            exit(1)

        return ix

    def index_suttas(self, schema_name: str, suttas: List[USutta]):
        ix = self.suttas_index

        try:
            # NOTE: Only use multisegment=True when indexing from scratch.
            # Memory limit applies to each process individually.
            writer = ix.writer(procs=4, limitmb=256, multisegment=True)

            for i in suttas:
                # Prefer the html content field if not empty.
                if i.content_html is not None and len(i.content_html.strip()) > 0:
                    content = compactRichText(i.content_html) # type: ignore
                elif i.content_plain is not None:
                    content = compactPlainText(i.content_plain) # type: ignore
                else:
                    continue

                # Add title and title_pali to content field so a single field query will match
                # Db fields can be None
                c = list(filter(lambda x: x is not None, [i.sutta_ref, i.title, i.title_pali]))
                pre = " ".join(c) # type: ignore
                if len(pre) > 0:
                    content = f"{pre} {content}"

                writer.update_document(
                    index_key = f"{schema_name}:suttas:{i.uid}",
                    db_id = i.id,
                    schema_name = schema_name,
                    uid = i.uid,
                    title = i.title,
                    title_pali = i.title_pali,
                    title_trans = i.title_trans,
                    content = content,
                    ref = i.sutta_ref,
                )
            writer.commit()

        except Exception as e:
            logger.error("Can't index.")
            print(e)

    def index_dict_words(self, schema_name: str, words: List[UDictWord]):
        print("index_dict_words()")
        ix = self.dict_words_index

        try:
            # NOTE: Only use multisegment=True when indexing from scratch.
            # Memory limit applies to each process individually.
            writer = ix.writer(procs=4, limitmb=256, multisegment=True)
            for i in words:
                # Prefer the html content field if not empty
                if i.definition_html is not None and len(i.definition_html.strip()) > 0:
                    content = compactRichText(i.definition_html) # type: ignore
                elif i.definition_plain is not None:
                    content = compactPlainText(i.definition_plain) # type: ignore
                else:
                    continue

                # Add word and synonyms to content field so a single query will match
                if i.word is not None:
                    content = f"{i.word} {content}"

                if i.synonyms is not None:
                    content = f"{content} {i.synonyms}"

                writer.update_document(
                    index_key = f"{schema_name}:dict_words:{i.uid}",
                    db_id = i.id,
                    schema_name = schema_name,
                    uid = i.uid,
                    word = i.word,
                    synonyms = i.synonyms,
                    content = content,
                )
            writer.commit()

        except Exception as e:
            logger.error("Can't index.")
            print(e)

