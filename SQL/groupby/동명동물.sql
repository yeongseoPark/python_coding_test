-- 코드를 입력하세요
SELECT name, count(name)
from ANIMAL_INS 
group by name
having count(name) > 1
order by name;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59041