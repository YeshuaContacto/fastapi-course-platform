from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = "Platziflix"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/platziflix"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Crear instancia global de configuración
settings = Settings()
