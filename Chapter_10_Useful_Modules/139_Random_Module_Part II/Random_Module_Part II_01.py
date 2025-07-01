import random

random.seed(10)  # Set a seed for reproducibility

for i in range(5):
    # Generate a random integer between 1 and 1000
    random_integer = random.randint(1, 1000)
    print(f"Random Integer {i + 1}: {random_integer}")