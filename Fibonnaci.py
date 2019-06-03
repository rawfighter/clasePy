def fibonnaci(number):
    if number==0 or number==1:
        return 1
    else:
        return fibonnaci(number-1)+fibonnaci(number-2)
print(fibonnaci(0))
print(fibonnaci(1))
print(fibonnaci(2))
print(fibonnaci(3))
print(fibonnaci(4))