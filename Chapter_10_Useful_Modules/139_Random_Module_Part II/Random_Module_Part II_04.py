import random

fruits = ["apple", "banana", "cherry"]

result = random.choices(fruits, k=4)
print("Randomly chosen fruits:", result)