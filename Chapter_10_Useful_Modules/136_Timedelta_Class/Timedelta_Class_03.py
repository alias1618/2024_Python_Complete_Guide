import datetime

now = datetime.datetime.now()
# Print the current date and time
oneday = datetime.datetime(2020, 1, 1)

print(now == oneday)  # False
print(now != oneday)  # True   
print(now < oneday)  # False
print(now > oneday)  # True
print(now <= oneday)  # False
print(now >= oneday)  # True
