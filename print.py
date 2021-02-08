import tempfile
import os 
from tkinter import*

def iprint():
	q=ent.get()
	file=tempfile.mktemp('.txt')
	open(file,'w').write(q)
	os.startfile(file,'print')

root=Tk()

ent=Entry(width=20,fon=('times',14))
ent.pack()
btn=Button(text='print',width=10,font=('times',15),comman=iprint)
btn.pack()




mainloop()