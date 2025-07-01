import random

fruits = ["apple", "banana", "cherry"]
result = random.choices(fruits, weights=[1, 1, 2], k=10)
print("Randomly chosen fruits with weights:", result)