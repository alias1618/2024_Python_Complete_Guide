# Structural Pattern Matching
# switch statement ==

lang = input("你希望學什麼程式語言?")

# if lang == "JavaScript":
#     print("你會成為網頁前端開發人員!")
# elif lang == "PHP":
#     print("你會成為網頁後端開發人員!")
# elif lang == "Python":
#     print("你會成為資料科學家!")
# elif lang == "Kotlin":
#     print("你會成為Android應用程式開發人員!")
# elif lang == "Swift":
#     print("你會成為iOS應用程式開發人員!")
# else:
#     print("你會成為其他開發人員")


# match subject:
#     case <pattern_1>:
#         <action_1>
#     case <pattern_2>:
#         <action_2>
#     case <pattern_3>:
#         <action_3>
#     case _:
#         <action_wildcard>


match lang:
    case "JavaScript":
        print("你會成為網頁前端開發人員!")
    case "PHP":
        print("你會成為網頁後端開發人員!")
    case "Python":
        print("你會成為資料科學家!")
    case "Kotlin":
        print("你會成為Android應用程式開發人員!")
    case "Swift":
        print("你會成為iOS應用程式開發人員!")
    case _:
        print("你會成為其他開發人員")