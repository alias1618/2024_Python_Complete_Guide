# Structural Pattern Matching
# switch statement ==
# or

day = input("今天星期幾")


match day:
    case "星期日" | "星期一":
        print("今日公休")
    case "星期六":
        print("今日營業半日!")
    case _:
        print("今日正常營業")