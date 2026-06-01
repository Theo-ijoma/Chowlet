from typing import TYPE_CHECKING
from uuid import uuid4
from uuid import UUID as PyUUID

from sqlalchemy import Boolean, String  # type: ignore[import]
from sqlalchemy.dialects.postgresql import UUID  # type: ignore[import]
from sqlalchemy.orm import Mapped, mapped_column, relationship  # type: ignore[import]

from app.db.base import Base

if TYPE_CHECKING:
    from app.db.models.user import User


class School(Base):
    __tablename__ = "schools"

    id: Mapped[PyUUID] = mapped_column(
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

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="school"
    )
