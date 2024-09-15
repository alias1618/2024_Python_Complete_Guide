from sys import argv

if len(argv) < 2:
    print("Please provide a filename")
else:
    file = open(argv[1])
    lines = file.read()

    lines = lines.split("\n")
    word_count = 0
    letter_count = 0

    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)

    line_count = len(lines) - 1

    print(f"The line count is {line_count}")
    print(f"The word count is {word_count}")
    print(f"The letter count is {letter_count}")