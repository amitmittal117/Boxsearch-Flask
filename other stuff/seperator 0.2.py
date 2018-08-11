from xlrd import open_workbook
import xlsxwriter
import unicodecsv
import xlrd
import csv
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="import_testing")
mycursor = mydb.cursor()

count = 0
# letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','i']
# letter_list = ['A','B','C']
letter_list = ['A']
for every_letter in letter_list:
	workbook = xlsxwriter.Workbook("letterxl/"+str(every_letter)+'.xlsx')
	worksheet = workbook.add_worksheet()
	list_for_links = []
	book = open_workbook("alldataoflavinmoviewithoutsize.xlsx")
	for sheet in book.sheets():
		for rowidx in range(sheet.nrows):
			row = sheet.row(rowidx)
			for colidx, cell in enumerate(row):
				link = cell.value
				if link[33] == every_letter:
					# print(link)
					list_for_links.append(link)

	# for l in list_for_links:
	# 	print(l)
	row = col = 0
	for each_line in list_for_links:
		# print(each_line)
		worksheet.write(row,col,each_line)
		print (count)
		row = row + 1
		count = count +1
	workbook.close()

def xls2csv (xls_filename, csv_filename):

	wb = xlrd.open_workbook(xls_filename)
	sh = wb.sheet_by_index(0)
	print('converted')
	fh = open(csv_filename,"wb")
	csv_out = unicodecsv.writer(fh, encoding='utf-8')

	for row_number in range (sh.nrows):
		csv_out.writerow(sh.row_values(row_number))

	fh.close()

for every_letter in letter_list:
	xlsfile = 'letterxl/'+every_letter+'.xlsx'
	csvfile = 'lettercsv/'+every_letter+'.csv'
	xls2csv(xlsfile,csvfile)

for every_letter in letter_list:
	csv_data = csv.reader(file('lettercsv/'+every_letter+'.csv'))
	for row in csv_data:
		mycursor.execute('INSERT INTO '+every_letter+'(link) VALUES("%s")',row)
	
	mydb.commit()
	cursor.close()
	print ("Done")