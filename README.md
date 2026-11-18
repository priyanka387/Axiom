# Axiom

**Enterprise AI Workforce Platform**

Axiom is a production-oriented platform for building AI workers that execute real enterprise business processes while respecting permissions, policies, approvals, and audit requirements.

The first reference workflow is **Duplicate Payment Resolution**:

`request → investigate → verify → apply policy → calculate action → approve when required → execute → update systems → notify → verify`

## Why Axiom

Most agent demos stop at "LLM + tools". Axiom treats an enterprise agent as a controlled execution system:

- durable workflow state
- typed tool contracts
- authorization and policy decisions
- human approval as a first-class state
- idempotent business actions
- audit trails
- observability and replay
- deterministic evaluation

## Current milestone

**Milestone 1 — Production Foundation**

This repository establishes the backend foundation:

- FastAPI
- Pydantic Settings
- SQLAlchemy 2 async
- PostgreSQL
- Alembic
- structured JSON logging
- health/readiness endpoints
- pytest
- Ruff
- mypy
- Docker Compose
- GitHub Actions

No agent autonomy is implemented yet. That is intentional: the runtime will be built on a tested foundation.

## Local development

Requirements: Python 3.11+, uv, Docker.

```bash
cp .env.example .env
docker compose up -d postgres
uv sync
uv run uvicorn axiom_api.main:app --reload
```

API:

- `GET /health/live`
- `GET /health/ready`
- `GET /docs`

Checks:

```bash
make test
make lint
make typecheck
```

## Roadmap

1. Production foundation
2. Core domain model
3. Tool registry and execution
4. Agent runtime
5. Policy engine
6. Human approval
7. Duplicate Payment Resolution vertical slice
8. Observability and tracing
9. Evaluation and replay
10. Enterprise AI Workforce
11. Multi-tenancy and production hardening

## Engineering principles

- modular monolith first
- explicit contracts over magic
- policy is outside the model
- dangerous actions require authorization
- every side effect is observable and auditable
- retries must be safe
- business workflows must be resumable
- evaluation is part of development, not an afterthought

## License

Apache-2.0.
