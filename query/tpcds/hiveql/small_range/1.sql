select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 1      and 11
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 21     and 31
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 41     and 51
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 61     and 71
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 81     and 91
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 1      and 11
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 21     and 31
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 41     and 51
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 61     and 71
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 81     and 91
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 1      and 11
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 21     and 31
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 41     and 51
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 61     and 71
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 81     and 91
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 1      and 11
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 21     and 31
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 41     and 51
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 61     and 71
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 81     and 91
select avg(ss_net_paid)         from store_sales where ss_quantity       between 1      and 11
select avg(ss_net_paid)         from store_sales where ss_quantity       between 21     and 31
select avg(ss_net_paid)         from store_sales where ss_quantity       between 41     and 51
select avg(ss_net_paid)         from store_sales where ss_quantity       between 61     and 71
select avg(ss_net_paid)         from store_sales where ss_quantity       between 81     and 91
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 1      and 11
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 21     and 31
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 41     and 51
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 61     and 71
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 81     and 91
select avg(ss_net_profit)       from store_sales where ss_quantity       between 1      and 11
select avg(ss_net_profit)       from store_sales where ss_quantity       between 21     and 31
select avg(ss_net_profit)       from store_sales where ss_quantity       between 41     and 51
select avg(ss_net_profit)       from store_sales where ss_quantity       between 61     and 71
select avg(ss_net_profit)       from store_sales where ss_quantity       between 81     and 91
select avg(ss_list_price)       from store_sales where ss_quantity       between 0      and 10
select avg(ss_list_price)       from store_sales where ss_quantity       between 6      and 16
select avg(ss_list_price)       from store_sales where ss_quantity       between 11     and 21
select avg(ss_list_price)       from store_sales where ss_quantity       between 16     and 26
select avg(ss_list_price)       from store_sales where ss_quantity       between 21     and 31
select avg(ss_list_price)       from store_sales where ss_quantity       between 26     and 36
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 110
select avg(ss_list_price)       from store_sales where ss_list_price     between 70     and 90 
select avg(ss_list_price)       from store_sales where ss_list_price     between 80     and 100
select avg(ss_list_price)       from store_sales where ss_list_price     between 100    and 120
select avg(ss_list_price)       from store_sales where ss_list_price     between 110    and 130
select avg(ss_list_price)       from store_sales where ss_list_price     between 120    and 140
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 7000   and 8800  
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 8000   and 9800  
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 10800
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 10000  and 11800
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 11000  and 12800
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 12000  and 13800
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 10     and 20 
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 20     and 30 
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 30     and 40
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 50
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 50     and 60
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 60     and 70
select avg(ws_quantity)         from web_sales where ws_sales_price    between 100.00 and 130
select avg(ws_quantity)         from web_sales where ws_sales_price    between  50.00 and 80
select avg(ws_quantity)         from web_sales where ws_sales_price    between 150.00 and 180
select count(*) 			    from store_sales where ss_quantity 	     between 1    and 11
select count(*) 			    from store_sales where ss_quantity 	     between 21   and 31
select count(*) 			    from store_sales where ss_quantity 	     between 41   and 51
select count(*) 			    from store_sales where ss_quantity 	     between 61   and 71
select count(*) 			    from store_sales where ss_quantity 	     between 81   and 91
select count(ss_list_price)     from store_sales where ss_quantity 	     between 0    and 10
select count(ss_list_price)     from store_sales where ss_quantity 	     between 6    and 16
select count(ss_list_price)     from store_sales where ss_quantity 	     between 11   and 21
select count(ss_list_price)     from store_sales where ss_quantity 	     between 16   and 26
select count(ss_list_price)     from store_sales where ss_quantity 	     between 21   and 31
select count(ss_list_price)     from store_sales where ss_quantity 	     between 26   and 36
select count(ss_list_price)     from store_sales where ss_list_price     between 90   and 110
select count(ss_list_price)     from store_sales where ss_list_price     between 70   and 90 
select count(ss_list_price)     from store_sales where ss_list_price     between 80   and 100
select count(ss_list_price)     from store_sales where ss_list_price     between 100  and 120
select count(ss_list_price)     from store_sales where ss_list_price     between 110  and 130
select count(ss_list_price)     from store_sales where ss_list_price     between 120  and 150
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 7000   and 8800 
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 8000   and 9800 
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 9000   and 10800
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 10000  and 11800
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 11000  and 12800
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 12000  and 13800
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 10     and 20 
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 20     and 30 
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 30     and 40
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 40     and 50
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 50     and 60
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 60     and 70
select sum (ss_quantity)        from store_sales where ss_sales_price    between 50.00  and 70
select sum (ss_quantity)        from store_sales where ss_sales_price    between 100.00 and 120
select sum (ss_quantity)        from store_sales where ss_sales_price    between 150.00 and 170
select sum (ss_quantity)        from store_sales where ss_net_profit     between 0      and 2000
select sum (ss_quantity)        from store_sales where ss_net_profit     between 150    and 2015
select sum (ss_quantity)        from store_sales where ss_net_profit     between 50     and 2050