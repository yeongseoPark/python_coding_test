select 
a.product_code as product_code,
sum(a.price * b.sales_amount) as sales
from product a
    join offline_sale b
    on a.product_id = b.product_id
group by a.product_code
order by sales DESC, product_code;