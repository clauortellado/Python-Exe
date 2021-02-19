from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

window.config(menu=menu)
window.mainloop()