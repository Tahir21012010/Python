try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex:
    print("exception:", ex)
print("Please enter a valid number.")