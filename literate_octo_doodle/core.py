import couchdb
from literate_octo_doodle import configuration


def get_db(db_uri, db_name):
    """
    SERVER = http://couchdb.domain.org:5984
    DATABASE = scielobooks_1a
    """
    try:
        couch = couchdb.Server(db_uri)
        return couch[db_name]
    except IOError:
        print("Check SERVER and DATABASE configuration")
        exit()


_db = get_db(configuration.SERVER, configuration.DATABASE)


def get_data(filters, field_names):
    for _id in _db:
        _record = _db[_id]
        if selected(filters, _record):
            data = {}
            for k in field_names:
                data[k] = _record.get(k) or ""
            yield data


def selected(filters, _record):
    for name, value in filters.items():
        if not _record.get(name) == value:
            return
    return _record
