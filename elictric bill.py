# Take inut of units consuned from user
units = int(input("Please enter Number of units you Consumed : "))
# Check condition of units consumed
# Then calculate the bill amount
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.0)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.0) + ((units - 200) * 2.5)
else:
    bill = (100 * 1.5) + (100 * 2.0) + (100 * 2.5) + ((units - 300) * 3.0)
# Display the bill
print(f"Your total electricity bill is: ${bill:.2f}")
# This code calculates the electricity bill based on the number of units consumed.
# The rates are as follows:
# - For the first 100 units: $1.50 per unit
# - For the next 100 units (101-200): $2.00 per unit
# - For the next 100 units (201-300): $2.50 per unit
# - For any units above 300: $3.00 per unit
# The bill is calculated based on these rates and displayed to the user.
# The code takes the number of units consumed as input from the user and calculates the total bill based on the defined rates.
# The bill is then printed with two decimal places for clarity.
# This code calculates the electricity bill based on the number of units consumed.
# The rates are as follows:
# - For the first 100 units: $1.50 per unit
