from tkinter import *
base=Tk()
import math
val = ""
operator = ""
a = 0
def btn1():
    global val
    val = val+"1"
    data.set(val)
def btn2():
    global val
    val = val+"2"
    data.set(val)
def btn3():
    global val
    val = val+"3"
    data.set(val)
def btn4():
    global val
    val = val+"4"
    data.set(val)
def btn5():
    global val
    val = val+"5"
    data.set(val)
def btn6():
    global val
    val = val+"6"
    data.set(val)
def btn7():
    global val
    val = val+"7"
    data.set(val)
def flot():
    global val
    val = val+"."
    data.set(val)
def btn8():
    global val
    val = val+"8"
    data.set(val)
def btn9():
    global val
    val = val+"9"
    data.set(val)
def btn0():
    global val
    val = val+"0"
    data.set(val)
def btn00():
    global val
    val = val+"00"
    data.set(val)
def btnplus():
    global a
    global operator
    global val
    a=int(val)
    operator ="+"
    val = val + "+"
    data.set(val)
def btnmul():
    global a
    global operator
    global val
    a=int(val)
    operator ="*"
    val = val + "x"
    data.set(val)
def btndiv():
    global a
    global operator
    global val
    a=int(val)
    operator ="/"
    val = val + "/"
    data.set(val)
def btnsub():
    global a
    global operator
    global val
    a=int(val)
    operator ="-"
    val = val + "-"
    data.set(val)
def btnc():
    global a
    global operator
    global val
    a = 0
    operator = ""
    val = ""
    data.set(val)
def sin():
    global val
    val=float(val)
    val=math.sin(val)
    data.set(val)
def cos():
    global val
    val=float(val)
    val = math.cos(val)
    data.set(val)
def log():
    global val
    val=int(val)
    val=math.log(val)
    data.set(val)
def tan():
    global val
    val=float(val)
    val = math.tan(val)
    data.set(val)
def factorial():
    global val
    val = int(val)
    val = math.factorial(val)
    data.set(val)
def rad():
    global val
    val=float(val)
    val = math.radians(val)
    data.set(val)
def deg():
    global val
    val=int(val)
    val = math.degrees(val)
    data.set(val)
def x2():
    global val
    val=int(val)
    val = val*val*val
    data.set(val)
def x3():
    global val
    val = int(val)
    val = val*val*val
    data.set(val)
def percentage():
    global val
    val=int(val)
    val = val / 100
    data.set(val)
def e():
    val = 2.71828
    data.set(val)
def result():
    global a
    global operator
    global val
    vall = val
    if operator == "+":
        x = int((vall.split("+")[1]))
        c=a+x
        data.set(c)
        val=str(c)
    if operator == "*":
        x = int((vall.split("x")[1]))
        c=a*x
        data.set(c)
        val=str(c)
    if operator == "/":
        x = int((vall.split("/")[1]))
        c=a/x
        data.set(c)
        val=str(c)
    if operator == "-":
        x = int((vall.split("-")[1]))
        c=a-x
        data.set(c)
        val=str(c)
base.title('calculator')
base.geometry("400x500")
rowx=Frame(base,bg="#ffffff")
rowx.pack(expand=True, fill ="both")
rowk=Frame(base,bg="#ffffff")
rowk.pack(expand=True, fill ="both")
data = StringVar()
lbl=Label(base,anchor=SE,bg="#c0c0c0",textvariable=data,background = "#ffffff",fg = "#000000",font=22)
lbl.pack(expand=True,fill='both')
roww=Frame(base,bg="#c0c0c0")
roww.pack(expand=True, fill ="both")
row1=Frame(base)
row1.pack(expand=True, fill ="both")
row2=Frame(base,bg="grey")
row2.pack(expand=True, fill ="both")
row3=Frame(base,bg="black")
row3.pack(expand=True, fill ="both")
row4=Frame(base,bg="grey")
row4.pack(expand=True, fill ="both")
row5=Frame(base,bg="grey")
row5.pack(expand=True, fill ="both")
btn7=Button(row1,text="7",bg="#c0c0c0",borderwidth=0,relief=FLAT, font=("verdana",22),command=btn7)
btn7.pack(side=LEFT,expand= True,fill="both")
btn8=Button(row1,text="8",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn8)
btn8.pack(side=LEFT,expand= True,fill="both")
btn9=Button(row1,text="9",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn9)
btn9.pack(side=LEFT,expand= True,fill="both")
btnx=Button(row1,text="x",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",11),command=btnmul)
btnx.pack(side=LEFT,expand= True,fill="both")
btn9=Button(row1,text="sin",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",11),command=sin)
btn9.pack(side=LEFT,expand= True,fill="both")
btnx=Button(row1,text="=",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",14),command=result)
btnx.pack(side=LEFT,expand= True,fill="both")
btn4=Button(row2,text="4",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn4)
btn4.pack(side=LEFT,expand= True,fill="both")
btn5=Button(row2,text="5",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn5)
btn5.pack(side=LEFT,expand= True,fill="both")
btn6=Button(row2,text="6",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn6)
btn6.pack(side=LEFT,expand= True,fill="both")
btni=Button(row2,text="-",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",11),command=btnsub)
btni.pack(side=LEFT,expand= True,fill="both")
btn6=Button(row2,text="cos",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",10),command=cos)
btn6.pack(side=LEFT,expand= True,fill="both")
btni=Button(row2,text="log",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",10),command=log)
btni.pack(side=LEFT,expand= True,fill="both")
btn1=Button(row3,text="1",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn1)
btn1.pack(side=LEFT,expand= True,fill="both")
btn2=Button(row3,text="2",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn2)
btn2.pack(side=LEFT,expand= True,fill="both")
btn3=Button(row3,text="3",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22),command=btn3)
btn3.pack(side=LEFT,expand= True,fill="both")
btnp=Button(row3,text="+ ",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11),command=btnplus)
btnp.pack(side=LEFT,expand= True,fill="both")
btn6=Button(row3,text="tan  ",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11),command=tan)
btn6.pack(side=LEFT,expand= True,fill="both")
btni=Button(row3,text="n!",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11),command=factorial)
btni.pack(side=LEFT,expand= True,fill="both")
btnd=Button(row4,text=" /",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",15),command=btndiv)
btnd.pack(side=LEFT,expand= True,fill="both")
btno=Button(row4,text="  0",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",22),command=btn0)
btno.pack(side=LEFT,expand= True,fill="both")
btnoo=Button(row4,text="00 ",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",22),command=btn00)
btnoo.pack(side=LEFT,expand= True,fill="both")
btndo=Button(row4,text=". ",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",15),command=flot)
btndo.pack(side=LEFT,expand= True,fill="both")
btneq=Button(row4,text=" rad",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11),command=rad)
btneq.pack(side=LEFT,expand= True,fill="both")
btn6=Button(row4,text="deg  ",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",10),command=deg)
btn6.pack(side=LEFT,expand= True,fill="both")
btn22=Button(row5,text="x2",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11),command=x2)
btn22.pack(side=LEFT,expand= True,fill="both")
btn33=Button(row5,text="x3",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11),command=x3)
btn33.pack(side=LEFT,expand= True,fill="both")
btnsq=Button(row5,text=" C",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11),command=btnc)
btnsq.pack(side=LEFT,expand= True,fill="both")
btnpr=Button(row5,text="    %",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11),command=percentage)
btnpr.pack(side=LEFT,expand= True,fill="both")
btnsq=Button(row5,text="  x^y",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btnsq.pack(side=LEFT,expand= True,fill="both")
btnpr=Button(row5,text="e",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11),command=e)
btnpr.pack(side=LEFT,expand= True,fill="both")
base.mainloop()