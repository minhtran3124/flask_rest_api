from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    db_url: str
    host: str
    port: int
    debug: bool

    class Config:
        env_file = ".env"


settings = Settings()
