from typing import TYPE_CHECKING
from enum import StrEnum
from uuid import uuid4
from uuid import UUID as PyUUID

from sqlalchemy import Boolean, Enum, ForeignKey, String, UniqueConstraint  # type: ignore[import]
from sqlalchemy.dialects.postgresql import UUID  # type: ignore[import]
from sqlalchemy.orm import Mapped, mapped_column, relationship  # type: ignore[import]

from app.db.base import Base

if TYPE_CHECKING:
    from app.db.models.school import School


class UserRole(StrEnum):
    STUDENT = "student"
    RESTAURANT = "restaurant"
    RIDER = "rider"
    SCHOOL_ADMIN = "school_admin"
    SUPER_ADMIN = "super_admin"


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        UniqueConstraint("school_id", "email", name="uq_users_school_email"),
    )

    id: Mapped[PyUUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    school_id: Mapped[PyUUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("schools.id"),
        index=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(
            UserRole,
            name="user_role",
            values_callable=lambda roles: [role.value for role in roles],
        ),
        nullable=False,
        default=UserRole.STUDENT
    )

    supabase_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    school: Mapped["School"] = relationship(
        back_populates="users"
    )
