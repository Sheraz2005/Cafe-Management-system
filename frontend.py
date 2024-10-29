from tkinter import *
from tkinter import font
import datetime
import sqlite3


root=Tk()
root.geometry("1650x700")
root.title("Cafe Management System")



def menucard():
    rt=Tk()
    rt.title("Menu Card")

    frame = Frame(rt,highlightbackground="black", highlightthickness=2, width = 230, height=200,border=20)
    frame.pack()

    title_font=font.Font(size=30)
    title=Label(rt,text="----MENU----",font=title_font, fg="black")
    title.place(relx=0.1,rely=0.1,anchor=CENTER)

    title.pack()

    myLab=Label(rt,text="PIZZA",font=("Calibri",14,"bold"))
    myLab.place(relx=0.1,rely=0.1,anchor='w')

    myLab1=Label(rt,text="BURGER",font=("Calibri",14,"bold"))
    myLab1.place(relx=0.1,rely=0.3,anchor='w')

    myLab2=Label(rt,text="ICE CREAM",font=("Calibri",14,"bold"))
    myLab2.place(relx=0.1,rely=0.5,anchor='w')

    myLab3=Label(rt,text="DRINKS",font=("Calibri",14,"bold"))
    myLab3.place(relx=0.1,rely=0.7,anchor='w')


    myLab=Label(rt,text="250/-",font=("Calibri",14,"bold"))
    myLab.place(relx=0.7,rely=0.1,anchor='w')

    myLab1=Label(rt,text="140/-",font=("Calibri",14,"bold"))
    myLab1.place(relx=0.7,rely=0.3,anchor='w')

    myLab2=Label(rt,text="90/-",font=("Calibri",14,"bold"))
    myLab2.place(relx=0.7,rely=0.5,anchor='w')

    myLab3=Label(rt,text="50/-",font=("Calibri",14,"bold"))
    myLab3.place(relx=0.7,rely=0.7,anchor='w')
   
orderno = StringVar()
pizza = StringVar()
burger = StringVar()
icecream = StringVar()
drinks = StringVar()
cost = StringVar()
subtotal = StringVar()
gst = StringVar()
service = StringVar()
total = StringVar()

def tottal():
    # get order
    ord_n=orderno.get()
    piz=float(pizza.get())
    bur=float(burger.get())
    ic=float(icecream.get())
    drk=float(drinks.get())

    #computing charges

    costpiz=piz*250
    costbur=bur*140
    costic=ic*90
    costdrk=drk*50
    costmeal=(costbur+costdrk+costic+costpiz)
    costgst=(costmeal)*0.18
    costsrt=(costmeal)*0.05
    totTax=(costgst+costsrt)
    total_amt=(costmeal+totTax)

    fcmeal=str(costmeal)
    fgst=str(costgst)
    fsrt=str(costsrt)
    ftot=str(total_amt)
    #setting values

    cost.set(fcmeal)
    subtotal.set(fcmeal)
    gst.set(fgst)
    service.set(fsrt) 
    total.set(ftot)

def reset():
        orderno.set("")
        pizza.set("")
        burger.set("")
        icecream.set("")
        drinks.set("")
        cost.set("")
        subtotal.set("")
        gst.set("")
        service.set("")
        total.set("")

def exit():
        root.destroy()


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


e1 = Entry(root,width=30,borderwidth=5,textvariable=orderno,font=("Calibri",10,"bold"))
e1.place(relx=0.08,rely=0.2,anchor='w')
myLabel1=Label(root,text="Order Number:",font=("Calibri",12,"bold"))
myLabel1.place(relx=0.01,rely=0.2,anchor='w')

lab=Label(root,text="---------Order Details--------",font=("Calibri",12,"bold"))
lab.place(relx=0.06,rely=0.25,anchor='w')

e2 = Entry(root,width=30,borderwidth=5,textvariable=pizza,font=("Calibri",10,"bold"))
e2.place(relx=0.08,rely=0.30,anchor='w')
myLabel2=Label(root,text="Pizza:",font=("Calibri",12,"bold"))
myLabel2.place(relx=0.03,rely=0.30,anchor='w')

e3 = Entry(root,width=30,borderwidth=5,textvariable=burger,font=("Calibri",10,"bold"))
e3.place(relx=0.08,rely=0.35,anchor='w')
myLabel3=Label(root,text="Burger:",font=("Calibri",12,"bold"))
myLabel3.place(relx=0.025,rely=0.35,anchor='w')

e4 = Entry(root,width=30,borderwidth=5,textvariable=icecream,font=("Calibri",10,"bold"))
e4.place(relx=0.08,rely=0.40,anchor='w')
myLabel4=Label(root,text="Ice Cream:",font=("Calibri",12,"bold"))
myLabel4.place(relx=0.02,rely=0.40,anchor='w')

e5 = Entry(root,width=30,borderwidth=5,textvariable=drinks,font=("Calibri",10,"bold"))
e5.place(relx=0.08,rely=0.45,anchor='w')
myLabel5=Label(root,text="Drinks:",font=("Calibri",12,"bold"))
myLabel5.place(relx=0.025,rely=0.45,anchor='w')

lab2=Label(root,text="-----------Bill Details----------",font=("Calibri",12,"bold"))
lab2.place(relx=0.06,rely=0.50,anchor='w')

e6 = Entry(root,width=30,borderwidth=5,textvariable=cost,font=("Calibri",10,"bold"))
e6.place(relx=0.08,rely=0.55,anchor='w')
myLabel6=Label(root,text="Cost:",font=("Calibri",12,"bold"))
myLabel6.place(relx=0.03,rely=0.55,anchor='w')

e7 = Entry(root,width=30,borderwidth=5,textvariable=subtotal,font=("Calibri",10,"bold"))
e7.place(relx=0.08,rely=0.60,anchor='w')
myLabel7=Label(root,text="Subtotal:",font=("Calibri",12,"bold"))
myLabel7.place(relx=0.025,rely=0.60,anchor='w')

e8 = Entry(root,width=30,borderwidth=5,textvariable=gst,font=("Calibri",10,"bold"))
e8.place(relx=0.08,rely=0.70,anchor='w')
myLabel8=Label(root,text="GST:",font=("Calibri",12,"bold"))
myLabel8.place(relx=0.035,rely=0.70,anchor='w')

e9 = Entry(root,width=30,borderwidth=5,textvariable=service,font=("Calibri",10,"bold"))
e9.place(relx=0.08,rely=0.75,anchor='w')
myLabel9=Label(root,text="Service Tax:",font=("Calibri",12,"bold"))
myLabel9.place(relx=0.02,rely=0.75,anchor='w')

e0 = Entry(root,width=30,borderwidth=5,textvariable=total,font=("Calibri",10,"bold"))
e0.place(relx=0.08,rely=0.80,anchor='w')
myLabel0=Label(root,text="Total:",font=("Calibri",12,"bold"))
myLabel0.place(relx=0.03,rely=0.80,anchor='w')
    

def buttons_FE():
    myButton1=Button(root,text="Menu Card",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey",command=menucard)
    myButton1.place(relx=0.3,rely=0.20,anchor='n')

    myButton2=Button(root,text="Add",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton2.place(relx=0.37,rely=0.20,anchor='n')

    myButton3=Button(root,text="Delete Record",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey")
    myButton3.place(relx=0.3,rely=0.31,anchor='n')

    myButton4=Button(root,text="Reset",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey",command=reset)
    myButton4.place(relx=0.37,rely=0.31,anchor='n')

    myButton5=Button(root,text="Total",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey",command=tottal)
    myButton5.place(relx=0.3,rely=0.42,anchor='n')

    myButton6=Button(root,text="Exit System",font=("Calibri",12,"bold"),height=3,width=12,borderwidth=5,bg="grey",command=exit)
    myButton6.place(relx=0.37,rely=0.42,anchor='n')

    myButton7=Button(root,text="FeedBack Form",font=("Calibri",12,"bold"),height=3,width=17,borderwidth=5,bg="grey")
    myButton7.place(relx=0.335,rely=0.55,anchor='n')
buttons_FE()

def table_FE():
     lst[]


def framess():
    frame = Frame(root, bg='white',highlightbackground="black", highlightthickness=2, width = 700, height=520,border=20)
    frame.place(relx=0.93,rely=0.535,anchor='e')

    # label1=Label(frame,text="Order No.   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label1.place(relx=-0.01,rely=-0.035,anchor='nw')

    # label2=Label(frame,text="Pizza   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label2.place(relx=0.11,rely=-0.035,anchor='nw')

    # label3=Label(frame,text="Burger   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label3.place(relx=0.19,rely=-0.035,anchor='nw')

    # label4=Label(frame,text="Ice Cream   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label4.place(relx=0.28,rely=-0.035,anchor='nw')

    # label5=Label(frame,text="Drinks   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label5.place(relx=0.40,rely=-0.035,anchor='nw')

    # label6=Label(frame,text="Cost   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label6.place(relx=0.49,rely=-0.035,anchor='nw')

    # label7=Label(frame,text="Subtotal   |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label7.place(relx=0.57,rely=-0.035,anchor='nw')

    # label8=Label(frame,text="GST    |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label8.place(relx=0.69,rely=-0.035,anchor='nw')

    # label9=Label(frame,text="Service Tax     |",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label9.place(relx=0.77,rely=-0.035,anchor='nw')

    # label0=Label(frame,text="Total",bg='white',padx=2,pady=2,font=("Calibri",9))
    # label0.place(relx=0.93,rely=-0.035,anchor='nw')
framess()

root.mainloop()
