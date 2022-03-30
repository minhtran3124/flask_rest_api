from football_api.database import db


class Season(db.Model):
    """
    Season Flask-SQLAlchemy Model
    Represents objects contained in the seasons table
    """

    __tablename__ = "seasons"

    year = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"**Season** year: {self.year} **Season**"
