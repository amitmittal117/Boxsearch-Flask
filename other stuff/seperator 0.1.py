from xlrd import open_workbook
import xlsxwriter
count = 0
letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','i']
# letter_list = ['A','B','C']
# letter_list = ['B']
for every_letter in letter_list:
	workbook = xlsxwriter.Workbook("diff/"+str(every_letter)+'.xlsx')
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
