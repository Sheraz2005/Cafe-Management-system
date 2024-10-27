from tkinter import *
from tkinter import font
import datetime

root=Tk()
root.geometry("1650x700")
root.title("Cafe Management System")

def title_label():
    title_font=font.Font(size=24)
    title=Label(root,text="CAFE MANAGEMENT",font=title_font)
    title.pack()
title_label()

def Date_Time():
    t = datetime.datetime.now()
    mylabel2=Label ( root,text=str(t.day) + "-" + str(t.month) + "-" + str(t.year) )
    mylabel2.pack()
    mylabel3=Label ( root,text= str(t.hour) + ":" + str(t.minute) + ":" + str(t.second))
    mylabel3.pack()
Date_Time()

def input_FE():
    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.2,anchor='w')
    myLabel=Label(root,text="Order Number:")
    myLabel.place(relx=0.01,rely=0.2,anchor='w')

    lab=Label(root,text="---------Order Details--------")
    lab.place(relx=0.06,rely=0.25,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.30,anchor='w')
    myLabel=Label(root,text="Pizza:")
    myLabel.place(relx=0.03,rely=0.30,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.35,anchor='w')
    myLabel=Label(root,text="Burger:")
    myLabel.place(relx=0.025,rely=0.35,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.40,anchor='w')
    myLabel=Label(root,text="Ice Cream:")
    myLabel.place(relx=0.02,rely=0.40,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.45,anchor='w')
    myLabel=Label(root,text="Drinks:")
    myLabel.place(relx=0.025,rely=0.45,anchor='w')

    lab=Label(root,text="-----------Bill Details----------")
    lab.place(relx=0.06,rely=0.50,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.55,anchor='w')
    myLabel=Label(root,text="Cost:")
    myLabel.place(relx=0.03,rely=0.55,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.60,anchor='w')
    myLabel=Label(root,text="Subtotal:")
    myLabel.place(relx=0.025,rely=0.60,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.70,anchor='w')
    myLabel=Label(root,text="GST:")
    myLabel.place(relx=0.035,rely=0.70,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.75,anchor='w')
    myLabel=Label(root,text="Service Tax:")
    myLabel.place(relx=0.02,rely=0.75,anchor='w')

    e = Entry(root,width=30,borderwidth=5)
    e.place(relx=0.08,rely=0.80,anchor='w')
    myLabel=Label(root,text="Total:")
    myLabel.place(relx=0.03,rely=0.80,anchor='w')
    
input_FE()

def buttons_FE():
    myButton=Button(root,text="Menu Card",height=3,width=10,borderwidth=5)
    myButton.place(relx=0.3,rely=0.20,anchor='n')
buttons_FE()
root.mainloop()
