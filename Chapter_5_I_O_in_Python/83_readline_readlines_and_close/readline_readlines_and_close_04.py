file = open("Chapter_5_I_O_in_Python/83_readline_readlines_and_close/myFile.txt")

while True:
    line = file.readline()
    if not line:
        break
    else:
        print(line)
        
file.close()