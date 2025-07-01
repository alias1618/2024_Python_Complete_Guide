import datetime

now = datetime.datetime.now()
# Print the current date and time
oneday = datetime.datetime(2020, 1, 1)
diff = now - oneday
print(diff)
# Print the difference in days
print(diff.days)  # 1360    
# Print the difference in seconds
print(diff.seconds)  # 0    
# Print the difference in microseconds
print(diff.microseconds)  # 0
