# Write your MySQL query statement below

# get time taken for each machine's process

with durations as (
    select a1.machine_id, a1.process_id, a2.timestamp - a1.timestamp as duration
    from Activity a1
    inner join Activity a2
    on a1.machine_id = a2.machine_id and a1.process_id = a2.process_id and a1.activity_type = 'start' and a2.activity_type = 'end'
)
select machine_id, round(sum(duration) / count(machine_id), 3) as processing_time
from durations
group by machine_id