from openpyxl import Workbook
import csv

data_rows = [fields for fields in csv.reader(open("Chapter_14_ETL_in_Python/14-1file.csv", newline=""))]

wb = Workbook()
ws = wb.active
ws.title = "MyFile2"
ws.sheet_properties.tabColor = "1072BA"
for row in data_rows:
    ws.append(row)

wb.save("Chapter_14_ETL_in_Python/165_Openpyxl/Myfile2.xlsx")