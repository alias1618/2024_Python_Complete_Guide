# 1. normal argument (p1, p2)
# 2. default argument
# 3. *args
# 4. **kwargs
def func(p1, p2, p3="there", *args, **kwargs):
    print("---------------------------")
    print(p1, p2, p3, args, kwargs)

func(1, 2, 3, 4, 5, x=1, y=3)
func(1, 2, 3, 4, x=4)
func(1, 2, 3, 4)
func(1, 2, 3)
func(1, 2)