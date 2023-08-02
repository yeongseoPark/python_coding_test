-- https://school.programmers.co.kr/learn/courses/30/lessons/133026

SELECT b.ingredient_type , sum(a.total_order) as total_order
from FIRST_HALF a, ICECREAM_INFO b
where a.flavor = b.flavor
group by b.ingredient_type 
order by sum(a.total_order);
