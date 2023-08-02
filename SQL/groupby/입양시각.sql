SELECT HOUR(datetime) as hour, count(datetime) as count
from ANIMAL_OUTS 
group by HOUR(datetime)
having hour >= 9 and hour <= 20
order by hour;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59412