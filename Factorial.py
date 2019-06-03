#Recursion

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
            return number * factorial(number - 1)
print(factorial(4))
print(factorial(0))
print(factorial(10))
print(factorial(100))