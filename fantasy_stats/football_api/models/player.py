from typing import List

from football_api.database import db
from football_api.core.model import BaseModel


class Player(BaseModel):
    """
    Player Flask-SQLAlchemy Model
    Represents objects contained in the players table
    """

    __tablename__ = 'players'

    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    stats = db.relationship('Stats', back_populates='player')

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return (
            f"**Player** "
            f"player_id: {self.player_id} "
            f"name: {self.name} "
            f"position: {self.position}"
            f"**Player** "
        )

    @classmethod
    def find_by_name(cls, name) -> "Player":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Player":
        return cls.query.filter_by(player_id=_id).first()

    @classmethod
    def find_by_position(cls, _position) -> "Player":
        return cls.query.filter_by(position=_position).all()

    @classmethod
    def find_all(cls) -> List["Player"]:
        return cls.query.all()
