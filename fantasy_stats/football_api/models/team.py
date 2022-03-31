from typing import List

from football_api.database import db
from football_api.core.model import BaseModel


class Team(BaseModel):
    """
    Team Flask-SQLAlchemy Model
    Represents objects contained in the teams table
    """

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    abbreviation = db.Column(db.String(), unique=True, nullable=False)
    stats = db.relationship("Stats", back_populates="team")

    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation

    def __repr__(self):
        return (
            f"**Team** "
            f"team_id: {self.team_id} "
            f"name: {self.name} "
            f"abbreviation: {self.abbreviation}"
            f"**Team** "
        )

    @classmethod
    def find_by_name(cls, name) -> "Team":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Team":
        return cls.query.filter_by(team_id=_id).first()

    @classmethod
    def find_all(cls) -> List["Team"]:
        return cls.query.all()
