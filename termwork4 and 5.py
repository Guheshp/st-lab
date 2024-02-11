#initialize the lock stock barrel price
lock_price = 40
stock_price = 30
barrel_price = 25

#initialize the products limit
lock_limit = 70
stock_limit = 80
barrel_limit = 90

#initialize the commission levels
commission_level_1 = 0.10
commisiion_level_2 = 0.15
commisiion_level_3 = 0.20

#colloect the sales person input 
lock_sold =  (int(input("Enter the number of locksold : ")))
stock_sold =  (int(input("Enter the number of stock_sold : ")))
barrel_sold =  (int(input("Enter the number of barrel_sold : ")))

#calculate the totalsale
total_sale = (lock_sold * lock_price) + (stock_sold+stock_price) + (barrel_sold+barrel_price)

print("Total sale for the salesperson is $", str(total_sale))

#calculate the cooissions 

if total_sale <= 1000:
    commission = total_sale * commission_level_1

elif total_sale <= 1800:
    commission = (1000 * commission_level_1) + ((total_sale - 1000) * commisiion_level_2) 
else:
    commission = (1000 * commission_level_1) + (800 * commisiion_level_2) + ((total_sale - 1800)*commisiion_level_3)

print("tota commision for salesperson $", str(commission))

