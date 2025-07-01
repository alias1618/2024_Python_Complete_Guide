import math

print(math.isnan(56))  # False
print(math.isnan(math.inf))  # True
print(math.isnan(float('nan')))  # True

print(math.isinf(56))  # False
print(math.isinf(math.inf))  # True
print(math.isinf(float('nan')))  # False
