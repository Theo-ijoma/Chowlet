"""Initial Chowlet tenant schema.

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-06-01
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "0001_initial_schema"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


user_role = postgresql.ENUM(
    "student",
    "restaurant",
    "rider",
    "school_admin",
    "super_admin",
    name="user_role",
)


def upgrade() -> None:
    user_role.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "schools",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("slug"),
    )

    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("school_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.String(length=20), nullable=True),
        sa.Column("role", user_role, nullable=False),
        sa.Column("supabase_id", sa.String(length=255), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["school_id"], ["schools.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("school_id", "email", name="uq_users_school_email"),
        sa.UniqueConstraint("supabase_id"),
    )
    op.create_index("ix_users_school_id", "users", ["school_id"])


def downgrade() -> None:
    op.drop_index("ix_users_school_id", table_name="users")
    op.drop_table("users")
    op.drop_table("schools")
    user_role.drop(op.get_bind(), checkfirst=True)
