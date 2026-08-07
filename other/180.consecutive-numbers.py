# Write your MySQL query statement below
select distinct id1.num as ConsecutiveNums
from Logs id1
join Logs id2
    on id1.id + 1 = id2.id
join Logs id3
    on id1.id + 2 = id3.id
where id1.num = id2.num and id1.num = id3.num
