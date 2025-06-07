from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Simple Booking API"

    database_url: str = "sqlite:///./database.db"

    environment: str = "development"

    class Config:
        env_file = ".env"  # Load from .env file
        case_sensitive = False

# Create a global settings instance
settings = Settings()

def get_settings() -> Settings:
    return Settings()
