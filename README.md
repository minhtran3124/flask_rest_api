# Building a RESTful API with Flask, Flask-RESTful, SQLAlchemy and pytest

## What is REST

- Follow wikipedia: https://en.wikipedia.org/wiki/Representational_state_transfer

## Technical Stacks

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)

### Flask

- Is a lightweight WSGI web application framework

### Flask-RESTful

- Is an extension for Flask that adds support for quickly building REST APIs

### Flask-SQLAlchemy

- Is an extension for Flask that adds support for SQLAlchemy to a Flask application
- It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks

### Marshmallow

- Simplified Object Serialization
- Is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes

## Required

- Python 3.9

## Database

- SQLite

## Project Structure

    fantasy_stats
    ┣ football_api
    ┃ ┣ models
    ┃ ┃ ┣ __init__.py
    ┃ ┃ ┣ player.py
    ┃ ┃ ┣ season.py
    ┃ ┃ ┣ stats.py
    ┃ ┃ ┗ team.py
    ┃ ┣ resources
    ┃ ┃ ┣ __init__.py
    ┃ ┃ ┣ players_resource.py
    ┃ ┃ ┣ seasons_resource.py
    ┃ ┃ ┣ stats_resources.py
    ┃ ┃ ┗ teams_resource.py
    ┃ ┣ schemas
    ┃ ┃ ┣ __init__.py
    ┃ ┃ ┣ player_schema.py
    ┃ ┃ ┣ season_schema.py
    ┃ ┃ ┣ stats_schema.py
    ┃ ┃ ┗ team_schema.py
    ┃ ┣ __init__.py
    ┃ ┣ api.py
    ┃ ┣ constants.py
    ┃ ┗ database.py
    ┣ tests
    ┃ ┣ integration
    ┃ ┃ ┣ __init__.py
    ┃ ┃ ┣ conftest.py
    ┃ ┃ ┣ test_players_resource.py
    ┃ ┃ ┣ test_seasons_resource.py
    ┃ ┃ ┣ test_stats_resource.py
    ┃ ┃ ┗ test_teams_resource.py
    ┃ ┗ __init__.py
    ┣ Makefile
    ┣ Pipfile
    ┣ Pipfile.lock
    ┣ fantasy_football.db
    ┣ football_api.log
    ┗ requirements.txt

## APIs

- Resource: players
    - POST  /api/players
    - GET   /api/players
    - GET   /api/players/<id>
- Resource: teams
    - POST  /api/teams
    - GET   /api/teams
    - GET   /api/teams/<id>
- Resource: seasons
    - POST  /api/seasons
    - GET   /api/seasons
- Resource: stats
    - GET   /api/stats/players/<id>
    - GET   /api/stats/season/


## How to Run

- Install dependencies
    ```
    pipenv install --dev
    ```

- Active virtualenv
    ```
    pipenv shell
    ```

## How to Test

- Run unit test
    ```
    pytest tests
    ```

- Run test coverage
    ```
    pytest --cov football_api
    ```