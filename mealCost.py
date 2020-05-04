''''
hacker-rank-problem : calculate total meal cost after adding tip and tax..
N.B:..have to print the result with standard format with rounded integer
'''

#taking input of MealCost as meal,TipPercent as tipp and TaxPercent as taxp
meal_cost = float(input("Enter the cost amount:"))
tipp = int(input("Enter tip percent:"))
taxp = int(input("Enter tax percent:"))

#calculating the tip and tax after percentage
tip = meal_cost*(tipp/100)
tax = meal_cost*(taxp/100)

#calculating total meal cost after adding tip and tax
#then rounded the result using round() function
TotalCost = round(meal_cost+tip+tax)

#printing the result with standard print() function. 
print('The total meal cost is {} dollars.'.format(TotalCost))
