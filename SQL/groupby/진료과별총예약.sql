SELECT MCDP_CD as "진료과 코드", count(apnt_no) as "5월예약건수"
from APPOINTMENT 
where APNT_YMD like '2022-05%'
group by MCDP_CD
order by count(apnt_no), MCDP_CD;

-- https://school.programmers.co.kr/learn/courses/30/lessons/132202