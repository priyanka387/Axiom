# Architecture

Axiom is being built as a modular monolith.

The architectural boundary is intentional: the model proposes actions, while deterministic application code enforces authorization, policy, state transitions, and side-effect safety.

See ADR 0001 for the initial deployment decision.
