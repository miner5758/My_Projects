import xlsxwriter

workbook = xlsxwriter.Workbook('thing.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Timestamp')
worksheet.write('B1', 'Steps Reached')
worksheet.write('C1', '# of times game has been run')

workbook.close()
