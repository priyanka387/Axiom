from uuid import UUID

from axiom_core.base import Base, CreatedAt, UpdatedAt, UUIDPk
from sqlalchemy import CheckConstraint, ForeignKey, Index, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Organization(Base):
    """Tenant boundary for Axiom."""

    __tablename__ = "organizations"

    __table_args__ = (
        UniqueConstraint("slug", name="uq_organizations_slug"),
        CheckConstraint(
            "length(trim(name)) >= 2",
            name="organization_name_min_length",
        ),
        CheckConstraint(
            "slug = lower(slug)",
            name="organization_slug_lowercase",
        ),
        CheckConstraint(
            "length(slug) >= 2",
            name="organization_slug_min_length",
        ),
    )

    id: Mapped[UUIDPk]
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    users: Mapped[list["User"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class User(Base):
    """Organization-scoped user/principal."""

    __tablename__ = "users"

    __table_args__ = (
        UniqueConstraint(
            "organization_id",
            "email",
            name="uq_users_organization_email",
        ),
        Index(
            "ix_users_organization_status",
            "organization_id",
            "status",
        ),
        Index(
            "ix_users_organization_created_at",
            "organization_id",
            "created_at",
        ),
        CheckConstraint(
            "length(trim(display_name)) >= 1",
            name="user_display_name_min_length",
        ),
        CheckConstraint(
            "email = lower(email)",
            name="user_email_lowercase",
        ),
        CheckConstraint(
            "status IN ('active', 'suspended', 'deactivated')",
            name="user_status_valid",
        ),
    )

    id: Mapped[UUIDPk]

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "organizations.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="active",
        server_default="active",
    )

    external_subject: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]

    organization: Mapped[Organization] = relationship(
        back_populates="users",
    )
