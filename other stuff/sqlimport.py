# import csv


# csvData = [['Name of Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

# with open('person.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvData)

# csvFile.close()

# import xlrd
# import csv

# def csv_from_excel():
#     wb = xlrd.open_workbook('alldataoflavinmoviewithoutsize.xlsx')
#     sh = wb.sheet_by_name('Sheet')
#     your_csv_file = open('A.csv', 'w')
#     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

#     for rownum in range(sh.nrows):
#         wr.writerow(sh.row_values(rownum))

#     your_csv_file.close()

# runs the csv_from_excel function:
# csv_from_excel()

# import pandas as pd
# data_xls = pd.read_excel('alldataoflavinmoviewithoutsize.xlsx', 'Sheet', index_col=None)
# data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)


# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="import_testing")
# mycursor = mydb.cursor()
# sql = ""
# mycursor.execute(sql)
# a = mycursor.fetchall()

# with open('A.csv', 'r') as csvFile:
# 	reader = csv.reader(csvFile)
# 	for row in reader:
# 		print(row)

# csvFile.close()


# import xlrd
# import unicodecsv

# def xls2csv (xls_filename, csv_filename):

# 	wb = xlrd.open_workbook(xls_filename)
# 	sh = wb.sheet_by_index(0)

# 	fh = open(csv_filename,"wb")
# 	csv_out = unicodecsv.writer(fh, encoding='utf-8')

# 	for row_number in range (sh.nrows):
# 		csv_out.writerow(sh.row_values(row_number))

# 	fh.close()
# xls2csv('alldataoflavinmoviewithoutsize.xlsx','abc.csv')


# print(float(1))
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="show")
mycursor = mydb.cursor()

sql = "SELECT `season_name` FROM `season_name`"
mycursor.execute(sql)
auto= mycursor.fetchall()
autodict = {}

for i in auto:
	autodict[i[0]] = 'null'



print(autodict)

# %7B%22Arrow%22%3A%20%22null%22%2C%20%22Suits%22%3A%20%22null%22%2C%20%22Barry%22%3A%20%22null%22%2C%20%22Game%20Of%20thrones%22%3A%20%22null%22%2C%20%22gunpowder%22%3A%20%22null%22%7D