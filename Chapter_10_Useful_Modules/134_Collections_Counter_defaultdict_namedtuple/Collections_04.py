from collections import defaultdict

#factory functrion

def default_factory():
    return "This is not defined"
# Create a defaultdict with the default factory function

d = defaultdict(default_factory)
# Accessing a key that does not exist will return the default value  

d["a"] = 1
d["b"] = 2

print(d["a"], d["b"], d["c"])  # Output: 1 2 This is not defined
# Accessing a key that does not exist will return the default value