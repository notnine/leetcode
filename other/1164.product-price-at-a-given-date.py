# Write your MySQL query statement below
with latest_dates as (
    select product_id, max(change_date) as latest_date from Products
    where change_date <= '2019-08-16'
    group by product_id
),
ids as(
    select distinct product_id
    from Products
)
select ids.product_id, (case when p.new_price is null then 10 else p.new_price end) as price
from ids
left join latest_dates ld
on ids.product_id = ld.product_id
left join products p
on p.change_date = ld.latest_date and p.product_id = ids.product_id