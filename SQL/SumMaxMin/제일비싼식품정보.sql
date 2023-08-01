-- https://school.programmers.co.kr/learn/courses/30/lessons/131115
SELECT * from food_product where price = (select max(price) from food_product);