from dbal.data_store import DataStore, create_ds


class _Singletons:
    ds = None


def init_ds(db):
    _Singletons.ds = create_ds(db)


def ds() -> DataStore:
    return _Singletons.ds
