-- Write your investigation queries here.
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
  AND table_type = 'BASE TABLE';

-- Assume:

-- one logical account = (partner_id, external_account_id)
-- records should be compared within the same sync run
-- correctness fields are balance_minor, currency, and account_status
-- sync-run metadata should be validated rather than blindly trusted

-- note: to engage the interviewer, i will make it clear on what i am currently doing.

-- investigation: first, i look at all our tables to get a sense of our schema, and to skim through the data that is stored in our db.

select * from account_sync_runs asr 

select * from partner_account_snapshots pas 

select * from internal_account_snapshots ias 

-- findings: looking at asr, i noticed that there is 1 run id 3004 that took almost 10 mins, much longer than the typical 2 mins. this run id is linked with partner bank_gamma, received 6 records, and has 2 error_count
-- approach: before diving deeper into this specific run id, it's better to compare pas and ias as a whole first. by doing this, we can pinpoint specific problematic account snapshots, and missing or duplicated accounts snapshots from either side.
-- problematic accounts can be snapshots where any of our invariants do not agree (balance_minor, currency, or account_status) for the same partner and account.

-- investigation 1: find missing accounts snapshots from either side
with missing_internal_snapshots as (
	select pas.partner_id, pas.external_account_id as eaid1, pas.sync_run_id, ias.partner_id, ias.external_account_id as eaid2, ias.sync_run_id
	from partner_account_snapshots pas 
	left join internal_account_snapshots ias
	on pas.partner_id = ias.partner_id and pas.external_account_id = ias.external_account_id and pas.sync_run_id = ias.sync_run_id
),
missing_external_snapshots as (
	select pas.partner_id, pas.external_account_id as eaid1, pas.sync_run_id, ias.partner_id, ias.external_account_id as eaid2, ias.sync_run_id
	from partner_account_snapshots pas 
	right join internal_account_snapshots ias
	on pas.partner_id = ias.partner_id and pas.external_account_id = ias.external_account_id and pas.sync_run_id = ias.sync_run_id
)
select * from missing_internal_snapshots
where eaid2 is null
union all
select * from missing_external_snapshots
where eaid1 is null
-- findings 1: there is a missing internal snapshot. partner bank gamma has a external account id G-006 with sync run 3,004 that does not exist internally.

-- investigation 2: find duplicates from either side
with duplicate_internal_snapshots as (
	select ias.partner_id, ias.external_account_id, ias.sync_run_id, count(*) as count
	from internal_account_snapshots ias 
	group by ias.partner_id, ias.external_account_id, ias.sync_run_id
	having count(*) > 1
),
duplicate_external_snapshots as (
	select pas.partner_id, pas.external_account_id, pas.sync_run_id, count(*) as count
	from partner_account_snapshots pas 
	group by pas.partner_id, pas.external_account_id, pas.sync_run_id
	having count(*) > 1
)
select * from duplicate_internal_snapshots 
union all
select * from duplicate_external_snapshots
-- finding 2: the query returned nothing, meaning that there are no duplicate records internally and externally.

-- investigation 3: investigate the existance of problematic account snapshots. i.e ones that violate our invariant (balance_minor, currency, or account_status)
select *
from internal_account_snapshots ias 
join partner_account_snapshots pas 
on ias.partner_id = pas.partner_id and ias.external_account_id = pas.external_account_id and ias.sync_run_id = pas.sync_run_id
where ias.balance_minor != pas.balance_minor or ias.currency != pas.currency or ias.account_status != pas.account_status 
-- finding 3: internal row id shows this account snapshot as having status open, while it has status closed in the partner snapshot. this is also of sync run id 3004

-- current findings
-- sync run id 3004 was problematic. account_sync_runs showed that it ran much longer, has partial completion status, and encountered 2 errors. There are no duplicate records internally and externally.
-- there is a missing internal snapshot with bank gamma, external accuont id G-006 with sync run 3,004. there is also a snapshot that breaks our invariant, with internal row id 30023 in our internal account
-- snapshots table. this snapshot is also under sync run 3004, and shows internally that the account has status open, while it has status closed in our partner's records.
-- we have not done a root cause analysis, so we do not know what the root causes are yet. the next step would be to investigate the cause specifically with run 3004, in which our missing and mismatching snapshots are from.
-- this investigation would contain looking through the logs of this sync run.
