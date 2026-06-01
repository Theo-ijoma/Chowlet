from uuid import uuid4

from sqlalchemy import String  # type: ignore[import]
from sqlalchemy.dialects.postgresql import UUID  # type: ignore[import]
from sqlalchemy.orm import Mapped, mapped_column  # type: ignore[import]

from app.db.base import Base


class School(Base):
    __tablename__ = "schools"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )