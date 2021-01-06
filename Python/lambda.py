people=[
    {"name":"Harry","houses":"Gryffindor"},
    {"name": "Cho", "houses": "Ravenclaw"},
    {"name": "Draco", "houses": "Slytherin"}
]

#def f(person):
 #   return person["houses"]

people.sort(key=lambda person: person["name"])

print(people)    