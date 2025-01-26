file = open("Chapter_5_I_O_in_Python/82_Intro_to_I_O_with_Files/myfile.txt")

print(file.read())
file.seek(0)
print(file.read())