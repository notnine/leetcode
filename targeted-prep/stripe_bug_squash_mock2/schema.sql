DROP TABLE IF EXISTS partner_account_snapshots;
DROP TABLE IF EXISTS internal_account_snapshots;
DROP TABLE IF EXISTS account_sync_runs;

CREATE TABLE account_sync_runs (
    run_id BIGINT PRIMARY KEY,
    partner_id TEXT NOT NULL,
    started_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    status TEXT NOT NULL,
    records_received INT NOT NULL,
    error_count INT NOT NULL
);

CREATE TABLE partner_account_snapshots (
    partner_row_id BIGINT PRIMARY KEY,
    partner_id TEXT NOT NULL,
    external_account_id TEXT NOT NULL,
    balance_minor BIGINT NOT NULL,
    currency TEXT NOT NULL,
    account_status TEXT NOT NULL,
    snapshot_at TIMESTAMP NOT NULL,
    sync_run_id BIGINT NOT NULL REFERENCES account_sync_runs(run_id)
);

CREATE TABLE internal_account_snapshots (
    internal_row_id BIGINT PRIMARY KEY,
    partner_id TEXT NOT NULL,
    external_account_id TEXT NOT NULL,
    balance_minor BIGINT NOT NULL,
    currency TEXT NOT NULL,
    account_status TEXT NOT NULL,
    snapshot_at TIMESTAMP NOT NULL,
    ingested_at TIMESTAMP NOT NULL,
    sync_run_id BIGINT NOT NULL REFERENCES account_sync_runs(run_id)
);

CREATE INDEX idx_partner_account_key
    ON partner_account_snapshots(partner_id, external_account_id);

CREATE INDEX idx_internal_account_key
    ON internal_account_snapshots(partner_id, external_account_id);

CREATE INDEX idx_account_runs_partner_time
    ON account_sync_runs(partner_id, started_at);
