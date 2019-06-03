def namenumber(name, number):
    count = 0
    while count < number:
        print(name)
        count+=1

print("Enter a name")
name = input()
print("Enter a number")
number = int(input())
namenumber(name, number)
