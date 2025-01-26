from openpyxl import Workbook
import csv

data_rows = [fields for fields in csv.reader(open("Chapter_14_ETL_in_Python/14-1file.csv", newline=""))]

wb = Workbook()
ws = wb.active
ws.title = "MyFile"
for row in data_rows:
    ws.append(row)

wb.save("Chapter_14_ETL_in_Python/165_Openpyxl/Myfile.xlsx")