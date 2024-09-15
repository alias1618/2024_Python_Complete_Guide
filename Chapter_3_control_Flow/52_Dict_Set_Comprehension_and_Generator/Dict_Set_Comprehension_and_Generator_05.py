x = [1, 2, 3, 4]

x_squared_generator = (item ** 2 for item in x)

# print(x_squared_generator)

for i in x_squared_generator:
    print(i)
