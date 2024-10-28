from tkinter import *
from tkinter import font
import datetime

root=Tk()
root.geometry("1650x700")
root.title("Cafe Management System")

def title_label():
    title_font=font.Font(size=24)
    title=Label(root,text="CAFE MANAGEMENT SYSTEM",font=title_font, fg="black")
    title.pack()
title_label()

def Date_Time():
    t = datetime.datetime.now()
    mylabel2=Label ( root,text="Date : "+str(t.day) + "-" + str(t.month) + "-" + str(t.year),font=("Calibri",10,"bold") )
    mylabel2.pack()
    mylabel3=Label ( root,text= "Time : "+str(t.hour) + ":" + str(t.minute) + ":" + str(t.second),font=("Calibri",10,"bold"))
    mylabel3.pack()
Date_Time()

def input_FE():
    e1 = Entry(root,width=30,borderwidth=5)
    e1.place(relx=0.08,rely=0.2,anchor='w')
    myLabel1=Label(root,text="Order Number:",font=("Calibri",12,"bold"))
    myLabel1.place(relx=0.01,rely=0.2,anchor='w')

    lab=Label(root,text="---------Order Details--------",font=("Calibri",12,"bold"))
    lab.place(relx=0.06,rely=0.25,anchor='w')

    e2 = Entry(root,width=30,borderwidth=5)
    e2.place(relx=0.08,rely=0.30,anchor='w')
    myLabel2=Label(root,text="Pizza:",font=("Calibri",12,"bold"))
    myLabel2.place(relx=0.03,rely=0.30,anchor='w')

    e3 = Entry(root,width=30,borderwidth=5)
    e3.place(relx=0.08,rely=0.35,anchor='w')
    myLabel3=Label(root,text="Burger:",font=("Calibri",12,"bold"))
    myLabel3.place(relx=0.025,rely=0.35,anchor='w')

    e4 = Entry(root,width=30,borderwidth=5)
    e4.place(relx=0.08,rely=0.40,anchor='w')
    myLabel4=Label(root,text="Ice Cream:",font=("Calibri",12,"bold"))
    myLabel4.place(relx=0.02,rely=0.40,anchor='w')

    e5 = Entry(root,width=30,borderwidth=5)
    e5.place(relx=0.08,rely=0.45,anchor='w')
    myLabel5=Label(root,text="Drinks:",font=("Calibri",12,"bold"))
    myLabel5.place(relx=0.025,rely=0.45,anchor='w')

    lab2=Label(root,text="-----------Bill Details----------",font=("Calibri",12,"bold"))
    lab2.place(relx=0.06,rely=0.50,anchor='w')

    e6 = Entry(root,width=30,borderwidth=5)
    e6.place(relx=0.08,rely=0.55,anchor='w')
    myLabel6=Label(root,text="Cost:",font=("Calibri",12,"bold"))
    myLabel6.place(relx=0.03,rely=0.55,anchor='w')

    e7 = Entry(root,width=30,borderwidth=5)
    e7.place(relx=0.08,rely=0.60,anchor='w')
    myLabel7=Label(root,text="Subtotal:",font=("Calibri",12,"bold"))
    myLabel7.place(relx=0.025,rely=0.60,anchor='w')

    e8 = Entry(root,width=30,borderwidth=5)
    e8.place(relx=0.08,rely=0.70,anchor='w')
    myLabel8=Label(root,text="GST:",font=("Calibri",12,"bold"))
    myLabel8.place(relx=0.035,rely=0.70,anchor='w')

    e9 = Entry(root,width=30,borderwidth=5)
    e9.place(relx=0.08,rely=0.75,anchor='w')
    myLabel9=Label(root,text="Service Tax:",font=("Calibri",12,"bold"))
    myLabel9.place(relx=0.02,rely=0.75,anchor='w')

    e0 = Entry(root,width=30,borderwidth=5)
    e0.place(relx=0.08,rely=0.80,anchor='w')
    myLabel0=Label(root,text="Total:",font=("Calibri",12,"bold"))
    myLabel0.place(relx=0.03,rely=0.80,anchor='w')
    
input_FE()

def buttons_FE():
    myButton1=Button(root,text="Menu Card",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton1.place(relx=0.3,rely=0.20,anchor='n')

    myButton2=Button(root,text="Add",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton2.place(relx=0.37,rely=0.20,anchor='n')

    myButton3=Button(root,text="Delete Record",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton3.place(relx=0.3,rely=0.31,anchor='n')

    myButton4=Button(root,text="Reset",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton4.place(relx=0.37,rely=0.31,anchor='n')

    myButton5=Button(root,text="Total",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton5.place(relx=0.3,rely=0.42,anchor='n')

    myButton6=Button(root,text="Exit System",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton6.place(relx=0.37,rely=0.42,anchor='n')

    myButton7=Button(root,text="FeedBack Form",font=("Calibri",12,"bold"),height=3,width=17,borderwidth=5,bg="grey")
    myButton7.place(relx=0.335,rely=0.55,anchor='n')
buttons_FE()

def framess():
    frame = Frame(root, bg='white',highlightbackground="black", highlightthickness=2, width = 700, height=520,border=20)
    frame.place(relx=0.93,rely=0.535,anchor='e')

    label1=Label(frame,text="Order No.   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=-0.01,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Pizza   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.11,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Burger   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.19,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Ice Cream   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.28,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Drinks   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.40,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Cost   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.49,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Subtotal   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.57,rely=-0.035,anchor='nw')

    label1=Label(frame,text="GST    |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.69,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Service Tax     |",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.77,rely=-0.035,anchor='nw')

    label1=Label(frame,text="Total",bg='white',padx=2,pady=2,font=("Calibri",9))
    label1.place(relx=0.93,rely=-0.035,anchor='nw')
framess()

root.mainloop()
