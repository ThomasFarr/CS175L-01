#CS175
#Thomas Farrell
#rainfall.py

total_rainfall = 0.0
monthly_rainfall = 0.0
average_rainfall = 0.0
y = 0
z = 0

years = int(input("How Many Years(Between 1 and 3): "))
months = int(input("How Many Months: "))

if years > 4 or years < 0:
    print ("Not between 1 and 3")
    years = int(input("How Many Years(Between 1 and 3): "))
else:
    while y < (years * 12):
        monthly_rainfall = float(input("average rainfall in month: "))
        total_rainfall += monthly_rainfall
        print (total_rainfall)
        y += 1   
    while z < months:
        monthly_rainfall = float(input("average rainfall in month: "))
        total_rainfall += monthly_rainfall
        print (total_rainfall)
        z += 1

total_months = (years * 12) + months
print (total_months, "months in total")
average_rainfall = total_rainfall / total_months
print ("Total Rainfall: ", total_rainfall, "inches" )
print ((f"Average Rainfall: {average_rainfall:.2f} inches in average per month"))




'''
    for months in range (years):
        for monthly_rainfall in range (years * 12):
            monthly_rainfall = float(input("average rainfall in month: "))
            total_rainfall += monthly_rainfall
            print (total_rainfall)


            
        for monthly_rainfall in range (months):
            monthly_rainfall = float(input("average rainfall in month: "))
            total_rainfall += monthly_rainfall
print ("Total Rainfall: ", total_rainfall )
print ((f"Average Rainfall: {average_rainfall:.2f}"))
'''        
        
        
        
        

#Declare variables to hold the total rainfall,
# monthly rainfall, average rainfall (all float), the number
# of years, and the total number of months.
# Get (input) number of years (validate input must be 1 to 3)
# Get (input) rainfall by month (nested for loops: year then 
#month)
# Calculate and print the total rainfall and the average 
#rainfall

