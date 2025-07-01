import datetime
# Get the current date and time

x = datetime.datetime.now()
# Print the type of the current date and time
print(type(x))  # <class 'datetime.datetime'>
# Print the current date and time
print(x)  # 2023-10-01 12:34:56.789012
# Print the year, month, and day
print(x.year)  # 2023
print(x.month)  # 10

print(x.day)  # 1
# Print the hour, minute, second, and microsecond   
print(x.hour)  # 12
print(x.minute)  # 34
print(x.second)  # 56
print(x.microsecond)  # 789012