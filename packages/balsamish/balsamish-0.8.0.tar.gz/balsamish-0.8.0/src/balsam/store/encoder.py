import datetime
import json

from balsam import selection


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # pylint: disable=arguments-differ, method-hidden
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        if isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        if isinstance(obj, selection.Selection):
            return selection.to_dict(obj)

        return super(CustomEncoder, self).default(obj)
