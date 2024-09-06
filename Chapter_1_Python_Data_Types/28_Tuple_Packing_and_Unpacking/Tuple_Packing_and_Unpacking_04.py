x = 25
y = 35

#---------- 正常數值交換的流程
temp = x # temp = 25
x = y # x = 35
y = temp # 25

print(x)
print(y)
#--------- 使用tuple 的流程

x = 25
y = 35

x, y = y, x
print(x)
print(y)