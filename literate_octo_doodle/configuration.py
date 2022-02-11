import os

DEFAULT_BOOK_FIELDS = (
    "_id,title,is_comercial,isbn,eisbn,doi_number,use_licence,publisher,language"
)
DEFAULT_CHAPTER_FIELDS = (
    "_id,monograph_title,title,order,monograph,descriptive_information"
)

###########################################################################

SERVER = os.environ.get('SERVER') or 'http://couchdb.domain.org:5984'
DATABASE = os.environ.get("DATABASE") or 'database_name'
BOOK_FIELDS = (
    os.environ.get("BOOK_FIELDS") or DEFAULT_BOOK_FIELDS
)
CHAPTER_FIELDS = (
    os.environ.get("CHAPTER_FIELDS") or DEFAULT_CHAPTER_FIELDS
)

###########################################################################

print(
    f"""
    Running with:

    SERVER = {SERVER}
    DATABASE = {DATABASE}
    BOOK_FIELDS = {BOOK_FIELDS}
    CHAPTER_FIELDS = {CHAPTER_FIELDS}
    """
)