from contextlib import asynccontextmanager

from fastapi import FastAPI

from axiom_api.routes.health import router as health_router
from axiom_core.config import get_settings
from axiom_core.logging import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging(get_settings().log_level)
    yield


app = FastAPI(title="Axiom API", version="0.1.0", lifespan=lifespan)
app.include_router(health_router)
