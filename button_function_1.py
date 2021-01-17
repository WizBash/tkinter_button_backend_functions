from tkinter import*

#============vutton function=================
def press():
  label.config(text='button 1 clicked')
def press2():
  label.config(text='button 2 clicked')

root=Tk()
root.title('button_functions')


Btn = Button(width=10,text='button 1',command=press)
Btn.grid(row=1, column=1)
label=Label(text='not clicked')
label.grid(row=2,column=1)

btn2=Button(width=10,text='Button 2',command=press2)
Btn.grid(row=3, column=1)



maainloop()
 #bbb
