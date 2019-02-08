select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 1      and 2
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 21     and 22
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 41     and 42
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 61     and 62
select avg(ss_ext_discount_amt) from store_sales where ss_quantity       between 81     and 82
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 1      and 2
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 21     and 22
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 41     and 42
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 61     and 62
select avg(ss_ext_sales_price)  from store_sales where ss_quantity       between 81     and 82
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 1      and 2
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 21     and 22
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 41     and 42
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 61     and 62
select avg(ss_ext_list_price)   from store_sales where ss_quantity       between 81     and 82
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 1      and 2
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 21     and 22
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 41     and 42
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 61     and 62
select avg(ss_ext_tax)          from store_sales where ss_quantity       between 81     and 82
select avg(ss_net_paid)         from store_sales where ss_quantity       between 1      and 2
select avg(ss_net_paid)         from store_sales where ss_quantity       between 21     and 22
select avg(ss_net_paid)         from store_sales where ss_quantity       between 41     and 42
select avg(ss_net_paid)         from store_sales where ss_quantity       between 61     and 62
select avg(ss_net_paid)         from store_sales where ss_quantity       between 81     and 82
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 1      and 2
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 21     and 22
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 41     and 42
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 61     and 62
select avg(ss_net_paid_inc_tax) from store_sales where ss_quantity       between 81     and 82
select avg(ss_net_profit)       from store_sales where ss_quantity       between 1      and 2
select avg(ss_net_profit)       from store_sales where ss_quantity       between 21     and 22
select avg(ss_net_profit)       from store_sales where ss_quantity       between 41     and 42
select avg(ss_net_profit)       from store_sales where ss_quantity       between 61     and 62
select avg(ss_net_profit)       from store_sales where ss_quantity       between 81     and 82
select avg(ss_list_price)       from store_sales where ss_quantity       between 0      and 1
select avg(ss_list_price)       from store_sales where ss_quantity       between 6      and 7
select avg(ss_list_price)       from store_sales where ss_quantity       between 11     and 12
select avg(ss_list_price)       from store_sales where ss_quantity       between 16     and 17
select avg(ss_list_price)       from store_sales where ss_quantity       between 21     and 22
select avg(ss_list_price)       from store_sales where ss_quantity       between 26     and 27
select avg(ss_list_price)       from store_sales where ss_list_price     between 90     and 92
select avg(ss_list_price)       from store_sales where ss_list_price     between 70     and 72 
select avg(ss_list_price)       from store_sales where ss_list_price     between 80     and 82
select avg(ss_list_price)       from store_sales where ss_list_price     between 100    and 102
select avg(ss_list_price)       from store_sales where ss_list_price     between 110    and 112
select avg(ss_list_price)       from store_sales where ss_list_price     between 120    and 122
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 7000   and 7180  
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 8000   and 8180  
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 9000   and 9180
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 10000  and 10180
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 11000  and 11180
select avg(ss_list_price)       from store_sales where ss_coupon_amt     between 12000  and 12180
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 10     and 11 
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 20     and 21 
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 30     and 31
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 40     and 41
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 50     and 51
select avg(ss_list_price)       from store_sales where ss_wholesale_cost between 60     and 61
select avg(ws_quantity)         from web_sales where ws_sales_price    between 100.00 and 103
select avg(ws_quantity)         from web_sales where ws_sales_price    between  50.00 and 53
select avg(ws_quantity)         from web_sales where ws_sales_price    between 150.00 and 153
select count(*) 			    from store_sales where ss_quantity 	     between 1    and 2
select count(*) 			    from store_sales where ss_quantity 	     between 21   and 22
select count(*) 			    from store_sales where ss_quantity 	     between 41   and 42
select count(*) 			    from store_sales where ss_quantity 	     between 61   and 62
select count(*) 			    from store_sales where ss_quantity 	     between 81   and 82
select count(ss_list_price)     from store_sales where ss_quantity 	     between 0    and 1
select count(ss_list_price)     from store_sales where ss_quantity 	     between 6    and 7
select count(ss_list_price)     from store_sales where ss_quantity 	     between 11   and 12
select count(ss_list_price)     from store_sales where ss_quantity 	     between 16   and 17
select count(ss_list_price)     from store_sales where ss_quantity 	     between 21   and 22
select count(ss_list_price)     from store_sales where ss_quantity 	     between 26   and 27
select count(ss_list_price)     from store_sales where ss_list_price     between 90   and 92
select count(ss_list_price)     from store_sales where ss_list_price     between 70   and 72 
select count(ss_list_price)     from store_sales where ss_list_price     between 80   and 82
select count(ss_list_price)     from store_sales where ss_list_price     between 100  and 102
select count(ss_list_price)     from store_sales where ss_list_price     between 110  and 112
select count(ss_list_price)     from store_sales where ss_list_price     between 120  and 122
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 7000   and 7180  
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 8000   and 8180  
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 9000   and 9180
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 10000  and 10180
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 11000  and 11180
select count(ss_list_price)     from store_sales where ss_coupon_amt     between 12000  and 12180
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 10     and 11 
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 20     and 21 
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 30     and 31
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 40     and 41
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 50     and 51
select count(ss_list_price)     from store_sales where ss_wholesale_cost between 60     and 61
select sum (ss_quantity)        from store_sales where ss_sales_price    between 50.00  and 52
select sum (ss_quantity)        from store_sales where ss_sales_price    between 100.00 and 102
select sum (ss_quantity)        from store_sales where ss_sales_price    between 150.00 and 152
select sum (ss_quantity)        from store_sales where ss_net_profit     between 0      and 200
select sum (ss_quantity)        from store_sales where ss_net_profit     between 150    and 350
select sum (ss_quantity)        from store_sales where ss_net_profit     between 50     and 250