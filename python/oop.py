# object-oriented programming

# class Person:
#     def __init__(self):
#         self.name = "Doe"
#         self.age = 67
#         self.occupation = "police"
#
# person = Person()
# person.name = "Nicolette"
# print(person.name)
# print(person.age)
# print(person.occupation)

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = People("Job", 88)
person2 =People("Elijah",78)
print(f"my name is {person1.name}")