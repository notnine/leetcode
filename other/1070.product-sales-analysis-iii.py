# Write your MySQL query statement below
with first_years as (
    select product_id, min(year) as first_year
    from Sales
    group by product_id
)
select fy.product_id, fy.first_year, s.quantity, s.price
from Sales s
join first_years fy
on s.product_id = fy.product_id and s.year = fy.first_year