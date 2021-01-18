from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from remote_debugging.store import db


class Sample(db.Model):
    __tablename__ = "sample"

    id = db.Column(db.INTEGER, primary_key=True)
    raw_data = db.Column(JSONB)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
