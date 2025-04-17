try:
    a = {1: 'hello', 2: 'how', 3: 'are', 4: 'you'}
    print(a[5])
except KeyError:
    print("We've got an error")