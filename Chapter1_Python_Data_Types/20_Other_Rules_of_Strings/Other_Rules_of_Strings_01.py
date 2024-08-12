#Python 字串內不可改變，但是可以小技巧換掉字串
name = "Sam Donaldson"
name = "P" + name[1:]
print(name)