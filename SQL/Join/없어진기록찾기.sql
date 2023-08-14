select b.animal_id as animal_id , b.name as name
from animal_outs b
    left outer join animal_ins a
    on a.animal_id = b.animal_id
where a.animal_id is null
order by animal_id
;