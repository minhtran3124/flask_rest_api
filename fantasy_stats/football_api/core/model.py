from football_api.database import db


class BaseModel(db.Model):
    """
    Player Flask-SQLAlchemy Model

    Represents objects contained in the players table
    """

    __abstract__ = True

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
