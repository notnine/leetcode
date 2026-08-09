# Stripe Bug Squash Mock 2

## Incident

A monitoring alert says **account snapshot reconciliation quality degraded recently**.

You have three tables:

- `account_sync_runs`: one row per partner sync run
- `partner_account_snapshots`: raw account snapshots received from partners
- `internal_account_snapshots`: Stripe's internally ingested account snapshots

Your task is to investigate the issue using SQL, determine scope and likely cause, and summarize next steps.

## Important assumptions

- A logical account is identified by `(partner_id, external_account_id)`.
- Compare records only when they represent the same logical account and the same sync run.
- Relevant correctness fields are `balance_minor`, `currency`, and `account_status`.
- Do not assume run metadata is always trustworthy; validate against the transaction/snapshot tables.

No bugs or anomaly locations are documented here.
