# from xlrd import open_workbook
# import mysql.connector

# mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="import_testing")
# mycursor = mydb.cursor()

# letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','i']
# # letter_list = ['A','B','C','D','E','F','G','H']
# # letter_list = ['A','B','C']
# # letter_list = ['A']
# for every_letter in letter_list:
# 	book = open_workbook("alldataoflavinmoviewithoutsize.xlsx").sheets()
# 	for sheet in book:
# 		for rowidx in range(sheet.nrows):
# 			row = sheet.row(rowidx)
# 			for colidx, cell in enumerate(row):
# 				link = cell.value
# 				if link[33] == every_letter:
# 					sql = 'INSERT INTO '+every_letter+'(link) VALUES("'+link+'")'
# 					mycursor.execute(sql)
# 	mydb.commit()
# 	print (every_letter+" Done")

# a= 1
a = '1'
# print(isinstance(a, int))

b = '1'

if a != b:
	print('true')

# if str(type(a)) == "<class 'int'>":
# 	print(a)
