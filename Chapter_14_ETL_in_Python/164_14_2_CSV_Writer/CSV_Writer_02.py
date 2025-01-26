import csv

with open("Chapter_14_ETL_in_Python/164_14_2_CSV_Writer/new_01.csv", mode="w", newline="", encoding="cp950") as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerows([['e','f','g'], ['h','i','j']])