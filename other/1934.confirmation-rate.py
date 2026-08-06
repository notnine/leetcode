# Write your MySQL query statement below
with counts as (
    select s.user_id, sum(case when action = 'confirmed' then 1 else 0 end) as confirm_count, count(*) as total_count
    from Signups s left join Confirmations c
        on s.user_id = c.user_id
    group by s.user_id
)

select s.user_id, round(coalesce(confirm_count / total_count), 2) as confirmation_rate
from Signups s left join counts
    on s.user_id = counts.user_id