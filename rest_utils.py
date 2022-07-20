from flask import jsonify

from dbal.data_store import Base


def _to_json(obj):
    if obj is None:
        return None
    if isinstance(obj, list):
        if len(obj) > 0:
            if isinstance(obj[0], Base):
                res = [o.__dict__ for o in obj]
                # there is no '_sa_instance_state' for __abstract__
                if '_sa_instance_state' in res[0]:
                    [r.pop('_sa_instance_state', None) for r in res]
            else:
                res = obj
        else:
            res = obj
    elif isinstance(obj, Base):
        # https://stackoverflow.com/questions/1958219/how-to-convert-sqlalchemy-row-object-to-a-python-dict
        res = dict(obj.__dict__)
        res.pop('_sa_instance_state', None)
    else:
        if isinstance(obj, dict):
            res = obj
        else:
            res = obj.__dict__
    return res


def _to_json_str(obj):
    res = _to_json(obj)
    return jsonify(res)


def json_response(res):
    # Content-Type: application/json
    # and httpCode 200
    # are set without specifying in code
    return _to_json_str(res)
