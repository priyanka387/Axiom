install:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy apps/api/src packages/core/src

migrate:
	uv run alembic upgrade head

api:
	uv run uvicorn axiom_api.main:app --reload
