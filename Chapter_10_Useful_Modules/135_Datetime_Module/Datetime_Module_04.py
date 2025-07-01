import datetime
# Get the current date and time

x = datetime.datetime.now()
# Print the type of the current date and time

print(x.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-10-01 12:34:56

print(x.strftime("%A-%B-%d-%Y"))  # Sunday-October-01-2023