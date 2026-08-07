# Write your MySQL query statement below
with popular_managers as (
    select managerId
    from Employee
    group by managerId
    having count(managerId) >= 5
)
select name
from Employee
join popular_managers
on Employee.id = popular_managers.managerId