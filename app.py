from dbal.data_store import DataStore, create_ds


class _App:
    ds = None  # Singleton


def init_ds(db):
    _App.ds = create_ds(db)


def ds() -> DataStore:
    return _App.ds
