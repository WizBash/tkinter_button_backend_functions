from tkinter import*
def printrct():
	global receipt_text
	r=Tk()
	r.title('Confirm User')
	#r.overrideredirect(True) # removes the titile bar
	r.config(bg='blueviolet')
	r.resizable(0,0)
	#r.wm_attributes('-alpha',0.9) # makes transparent window
	r.wm_attributes('-topmost',True) #on top of all windows
	r.iconbitmap('icon.ico')
	r.geometry("320x630+550+100")

	fr=Frame(r,bg='blueviolet')
	fr.grid(row=1,column=1)
	receipt_text=Text(fr,fg='black',width=35,height=28,font=('times',14))
	receipt_text.grid(row=1,column=1,columnspan=2)
	bpc=Button(fr,text='Cancel',font=('times',15),width=13,bg='blue',fg='red',relief='raised',command='')
	bpc.grid(row=2,column=1)
	bpp=Button(fr,text='Print',font=('times',15),width=14,bg='blue',fg='yellow',relief='raised',command='')
	bpp.grid(row=2,column=2)

	mainloop()

	pass

printrct()