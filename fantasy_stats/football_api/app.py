import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from flask import Flask

from football_api.database import db
from apis import init_api


def create_app(db_location):
    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-RESTful API,
    and Flask-SQLAlchemy connection

    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """

    # This configures our logging
    # writing all logs to the file "football_api.log"
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("football_api.log"), logging.StreamHandler()],
    )

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)

    # Initialize APIs for app
    return init_api(app)
