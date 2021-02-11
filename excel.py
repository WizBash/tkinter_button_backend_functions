import sqlite3
from xlsxwriter.workbook import Workbook

workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()

db=sqlite3.connect('Finance.db')
conn=db.cursor()

data=conn.execute('SELECT * FROM fees_pay')
for i, row in enumerate(data):
	print(row)
	worksheet.write(i,0, row[0])
	worksheet.write(i,1, row[1])
workbook.close()


db.close()