import shutil
import os
import zipfile

with zipfile.ZipFile('Backup.zip','w') as my_zip:
	my_zip.write('Finance.db')


src='Backup.zip'

dst='E:/backup'

shutil.copy(src=src,dst=dst)