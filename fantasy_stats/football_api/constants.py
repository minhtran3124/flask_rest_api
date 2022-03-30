from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

FANTASY_FOOTBALL_DATABASE = "fantasy_football.db"
DATABASE_LOCATION = f"sqlite:////{PROJECT_ROOT}/{FANTASY_FOOTBALL_DATABASE}"
