-- Stripe Bug Squash practice scratchpad
--
-- Suggested workflow:
-- 1) Clarify table grain and expected uniqueness.
-- 2) Establish baseline counts before joining.
-- 3) State a hypothesis before each focused query.
-- 4) Validate important findings with an independent query.
-- 5) End with scope, confidence, and recommended next step.

-- Start here:

-- hypothesis: are there transactions that violate our invariant? i.e, amount/currency/status b/w internal trx and partner's trx disagrees.

select *
from internal_transactions it
join partner_transactions pt 
on it.partner_id = pt.partner_id and it.partner_transaction_id = pt.partner_transaction_id
where it.amount_minor != pt.amount_minor or it.currency != pt.currency or it.status != pt.status

-- findings: found 1 trx that disagrees in currency, internal_txn_id 37.

-- next investigation: how did this trx get ingested, and whether there were faults.

select *
from partner_sync_runs psr 
where psr.run_id = 1004

-- assumption: psr.run_id is equal to it.sync_run_id.
-- findings: run_id 1004 has "partial" status, with error_count 3.
-- hypothesis: 1 of the 3 errors from run_id 1004 caused internal_txn_id 37 to have mismatching currencies. There are also 2 other errors we will investigate later.
-- approach: We can check our internal transactions and partner transactions that were processed by run_id 1004, and check each trx.

select *
from internal_transactions it
join partner_transactions pt 
on it.partner_id = pt.partner_id and it.partner_transaction_id = pt.partner_transaction_id
where it.sync_run_id = 1004 and (
	it.amount_minor != pt.amount_minor or
	it.currency != pt.currency or
	it.status != pt.status
)

-- findings: update, there's also internal_txn_id 39 that disagrees in status (posted vs pending)

-- investigation: check whether run_id 1004 is the only run_id with transactions that break our invariant
with mismatching_transactions as (
	select it.sync_run_id 
	from internal_transactions it 
	join partner_transactions pt
	on it.partner_id = pt.partner_id and it.partner_transaction_id = pt.partner_transaction_id
	where (
		it.amount_minor != pt.amount_minor or
		it.currency != pt.currency or
		it.status != pt.status
	)
)
select sync_run_id, count(sync_run_id)
from mismatching_transactions
group by sync_run_id
order by sync_run_id

-- findings: there's 2 mimsatching transactions with syn run id 1004, but since there's 3 errors, there's a 3rd error that we have potentially not found
-- hypothesis: there might be a duplicate, or missing transaction from sync run id 1004.
-- investigation: check whether there is a partner transaction partner_transaction_id that does not exist in internal transactions (missing partner transaction)

select *
from partner_transactions pt 
left join internal_transactions it 
ON pt.partner_id = it.partner_id
AND pt.partner_transaction_id = it.partner_transaction_id
where it.partner_transaction_id is null

-- findings: returned B-041, so partner transaction B-041 is missing from internal transactions. this transaction is from sync_run_id 2,005, and is with bank_beta. It's different from the 2 mismatching trxs.
-- hypotehsis: since there are missing transacitons, there might be duplicate trxns
-- investigation: search for duplicate internal trxs

select it.partner_id, it.partner_transaction_id, count(*)
from internal_transactions it 
group by it.partner_id, it.partner_transaction_id
having count(*) > 1

-- findings: there are no duplicate partner transactions in internal transactions
-- hypotehsis: are there internal trxs that do not exist in partner trxs?
-- investigation: search for rows in internal trxs that do not exist in partner trxs

select *
from internal_transactions it
left join partner_transactions pt 
on it.partner_id = pt.partner_id
and it.partner_transaction_id = pt.partner_transaction_id 
where pt.partner_transaction_id is null

-- findings: internal transactions has a bank_alpha trx with partner trx id A-040 that's missing from partner trxs
-- investigation: summarize all "bad trxs" found so far

with missing_partner_transactions as (
	select it.partner_id as partner_id, it.sync_run_id as sync_run_id, it.partner_transaction_id as partner_transaction_id, 'missing_partner' as issue_type
	from internal_transactions it
	left join partner_transactions pt 
	on it.partner_id = pt.partner_id
	and it.partner_transaction_id = pt.partner_transaction_id 
	where pt.partner_transaction_id is null),
missing_internal_transactions as (
	select pt.partner_id as partner_id, pt.sync_run_id as sync_run_id, pt.partner_transaction_id as partner_transaction_id, 'missing_internal' as issue_type
	from partner_transactions pt 
	left join internal_transactions it 
	ON pt.partner_id = it.partner_id
	AND pt.partner_transaction_id = it.partner_transaction_id
	where it.partner_transaction_id is null),
mismatching_transactions as (
	select it.partner_id as partner_id, it.sync_run_id as sync_run_id, it.partner_transaction_id as partner_transaction_id, 'mismatching_transaction' as issue_type
	from internal_transactions it 
	join partner_transactions pt
	on it.partner_id = pt.partner_id and it.partner_transaction_id = pt.partner_transaction_id
	where (
		it.amount_minor != pt.amount_minor or
		it.currency != pt.currency or
		it.status != pt.status
	)
),
all_issues as (select * from missing_partner_transactions union all select * from missing_internal_transactions union all select * from mismatching_transactions)
select partner_id, sync_run_id, issue_type, count(*) as issue_count
from all_issues
group by partner_id, sync_run_id, issue_type

-- findings: 1004 has 3 issues, with missing partner as 1, and mismatching transcations as 2. sync run id 2005 has 1 missing internal trx. 
-- hypotehsis: 1004 is problematic.
-- investigation: look into the sync runs and their timestamps, to see whether 1004 is isolated, or whether there is a pattern surrounding 1004.

select *, completed_at - started_at AS duration
from partner_sync_runs psr 
where psr.partner_id = 'bank_alpha'
order by started_at asc

-- findings: all our sync runs run once a day, at 5. most of the time they finish in 2 or 3 minutes, but sync run on august 4 took 14 minutes, 
-- and has partial status. more over, it only recieved 9 records, while every other sync run recieved 10 or 11.
-- investigation: not related to recent finding, but check whether there are duplicate partner trxs

select *
from partner_transactions pt1
join partner_transactions pt2
on pt1.partner_row_id != pt2.partner_row_id and pt1.partner_id = pt2.partner_id and pt1.partner_transaction_id = pt2.partner_transaction_id

-- findings: partner_row_ids 10,026 and 10,031 have the same partner_id and partner_transaction_id, so they are duplicates of each other. these occured with sync run 1003
-- investigation: did this duplicate partner trx create a duplicate internal trx?

select it.partner_id, it.partner_transaction_id, count(*) as count
from internal_transactions it 
group by it.partner_id, it.partner_transaction_id
having count(*) > 1

-- findings: we do not have duplicated internal trxs, so the ingestion process correctly deduplicated the partner trx.
-- investigation: check whether records received at partner sync runs match the actual partner transactions for each sync run
-- note: keep in mind the duplicate partner trx partner_row_ids 10,026 and 10,031 for sync run 1003

-- get the num of partner trxs per sync run from partner transactions
with partner_transactions_per_sync_run as (
	select pt.sync_run_id , count(*) as ptpsr_count
	from partner_transactions pt 
	group by pt.sync_run_id
)
select psr.run_id, psr.records_received, ptpsr.sync_run_id, ptpsr.ptpsr_count 
from partner_transactions_per_sync_run ptpsr
join partner_sync_runs psr
on ptpsr.sync_run_id = psr.run_id and ptpsr.ptpsr_count != psr.records_received 

-- findings: for sync run id 2005 we received 8, but ptpsr_count has 9. this correlates to the previous finding "partner transaction B-041 is missing from internal transactions. this transaction is from sync_run_id 2,005"

-- What did you find?
-- a: the key errors are: 1. trx disagrees in currency with internal_tx_id 37, partner bank_alpha, partner trx id A-037. Internally the currency is USD, while it's EUR on the partner's side. There is 1 trx that disagrees in
-- currency, with internal txn id 39, partner_id bank alpha, partner trx ID A-039. Internally it shows posted, while it shows pending on the partner's side. both of these come from the same sync run id 1004. Sync run id
-- 1004 looks problematic, as it has partially completed status, and took much longer than the others which finished in 2-3 mins. On top of the mismatching transactions, sync run id 1004 also has a trx that is missing on the
-- partner's side (i.e it only exists on our internal side). finally, there's also a trx that's missing internally with sync_run_id 2,005, partner transaction B-041. There's also duplicated partner trxs but we deduplicate these
-- correctly and there are no duplicate internal trxs on our side, so this is a no issue. so all in all, the main issues are: 2 mismatching trxs with sync run id 1,004 with bank alpha, 1 missing trx on partner's side with sync run
-- id 1,004 with bank alpha too, and 1 missing internal trx with sync run 2005 with bank beta.

-- What is your confidence?
-- i am highly confident because we compared our 3 tables using accurate sql queries.

-- What do you think is likely happening?
-- i think that the ineternally missing b-41 partner trx id is not a major issue, as it is the last partner trx we received, so there's a likelihood that our internal ingestion process is still processing this partner trx.
-- for the other 3 problematic transactions, sync run id 1004 is the issue, as it has partial completion status and took much longer than the rest, so furhter investigation on rca is required. 

-- What would you do next?
-- i would investigate specifically 1004 to find what hapenned in this sync run, specific logs from tihs sync run could be useful. i would also quarantine these 3 problematic trxs too, or the entire trxs from this sync run, 
-- before we can reconcile all the transactions from sync run 1004. there oculd be other problematic transactions that remain invisible for now.
-- for b-041, i would not mark this as missing yet, because it is the last trx received, so i would compare it to the baseline of howl ong it normally takes us to internally process partner trxs, and if it still isn't as long
-- as this baseline, then i would wait until it is longer before marking it as missing and doing investigating it more.
