# get_user_id(id) return a tuple (name, age)

# 普通的方式
# info = get_user_id(id)
# print("The user name is " + info[0])
# print("The user age is " + info[1])

# Pythonic
name, age = get_user_id(id)
print("The user name is " + name)
print("The user age is " + age)