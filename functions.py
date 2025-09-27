person = {"name": "Alice", "age": 30}

# def greet(name, age, /): #<--all parameters should only accept positional arguments
#     print(f"Hello {name}, you are {age} years old.")

# def greet(name, /,age): #<-- name only accepts positional arguments the rest accepts both
#     print(f"Hello {name}, you are {age} years old.")

# def greet(name, *, age): #<-- age only accepts keyword argument name can be any
#     print(f"Hello {name}, you are {age} years old.")

# def greet(*,name, age): #<--- all parameters should only accept keyword arguments
#     print(f"Hello {name}, you are {age} years old.")

# def greet(name, /, *, age):   #<-- name positional only and age keyword only
#     print(f"Hello {name}, you are {age} years old.")


# greet("john",31)
# greet(age=31, name="Julie")
# greet("john", age=31)
# greet(name="john", 31)

# greet(**person)

# -> str is not type check its just a hint to notify user of function that it should return type str
# def ageFunc(age) -> str:
#    return age
# print(ageFunc(person["age"]))


# to enforce type checking
# def ageFunc(age) -> str:
#     if not isinstance(age, str):
#         raise TypeError("Expected a string")
#     return age

# print(ageFunc(person["age"]))
