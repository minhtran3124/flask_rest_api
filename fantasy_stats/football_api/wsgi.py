import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from app import app


if __name__ == "__main__":
    app.run(debug=True)
