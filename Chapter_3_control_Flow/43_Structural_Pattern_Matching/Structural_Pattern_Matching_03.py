# Structural Pattern Matching
# switch statement ==
# or

command = input("Where do you wanna go?")
match command.split(" "):
    case ["Go", "north"]:
        print("You are heading to the north.")
    case ["Go", "east"]:
        print("You are heading to the east.")
    case ["Go", "west"]:
        print("You are heading to the west.")
    case ["Go", "south"]:
        print("You are heading to the south.")
    case ["Turn", "left"]:
        print("You want to turn left.")
    case ["Turn", "right"]:
        print("You want to turn right.")