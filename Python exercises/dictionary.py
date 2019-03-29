thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

#OR

another_dict = {
'brand': "BMW",
"model": "M60",
"year" : 2011
}
print(another_dict)

#Accessing items from a dictionary
x = thisdict["brand"]
print(x) #prints ford
#or
y=another_dict.get("model")
print(y) #prints M60

# To change value of an item in the dictionary
another_dict["year"] = 2018 #changes 2011 to 2018

# Looping inside a dictionary and printing values of the keys
for x in thisdict:
  print(thisdict[x])# prints values of the keys Ford mustang 1964
#or
for y in another_dict.values():
    print(y)

#or Loop through both keys and values, by using the items() function
for x, y in thisdict.items():
    print(x,y) # prints: brand Ford
               # model Mustang
               # year 1964

# doing calculations inside a dictionary. Assume we have a dictionary with lottery players names and loto-numbers
lottery_players = [
    {
        "name" : "John",
        "number" : (12, 23, 45, 15, 10)
    },
    {
        "name" : "Beni",
        "number" : (10, 25, 50, 16, 12)
    }
]

s = sum(lottery_players[0]["number"])
print(s)
