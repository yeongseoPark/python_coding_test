-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(*) as count
from ANIMAL_INS 
where ANIMAL_TYPE in ("cat", "dog")
group by ANIMAL_TYPE
order by ANIMAL_TYPE;

-- https://school.programmers.co.kr/learn/courses/30/lessons/59040