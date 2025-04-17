# 不要執行這個程式會有stackoverflow
def hello():
    print("hello")
    hello()

hello()