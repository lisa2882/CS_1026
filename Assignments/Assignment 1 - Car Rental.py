
import math

# Declaring Input Variables - Part 1.
custName = input("Please type in the customer's first and last name: ")
custAge = int(input("Please type in the customer's age: "))
custClassification = str(input("Please type in the customer's classification code: ").upper())
daysOfRental = int(input("Please type in the number of days the vehicle was rented: "))
weeksOfRental = math.ceil(daysOfRental / 7)
initialKilometers = int(input("Please type in the number of kilometres on the vehicle before it was rented: "))
newKilometers = int(input("Please type in the number of kilometres on the vehicle after it was rented: "))
changeKilometers = newKilometers - initialKilometers

# Printing the input values - Part 1.
print("Customer's name:", custName)
print("Customer's age:", custAge)
print("Customer's classification code:", custClassification)
print("Vehicle was rented for", daysOfRental, "days")
print("Vehicle's odometer reading at the start of the rental period:", initialKilometers, "km")
print("Vehicle's odometer reading at the end of the rental period:", newKilometers, "km")
print("---------------------------------------------------------")

# Declaring Pricing Variables - Note all figures are in dollars
totalCost = 0
budgetPerDayRate = 20
budgetKilometerRate = 0.30
dailyPerDayRate = 50
dailyKilometerLimit = 100
dailyKilometerOverageCharge = 0.3
weeklyPerWeekRate = 200
weeklyKilometerLimitLow = 1000
weeklyOverageChargeLow = 50
weeklyKilometerLimitHigh = 2000
weeklyOverageChargeHigh = 100
weeklyKilometerOverageChargeHigh = 0.30
costOfYouth = 10

# Classification codes and costing
if custClassification == "B":  # Budget
        totalCost += daysOfRental * budgetPerDayRate
        totalCost += budgetKilometerRate * changeKilometers
if custClassification == "D":  # Daily
        totalCost += dailyPerDayRate * daysOfRental
if changeKilometers / daysOfRental > dailyKilometerLimit:
            totalCost += (changeKilometers - dailyKilometerLimit * daysOfRental) * dailyKilometerOverageCharge
if custClassification == "W":  # Weekly
    totalCost += weeksOfRental * weeklyPerWeekRate
    if (changeKilometers / weeksOfRental > weeklyKilometerLimitLow
        & changeKilometers / weeksOfRental < weeklyKilometerLimitHigh):
        totalCost += weeklyOverageChargeLow * weeksOfRental
        if changeKilometers / weeksOfRental > weeklyKilometerLimitHigh:
            totalCost += weeklyOverageChargeHigh * weeksOfRental
            totalCost += weeklyKilometerOverageChargeHigh * (changeKilometers - weeklyKilometerLimitHigh)
# Cost Of Youth (age<25)
if custAge < 25:
    totalCost += costOfYouth * daysOfRental

# Billing Statement
if (not custClassification == "B" and not custClassification == "D"
    and not custClassification == "W"):
        print(custClassification, " is not a valid classification code. \n"
                                  "Please input valid classification code and run program again\n"
                                  "to receive price of rental.")
        print("Customer's name:", custName)
        print("Customer's age:", custAge)
else:
    print("Customer's name:", custName)
    print("Customer's age:", custAge)
    print("Customer's classification code:", custClassification)
    print("Vehicle was rented for", daysOfRental, "days")
    print("Vehicle's odometer reading at the start of the rental period", initialKilometers, "km")
    print("Vehicle's odometer reading at the end of the rental period", newKilometers, "km")
    print("Vehicle was driven", changeKilometers, "km during rental period")
    print("The total cost of renting the car is %.2f" % totalCost)
