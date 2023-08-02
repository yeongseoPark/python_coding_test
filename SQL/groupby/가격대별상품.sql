-- 코드를 입력하세요
SELECT FLOOR(price / 10000) * 10000 as price_group, count(*) as products 
from product
group by floor(price / 10000)
order by price_group;

-- https://school.programmers.co.kr/learn/courses/30/lessons/131530

SELECT truncate(price, -4) as price_group, count(*) as products 
from product
group by price_group
order by price_group;

-- truncate()의 두번재 매개변수가 음수이면, 소수점 위의 숫자를 절삭
-- ex ) (123456 ,-2) 면, 123400