select user_id as "buyer_id",u.join_date, 
case when orders_in_2019 is null then 0 
else orders_in_2019 end as "orders_in_2019" 
from  Users u left join(select buyer_id,count(order_id)as "orders_in_2019" from Orders o 
where order_date like '2019%' 
group by buyer_id)as t2 
on user_id=t2.buyer_id;