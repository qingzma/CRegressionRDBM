select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 1      and 20
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 21     and 40
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 41     and 60
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 61     and 80
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 81     and 100
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 1      and 20
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 21     and 40
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 41     and 60
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 61     and 80
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 81     and 100
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 1      and 20
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 21     and 40
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 41     and 60
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 61     and 80
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 81     and 100
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 1      and 20
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 21     and 40
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 41     and 60
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 61     and 80
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 81     and 100
select avg(ss_net_paid)         from store_sales where ss_quantity       between 1      and 20
select avg(ss_net_paid)         from store_sales where ss_quantity       between 21     and 40
select avg(ss_net_paid)         from store_sales where ss_quantity       between 41     and 60
select avg(ss_net_paid)         from store_sales where ss_quantity       between 61     and 80
select avg(ss_net_paid)         from store_sales where ss_quantity       between 81     and 100
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 1      and 20
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 21     and 40
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 41     and 60
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 61     and 80
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 81     and 100
select avg(ss_net_profit)       from store_sales where ss_quantity       between 1      and 20
select avg(ss_net_profit)       from store_sales where ss_quantity       between 21     and 40
select avg(ss_net_profit)       from store_sales where ss_quantity       between 41     and 60
select avg(ss_net_profit)       from store_sales where ss_quantity       between 61     and 80
select avg(ss_net_profit)       from store_sales where ss_quantity       between 81     and 100
select avg(ss_list_price)       from store_sales where ss_quantity       between 0      and 5
select avg(ss_list_price)       from store_sales where ss_quantity       between 6      and 10
select avg(ss_list_price)       from store_sales where ss_quantity       between 11     and 15
select avg(ss_list_price)       from store_sales where ss_quantity       between 16     and 20
select avg(ss_list_price)       from store_sales where ss_quantity       between 21     and 25
select avg(ss_list_price)       from store_sales where ss_quantity       between 26     and 30
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 100 
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 100 
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 100
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 100
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 100
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 100
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10000 
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10000 
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10000
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10000
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10000
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10000
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 60 
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 60 
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 60
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 60
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 60
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 60
select avg(ws_quantity)         from web_sales   where ws_sales_price    between 100.00 and 150.00
select avg(ws_quantity)         from web_sales   where ws_sales_price    between  50.00 and 100.00
select avg(ws_quantity)         from web_sales   where ws_sales_price    between 150.00 and 200.00
select count(*) 			from store_sales where ss_quantity 	     between 1    and 20
select count(*) 			from store_sales where ss_quantity 	     between 21   and 40
select count(*) 			from store_sales where ss_quantity 	     between 41   and 60
select count(*) 			from store_sales where ss_quantity 	     between 61   and 80
select count(*) 			from store_sales where ss_quantity 	     between 81   and 100
select count(ss_list_price) from store_sales where ss_quantity 	     between 0    and 5
select count(ss_list_price) from store_sales where ss_quantity 	     between 6    and 10
select count(ss_list_price) from store_sales where ss_quantity 	     between 11   and 15
select count(ss_list_price) from store_sales where ss_quantity 	     between 16   and 20
select count(ss_list_price) from store_sales where ss_quantity 	     between 21   and 25
select count(ss_list_price) from store_sales where ss_quantity 	     between 26   and 30
select count(ss_list_price) from store_sales where ss_list_price     between 100  and 110
select count(ss_list_price) from store_sales where ss_list_price     between 100  and 110
select count(ss_list_price) from store_sales where ss_list_price     between 100  and 110
select count(ss_list_price) from store_sales where ss_list_price     between 100  and 110
select count(ss_list_price) from store_sales where ss_list_price     between 100  and 110
select count(ss_list_price) from store_sales where ss_list_price     between 100  and 110
select count(ss_list_price) from store_sales where ss_coupon_amt     between 9000 and 10000
select count(ss_list_price) from store_sales where ss_coupon_amt     between 9000 and 10000
select count(ss_list_price) from store_sales where ss_coupon_amt     between 9000 and 10000
select count(ss_list_price) from store_sales where ss_coupon_amt     between 9000 and 10000
select count(ss_list_price) from store_sales where ss_coupon_amt     between 9000 and 10000
select count(ss_list_price) from store_sales where ss_coupon_amt     between 9000 and 10000
select count(ss_list_price) from store_sales where ss_wholesale_cost between 40   and 60
select count(ss_list_price) from store_sales where ss_wholesale_cost between 40   and 60
select count(ss_list_price) from store_sales where ss_wholesale_cost between 40   and 60
select count(ss_list_price) from store_sales where ss_wholesale_cost between 40   and 60
select count(ss_list_price) from store_sales where ss_wholesale_cost between 40   and 60
select count(ss_list_price) from store_sales where ss_wholesale_cost between 40   and 60
select sum (ss_quantity) from store_sales where ss_sales_price between 50.00  and 100.00
select sum (ss_quantity) from store_sales where ss_sales_price between 100.00 and 150.00
select sum (ss_quantity) from store_sales where ss_sales_price between 150.00 and 200.00
select sum (ss_quantity) from store_sales where ss_net_profit  between 0      and 2000
select sum (ss_quantity) from store_sales where ss_net_profit  between 150    and 3000
select sum (ss_quantity) from store_sales where ss_net_profit  between 50     and 25000