"""create organization and user domain tables

Revision ID: 0001_organization_user
Revises:
Create Date: 2026-11-18
"""

import sqlalchemy as sa
from alembic import op

revision = "0001_organization_user"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "organizations",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="pk_organizations"),
        sa.UniqueConstraint("slug", name="uq_organizations_slug"),
        sa.CheckConstraint(
            "length(trim(name)) >= 2",
            name="ck_organizations_organization_name_min_length",
        ),
        sa.CheckConstraint(
            "slug = lower(slug)",
            name="ck_organizations_organization_slug_lowercase",
        ),
        sa.CheckConstraint(
            "length(slug) >= 2",
            name="ck_organizations_organization_slug_min_length",
        ),
    )

    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("organization_id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("display_name", sa.String(length=200), nullable=False),
        sa.Column(
            "status",
            sa.String(length=32),
            nullable=False,
            server_default="active",
        ),
        sa.Column(
            "external_subject",
            sa.String(length=255),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.id"],
            name="fk_users_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_users"),
        sa.UniqueConstraint(
            "organization_id",
            "email",
            name="uq_users_organization_email",
        ),
        sa.CheckConstraint(
            "length(trim(display_name)) >= 1",
            name="ck_users_user_display_name_min_length",
        ),
        sa.CheckConstraint(
            "email = lower(email)",
            name="ck_users_user_email_lowercase",
        ),
        sa.CheckConstraint(
            "status IN ('active', 'suspended', 'deactivated')",
            name="ck_users_user_status_valid",
        ),
    )

    op.create_index(
        "ix_users_organization_status",
        "users",
        ["organization_id", "status"],
        unique=False,
    )

    op.create_index(
        "ix_users_organization_created_at",
        "users",
        ["organization_id", "created_at"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_users_organization_created_at",
        table_name="users",
    )

    op.drop_index(
        "ix_users_organization_status",
        table_name="users",
    )

    op.drop_table("users")
    op.drop_table("organizations")
