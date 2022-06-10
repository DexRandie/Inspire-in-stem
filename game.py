from cProfile import label
from tkinter import *
window = Tk()
window.title = Label(window,text = "Project Aurora")
window.title.pack()
window.config(bg="purple")
window.geometry("1080x760")


f_name = Label(window,text="Day",font=("times new roman",20))
f_name.config(bg = "pink")
s_name=Label(window,text=" 1",font=("times new roman",20))
s_name.config(bg = "pink")
f_name.pack( padx = 5,pady = 10)
btn = Button(window,text="click here")
btn.grid(column = 70 , row=20)
btn.pack(padx =5 , pady = 10)
btn.config(bg = "red")
btn.config(fg = "white")
































window.mainloop()