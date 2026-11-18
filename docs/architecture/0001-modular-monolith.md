# ADR 0001: Start as a Modular Monolith

## Status

Accepted.

## Decision

Axiom starts as a modular monolith with explicit Python package boundaries.

Initial deployable units:

- API
- future background worker
- PostgreSQL

We will extract a service only when scaling, isolation, security, or ownership requirements justify it.

## Rationale

Premature microservices add operational complexity before the domain and runtime contracts are proven. A modular monolith gives us transactional consistency, simple local development, easier debugging/replay, and a clean extraction path later.
