from collections.abc import AsyncIterator

from axiom_core.database import session_factory
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db() -> AsyncIterator[AsyncSession]:
    async with session_factory() as session:
        yield session
