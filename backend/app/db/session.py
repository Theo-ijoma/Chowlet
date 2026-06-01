from sqlalchemy import create_engine  # type: ignore[import]
from sqlalchemy.orm import sessionmaker  # type: ignore[import]

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)