select stu.student_id, stu.student_name, sub.subject_name, count(exa.student_id) as attended_exams
from Students stu
join Subjects sub
left join Examinations exa
    on stu.student_id = exa.student_id and sub.subject_name = exa.subject_name
group by stu.student_id, stu.student_name, sub.subject_name
order by stu.student_id, sub.subject_name asc
