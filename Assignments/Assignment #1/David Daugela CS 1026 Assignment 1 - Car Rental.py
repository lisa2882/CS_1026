
import math
# David Daugela - Student #: 250938255

# Declaring Input Variables - Part 1.
custName = str(input("Please type in the customer's first and last name: "))
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
BUDGET_PER_DAY_RATE = 20
BUDGET_KILOMETER_RATE = 0.30
DAILY_PER_DAY_RATE = 50
DAILY_KILOMETER_LIMIT = 100
DAILY_KILOMETER_OVERAGE_CHARGE = 0.3
WEEKLY_PER_WEEK_RATE = 200
WEEKLY_KILOMETER_LIMIT_LOW = 1000
WEEKLY_OVERAGE_CHARGE_LOW = 50
WEEKLY_KILOMETER_LIMIT_HIGH = 2000
WEEKLY_BASE_OVERAGE_CHARGE_HIGH = 100
WEEKLY_KILOMETER_OVERAGE_CHARGE_HIGH = 0.30
COST_OF_YOUTH = 10

# Classification codes and costing
if custClassification == "B":  # Budget
        totalCost += daysOfRental * BUDGET_PER_DAY_RATE
        totalCost += BUDGET_KILOMETER_RATE * changeKilometers
if custClassification == "D":  # Daily
        totalCost += DAILY_PER_DAY_RATE * daysOfRental
        if changeKilometers / daysOfRental > DAILY_KILOMETER_LIMIT:
            totalCost += (changeKilometers - DAILY_KILOMETER_LIMIT * daysOfRental) * DAILY_KILOMETER_OVERAGE_CHARGE
if custClassification == "W":  # Weekly
    totalCost += weeksOfRental * WEEKLY_PER_WEEK_RATE
    if (changeKilometers / weeksOfRental > WEEKLY_KILOMETER_LIMIT_LOW
    and changeKilometers / weeksOfRental < WEEKLY_KILOMETER_LIMIT_HIGH):
        totalCost += WEEKLY_OVERAGE_CHARGE_LOW * weeksOfRental
    elif changeKilometers / weeksOfRental > WEEKLY_KILOMETER_LIMIT_HIGH:
           totalCost += WEEKLY_BASE_OVERAGE_CHARGE_HIGH * weeksOfRental
           totalCost += WEEKLY_KILOMETER_OVERAGE_CHARGE_HIGH * (changeKilometers/weeksOfRental - WEEKLY_KILOMETER_LIMIT_HIGH)
# Cost Of Youth (age<25)
if custAge < 25:
    totalCost += COST_OF_YOUTH * daysOfRental

# Billing Statement
if (not custClassification == "B" and not custClassification == "D"
    and not custClassification == "W"):
        print(custClassification, " is not a valid classification code. \n"
                                  "Please input valid classification code and run program again\n"
                                  "to receive price of rental.")
        print("Customer's name:", custName)
        print("Customer's age:", custAge)
else:
    print("Billing Statement")
    print("Customer's name:", custName)
    print("Customer's age:", custAge)
    print("Customer's classification code:", custClassification)
    print("Vehicle was rented for", daysOfRental, "days")
    print("Vehicle's odometer reading at the start of the rental period", initialKilometers, "km")
    print("Vehicle's odometer reading at the end of the rental period", newKilometers, "km")
    print("Vehicle was driven", changeKilometers, "km during rental period")
    print("The total cost of renting the car is $%.2f" % totalCost)
