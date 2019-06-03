#!Git Edit
fruitsByColor = {"red": "apple", "blue": "berry"}
#!retrieve the values
name=""
print(fruitsByColor["blue"])
while(name != "-done"):
    print("Enter student name to get theirs hobbies")
    name= input()
    hobbiesByPerson={"Aaron":["photography","Speluking"], "Sarah":["climbing", "Speluking"]}
    if (name != "-done"):
         hobbies = hobbiesByPerson[name]
    for h in hobbies:
        print(h)
print("Acabamos")   
