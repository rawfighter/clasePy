name ="Ronald"
name2 = "Angie"
for i in name:
    print(i)

for e  in name2:
    print((e))
#declaring a list
list = ["characters", 1, True]
for i in list:
    print(i)

#empty
print("Empty List Handling")

list2= []
print(len(list2))
list2.append("firstItem")
list2.append("secondItem")
print(len(list2))
#get Specific item from the list
print(list2[0])
print(list2[1])

list2.remove("firstItem")
print(len(list2))