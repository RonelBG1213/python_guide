person = {"name": "Alice", "age": 30}

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(**person)

# -> str is not type check its just a hint to notify user of function that it should return type str
def ageFunc(age) -> str:
   return age
print(ageFunc(person["age"]))


# to enforce type checking
# def ageFunc(age) -> str:
#     if not isinstance(age, str):
#         raise TypeError("Expected a string")
#     return age

print(ageFunc(person["age"]))
