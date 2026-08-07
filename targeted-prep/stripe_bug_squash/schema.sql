DROP TABLE IF EXISTS partner_transactions;
DROP TABLE IF EXISTS internal_transactions;
DROP TABLE IF EXISTS partner_sync_runs;

CREATE TABLE partner_sync_runs (
    run_id            BIGINT PRIMARY KEY,
    partner_id        TEXT NOT NULL,
    started_at        TIMESTAMPTZ NOT NULL,
    completed_at      TIMESTAMPTZ,
    status            TEXT NOT NULL CHECK (status IN ('completed', 'partial', 'failed')),
    records_received  INTEGER NOT NULL,
    error_count       INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE internal_transactions (
    internal_txn_id        BIGINT PRIMARY KEY,
    partner_id             TEXT NOT NULL,
    partner_transaction_id TEXT,
    user_id                BIGINT NOT NULL,
    amount_minor           BIGINT NOT NULL,
    currency               TEXT NOT NULL,
    status                 TEXT NOT NULL,
    occurred_at            TIMESTAMPTZ NOT NULL,
    ingested_at            TIMESTAMPTZ NOT NULL,
    sync_run_id            BIGINT,
    FOREIGN KEY (sync_run_id) REFERENCES partner_sync_runs(run_id)
);

CREATE TABLE partner_transactions (
    partner_row_id          BIGINT PRIMARY KEY,
    partner_id              TEXT NOT NULL,
    partner_transaction_id  TEXT NOT NULL,
    amount_minor            BIGINT NOT NULL,
    currency                TEXT NOT NULL,
    status                  TEXT NOT NULL,
    occurred_at             TIMESTAMPTZ NOT NULL,
    received_at             TIMESTAMPTZ NOT NULL,
    sync_run_id             BIGINT NOT NULL,
    FOREIGN KEY (sync_run_id) REFERENCES partner_sync_runs(run_id)
);

CREATE INDEX idx_internal_partner_txn
    ON internal_transactions(partner_id, partner_transaction_id);

CREATE INDEX idx_partner_partner_txn
    ON partner_transactions(partner_id, partner_transaction_id);

CREATE INDEX idx_partner_sync_run
    ON partner_transactions(sync_run_id);
