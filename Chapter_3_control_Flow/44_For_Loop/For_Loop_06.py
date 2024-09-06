# for variable in iterable"
#     do something here


for a, b in [(1, 2), (3, 5), (5, 7)]:
    print(a + b)


#兩個寫法都是一樣答案，這種寫法比較不容易懂
for tuple in [(1, 2), (3, 5), (5, 7)]:
    print(tuple[0] + tuple[1])