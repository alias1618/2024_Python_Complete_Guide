from collections import defaultdict

#factory functrion

Harry = defaultdict(lambda: "Wrong key")
# Create a defaultdict with the default factory function

Harry["name"] = "Harry Potter"
# Accessing a key that does not exist will return the default value
Harry["age"] = 15
print(Harry["schooled"])  # Output: Wrong key