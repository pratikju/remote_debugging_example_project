from typing import Dict

from remote_debugging.store import db
from remote_debugging.store.models import Sample as SampleModel


class SampleRepo:
    def __init__(self):
        self._db = db

    def create(self, data: Dict):
        model = SampleModel(raw_data=data)

        self._db.session.add(model)
        self._db.session.commit()
