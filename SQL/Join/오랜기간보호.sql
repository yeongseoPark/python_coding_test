select ins.name as name, ins.datetime as datetime
from animal_ins ins
    left join animal_outs outs
    on ins.animal_id = outs.animal_id
where outs.animal_id is Null
order by datetime
LIMIT 3
;