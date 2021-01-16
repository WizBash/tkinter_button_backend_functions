from tkinter import*

#============vutton function=================
def press():
  label.config(text='button clicked')

root=Tk()
root.title('button_functions')


Btn = Button(width=10,text='Click Me',command=press)
Btn.grid(row=1, column=1)
label=Label(text='not clicked')
label.grid(row=2,column=1)



maainloop()
