stocks = int(2000)
price_per = int(40)

total_price = stocks * price_per
print ('Amount paid for the stock: $',total_price)

percent = float(.03)
commission = total_price * percent
print ('Commission paid on the purchase: $',commission)

sell_per = float(42.75)

sell_total = stocks * sell_per
print ('Amount the stock sold for: $',sell_total)

sell_com = sell_total * percent
print ('Commission paid on the sale: $',sell_com)

dif = sell_total - (total_price + commission + sell_com)
print ('Profit (or loss if negative): $',dif)
