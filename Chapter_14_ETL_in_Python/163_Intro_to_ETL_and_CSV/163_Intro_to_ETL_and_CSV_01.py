import csv

with open("Chapter_14_ETL_in_Python/14-1file.csv", newline="", encoding="cp950") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row)