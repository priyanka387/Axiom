from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from axiom_api.dependencies import get_db

router = APIRouter(tags=["health"])


@router.get("/health/live")
async def live() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/health/ready")
async def ready(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> dict[str, str]:
    await db.execute(text("SELECT 1"))
    return {"status": "ready"}
