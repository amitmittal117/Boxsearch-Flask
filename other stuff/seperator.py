from xlrd import open_workbook
# import xlsxwriter
import csv
count = 0
# letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','i']
# letter_list = ['A','B','C']
letter_list = ['A']
for every_letter in letter_list:
	
	list_for_links = []
	book = open_workbook("alldataoflavinmoviewithoutsize.xlsx")
	for sheet in book.sheets():
		for rowidx in range(sheet.nrows):
			row = sheet.row(rowidx)
			# print(type(row[0]))
			for colidx, cell in enumerate(row):
				link = cell.value
				if link[33] == every_letter:
					list_for_links.append(link)
	print (list_for_links)
	# with open('newcsv/'+every_letter+'.csv', 'w') as csvFile:
	# 	writer = csv.writer(csvFile)
	# 	writer.writerows(list_for_links)
	# csvFile.close()


#----------------------------------------------------
# to create the letter table
# database-name = ""
# table-name = ""
# sql = "CREATE TABLE '"+database-name+"'.'"+table-name+"'( 'link' VARCHAR(300) NOT NULL ) ENGINE = InnoDB;"
#----------------------------------------------------

	# workbook = xlsxwriter.Workbook('newcsv/'+str(every_letter)+' .xlsx')
	# worksheet = workbook.add_worksheet()
	# row = col = 0
	# for each_line in list_for_links:
	# 	worksheet.write(row,col,each_line)
	# 	print (count)
	# 	row = row + 1
	# 	count = count +1
	# workbook.close()
