import datetime

now = datetime.datetime.now()
# Print the current date and time
gap = datetime.timedelta(1)
tomorrow = now + gap
print(tomorrow)
