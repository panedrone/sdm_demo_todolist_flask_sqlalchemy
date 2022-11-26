from flask_marshmallow import Marshmallow


class _Ma:
    ma: Marshmallow


def init_marshmallow(flask_app):
    _Ma.ma = Marshmallow(flask_app)


def ma() -> Marshmallow:
    return _Ma.ma
