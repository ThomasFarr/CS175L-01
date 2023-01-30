#Thomas Farrell
#CS175L-01
#1/23/23

#declaring input variables
stocks = float(input('How many stocks would you like to buy?:'))
price_per = float(input('What is the buy price per stock?:'))
sell_per = float(input('What is the sell price per stock?:'))
buy_percent = float(input('What is the percent commission on buying?: '))
buy_percent /= 100
sell_percent = float(input('What is the percent comission on selling?:'))
sell_percent /= 100


#using declared variables to calculate print results
total_price = stocks * price_per
buy_commission = total_price * buy_percent
sell_total = stocks * sell_per
sell_com = sell_total * sell_percent
dif = sell_total - (total_price + buy_commission + sell_com)

#print statements
print ('Amount paid for the stock: $',total_price)
print ('Commission paid on the purchase: $',buy_commission)
print ('Amount the stock sold for: $',sell_total)
print ('Commission paid on the sale: $',sell_com)
print ('Profit (or loss if negative): $',dif)
