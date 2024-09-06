# < 8 => free
# >= 8 and <65 => 300
# >= 65 => half
age = 5

if age < 8:
    print("Movie is free for you!!")
elif 8 <= age < 65:
    print("You need to pay $300!")
else:
    print("You only need to pay $150!")