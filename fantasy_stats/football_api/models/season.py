from typing import List

from football_api.database import db
from football_api.core.model import BaseModel


class Season(BaseModel):
    """
    Season Flask-SQLAlchemy Model
    Represents objects contained in the seasons table
    """

    __tablename__ = "seasons"

    year = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, year):
        self.year = year

    def __repr__(self):
        return f"**Season** year: {self.year} **Season**"

    @classmethod
    def find_by_name(cls, name) -> "Season":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Season":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Season"]:
        return cls.query.all()
