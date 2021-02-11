import sqlite3
from xlsxwriter.workbook import Workbook

workbook = Workbook('output3.xlsx')
worksheet = workbook.add_worksheet()

db=sqlite3.connect('Finance.db')
conn=db.cursor()

data=conn.execute('SELECT * FROM fees_pay')
for i, row in enumerate(data):
	for j, value in enumerate(row):
		worksheet.write(i, j, value)
workbook.close()


db.close()