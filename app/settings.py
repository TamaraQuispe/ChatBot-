"""Configuración centralizada de la aplicación."""

import os
from dataclasses import dataclass, field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    # Database
    DATABASE_URL: str = field(default_factory=lambda: os.environ.get("DATABASE_URL", ""))
    DB_MIN_CONN: int = int(os.environ.get("DB_MIN_CONN", "1"))
    DB_MAX_CONN: int = int(os.environ.get("DB_MAX_CONN", "10"))

    # Server
    PORT: int = int(os.environ.get("PORT", "8000"))
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    DEBUG: bool = os.environ.get("DEBUG", "false").lower() == "true"

    # JWT / Auth
    JWT_SECRET: str = field(default_factory=lambda: os.environ.get("JWT_SECRET") or os.environ.get("SESSION_SECRET", "utp-chatbot-secret-dev-key-2024"))
    JWT_ACCESS_EXPIRY: int = int(os.environ.get("JWT_ACCESS_EXPIRY", "86400"))
    JWT_REFRESH_EXPIRY: int = int(os.environ.get("JWT_REFRESH_EXPIRY", "2592000"))
    SESSION_COOKIE: str = os.environ.get("SESSION_COOKIE", "utp_session")

    # OpenRouter
    OPENROUTER_API_KEY: str = field(default_factory=lambda: os.environ.get("OPENROUTER_API_KEY", ""))

    # Logging
    LOG_DIR: str = os.environ.get("LOG_DIR", "logs")
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "DEBUG").upper()

    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = int(os.environ.get("RATE_LIMIT_REQUESTS", "60"))
    RATE_LIMIT_WINDOW: int = int(os.environ.get("RATE_LIMIT_WINDOW", "60"))

    # CORS
    CORS_ORIGINS: list[str] = field(default_factory=lambda: os.environ.get("CORS_ORIGINS", "*").split(","))
    CORS_METHODS: str = os.environ.get("CORS_METHODS", "GET,POST,PUT,DELETE,OPTIONS")
    CORS_HEADERS: str = os.environ.get("CORS_HEADERS", "Content-Type,Authorization,Cookie")

    def is_database_configured(self) -> bool:
        return bool(self.DATABASE_URL)

    def is_openrouter_configured(self) -> bool:
        return bool(self.OPENROUTER_API_KEY)


settings = Settings()
