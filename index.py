from tkinter import *
base=Tk()
base.title('calculator')
base.geometry("400x500")
lbl=Label(base,anchor=SE,bg="#c0c0c0")
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




btn7=Button(row1,text="7",bg="#c0c0c0",borderwidth=0,relief=FLAT, font=("verdana",22))
btn7.pack(side=LEFT,expand= True,fill="both")

btn8=Button(row1,text="8",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn8.pack(side=LEFT,expand= True,fill="both")

btn9=Button(row1,text="9",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn9.pack(side=LEFT,expand= True,fill="both")

btnx=Button(row1,text="x",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",11))
btnx.pack(side=LEFT,expand= True,fill="both")

btn9=Button(row1,text="sin",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",11))
btn9.pack(side=LEFT,expand= True,fill="both")

btnx=Button(row1,text="=",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",14))
btnx.pack(side=LEFT,expand= True,fill="both")



btn4=Button(row2,text="4",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn4.pack(side=LEFT,expand= True,fill="both")

btn5=Button(row2,text="5",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn5.pack(side=LEFT,expand= True,fill="both")

btn6=Button(row2,text="6",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn6.pack(side=LEFT,expand= True,fill="both")

btni=Button(row2,text="-",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",11))
btni.pack(side=LEFT,expand= True,fill="both")

btn6=Button(row2,text="cos",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",10))
btn6.pack(side=LEFT,expand= True,fill="both")

btni=Button(row2,text="log",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",10))
btni.pack(side=LEFT,expand= True,fill="both")





btn1=Button(row3,text="1",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn1.pack(side=LEFT,expand= True,fill="both")

btn2=Button(row3,text="2",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn2.pack(side=LEFT,expand= True,fill="both")

btn3=Button(row3,text="3",bg="#c0c0c0",borderwidth=0,relief=FLAT,font=("verdana",22))
btn3.pack(side=LEFT,expand= True,fill="both")

btnp=Button(row3,text="+  ",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btnp.pack(side=LEFT,expand= True,fill="both")

btn6=Button(row3,text="tan  ",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11))
btn6.pack(side=LEFT,expand= True,fill="both")

btni=Button(row3,text="n!",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11))
btni.pack(side=LEFT,expand= True,fill="both")



btnd=Button(row4,text="/",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11))
btnd.pack(side=LEFT,expand= True,fill="both")

btno=Button(row4,text="0",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",22))
btno.pack(side=LEFT,expand= True,fill="both")

btndo=Button(row4,text=".",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",15))
btndo.pack(side=LEFT,expand= True,fill="both")

btneq=Button(row4,text=" rad",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btneq.pack(side=LEFT,expand= True,fill="both")

btn6=Button(row4,text="deg  ",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",10))
btn6.pack(side=LEFT,expand= True,fill="both")

btni=Button(row4,text="e",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btni.pack(side=LEFT,expand= True,fill="both")



btn22=Button(row5,text="x^2",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btn22.pack(side=LEFT,expand= True,fill="both")

btn33=Button(row5,text="x^3",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btn33.pack(side=LEFT,expand= True,fill="both")

btnsq=Button(row5,text="C",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btnsq.pack(side=LEFT,expand= True,fill="both")

btnpr=Button(row5,text="%",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btnpr.pack(side=LEFT,expand= True,fill="both")

btnsq=Button(row5,text="  x^y",borderwidth=0,bg="#c0c0c0",relief=FLAT,font=("verdana",11))
btnsq.pack(side=LEFT,expand= True,fill="both")

btnpr=Button(row5,text="mod",borderwidth=0,relief=FLAT,bg="#c0c0c0",font=("verdana",11))
btnpr.pack(side=LEFT,expand= True,fill="both")


base.mainloop()