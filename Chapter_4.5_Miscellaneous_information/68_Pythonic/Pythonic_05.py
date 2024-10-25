cmd = input("Give a command: ")

# 普通寫法的方式
# if cmd == "cd" or cmd =="dir" or cmd == "echo":
#     print("valid command")
# else:
#     print("invalid command") 

# Pythonic的方式
if cmd in ('dir', 'cd', 'echo'):
    print("valid command")
else:
    print("invalid command") 
