import random

my_tuple = (3, 4, 1, 2, 5, 8, 7, 6)

my_list = random.sample(my_tuple, k=len(my_tuple))
print("Original tuple:", my_tuple)