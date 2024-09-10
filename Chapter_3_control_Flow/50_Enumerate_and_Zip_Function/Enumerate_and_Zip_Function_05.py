x = [1, 2]
y = ['A', 'B', 'C']
z = ['a', 'b', 'c', 'd']
#   z 的 值中的d 會被捨去，根據最短的資料來決定zip資料長度

for tuple in zip(x, y):
    print(tuple)