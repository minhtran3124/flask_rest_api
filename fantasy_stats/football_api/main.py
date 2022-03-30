import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from football_api.constants import DATABASE_LOCATION

from app import create_app


if __name__ == "__main__":
    app = create_app(DATABASE_LOCATION)
    app.run(debug=True)
