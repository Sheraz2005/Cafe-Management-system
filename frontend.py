from tkinter import *
root=Tk()
root.geometry("1650x700")
root.title("Cafe Management System")

e = Entry(root,width=30,borderwidth=5).grid(row=0, column=1, padx=10, pady=10)
e.pack()

myLabel=Label(root,text="enter your name").pack()
root.mainloop()
