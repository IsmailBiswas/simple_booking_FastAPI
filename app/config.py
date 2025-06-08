from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    app_name: str = "Simple Booking API"
    database_url: str = "sqlite:///./database.db"

    env_file: str = ".env.dev"
    if os.getenv("PRODUCTION"):
        env_file = ".env"
    elif os.getenv("TESTING"):
        env_file = ".env.test"

    model_config = SettingsConfigDict(
        env_file = env_file,
        case_sensitive=False,
    )


# Create a global settings instance
settings = Settings()

def get_settings() -> Settings:
    return Settings()
