from uuid import uuid4

from axiom_core.domain.models import Organization, User


def test_organization_has_stable_identity_and_slug() -> None:
    organization = Organization(
        id=uuid4(),
        name="Acme Corp",
        slug="acme-corp",
    )

    assert organization.id is not None
    assert organization.name == "Acme Corp"
    assert organization.slug == "acme-corp"


def test_user_belongs_to_organization() -> None:
    organization = Organization(
        id=uuid4(),
        name="Acme Corp",
        slug="acme-corp",
    )

    user = User(
        id=uuid4(),
        organization=organization,
        email="owner@acme.example",
        display_name="Acme Owner",
    )

    assert user.organization_id == organization.id
    assert user.organization is organization
    assert user.status == "active"
