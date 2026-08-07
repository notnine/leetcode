# Stripe Bug Squash SQL Practice

## Scenario

You are investigating a reliability alert for transaction synchronization between an internal system and external financial partners.

The alert says that **reconciliation quality has degraded over the last several days**. Your job is to use SQL to determine:

- whether there is a real issue,
- where it is concentrated,
- what kinds of discrepancies exist,
- when the degradation appears to have started,
- how large the affected scope is,
- and what you would recommend doing next.

Do not assume the tables are perfectly clean or that joins are one-to-one.

## Tables

### `internal_transactions`

One row represents an internal transaction record.

Important columns:

- `internal_txn_id` — internal primary key
- `partner_id` — financial partner
- `partner_transaction_id` — partner-provided transaction identifier when available
- `user_id`
- `amount_minor` — amount in minor currency units
- `currency`
- `status`
- `occurred_at`
- `ingested_at`
- `sync_run_id`

### `partner_transactions`

One row represents a row received from a financial partner.

Important columns:

- `partner_row_id` — row-level primary key for the received record
- `partner_id`
- `partner_transaction_id`
- `amount_minor`
- `currency`
- `status`
- `occurred_at`
- `received_at`
- `sync_run_id`

### `partner_sync_runs`

One row represents a partner synchronization run.

Important columns:

- `run_id`
- `partner_id`
- `started_at`
- `completed_at`
- `status`
- `records_received`
- `error_count`

## Local setup

### Option A: Docker

Start Postgres:

```bash
docker run \
  --name stripe-sql \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=stripe \
  -p 5432:5432 \
  -d postgres:16
```

Load the schema and seed data from this directory:

```bash
psql postgresql://postgres:postgres@localhost:5432/stripe \
  -f schema.sql \
  -f seed.sql
```

If `psql` is not installed locally, you can run it inside the container:

```bash
docker exec -i stripe-sql psql -U postgres -d stripe < schema.sql
docker exec -i stripe-sql psql -U postgres -d stripe < seed.sql
```

Run your scratch file:

```bash
docker exec -i stripe-sql psql -U postgres -d stripe < solution.sql
```

## Interview-style rules

Treat this like the Stripe Bug Squash round:

1. Explain what you want to learn before writing a query.
2. Start with simple baselines rather than one giant query.
3. Check grain and uniqueness before trusting joined counts.
4. Form a hypothesis, then test it.
5. Validate any important conclusion independently.
6. Quantify impact.
7. Finish with a concise summary of cause, scope, confidence, and next steps.

There are intentionally no hints about what issues exist in the dataset.
