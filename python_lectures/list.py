fruits = ["apple", "banana", "cherry"]
print(fruits) # view all list
print(fruits[0]) # access by index


apple, banana , cherry = fruits # this is called unpacking a list
print(apple)
print(banana)
print(cherry)

pineapple = fruits.append("pineapple") # force another value inside list
print(fruits) # view new all list

# loop a list
# for fruit in fruits:
#     print(fruit)


# example of unpacking a list contains mutiple tuples
# fruit_pairs = [("apple", 1), ("banana", 2), ("cherry", 3)]

# for name, number in fruit_pairs:
#     print(f"{name} → {number}")
