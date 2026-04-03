# Decisions

## ADR-001: Stage-separated ETL modules

- Status: accepted
- Decision: Keep ingest/transform/load as explicit module boundaries.
- Why: Makes each stage independently testable and replaceable.

## ADR-002: Validate before write

- Status: accepted
- Decision: Enforce schema checks before writing persisted output.
- Why: Prevents silent corruption in downstream consumers.

## ADR-003: Keep pipeline orchestration thin

- Status: accepted
- Decision: `run_pipeline` coordinates only; logic remains inside stages.
- Why: Reduces orchestration complexity and improves maintainability.
