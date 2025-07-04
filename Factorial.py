def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial.__doc__)
print("the total of 0!:",factorial(0))
print("the total of 1!:",factorial(1))
print("the total of 2!:",factorial(2))
print("the total of 5!:",factorial(5))
print("the total of 10!:",factorial(10))