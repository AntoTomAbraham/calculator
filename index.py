from tkinter import *
base=Tk()
base.title('calculator')
base.geometry("400x500")
lbl=Label(base,anchor=SE,)
lbl.pack(expand=True,fill='both')
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




btn7=Button(row1,text="7",borderwidth=0,relief=FLAT, font=("verdana",22))
btn7.pack(side=LEFT,expand= True,fill="both")

btn8=Button(row1,text="8",borderwidth=0,relief=FLAT,font=("verdana",22))
btn8.pack(side=LEFT,expand= True,fill="both")

btn9=Button(row1,text="9",borderwidth=0,relief=FLAT,font=("verdana",22))
btn9.pack(side=LEFT,expand= True,fill="both")

btnx=Button(row1,text="x",borderwidth=0,relief=FLAT,font=("verdana",22))
btnx.pack(side=LEFT,expand= True,fill="both")




btn4=Button(row2,text="4",borderwidth=0,relief=FLAT,font=("verdana",22))
btn4.pack(side=LEFT,expand= True,fill="both")

btn5=Button(row2,text="5",borderwidth=0,relief=FLAT,font=("verdana",22))
btn5.pack(side=LEFT,expand= True,fill="both")

btn6=Button(row2,text="6",borderwidth=0,relief=FLAT,font=("verdana",22))
btn6.pack(side=LEFT,expand= True,fill="both")

btni=Button(row2,text="-",borderwidth=0,relief=FLAT,font=("verdana",22))
btni.pack(side=LEFT,expand= True,fill="both")






btn1=Button(row3,text="1",borderwidth=0,relief=FLAT,font=("verdana",22))
btn1.pack(side=LEFT,expand= True,fill="both")

btn2=Button(row3,text="2",borderwidth=0,relief=FLAT,font=("verdana",22))
btn2.pack(side=LEFT,expand= True,fill="both")

btn3=Button(row3,text="3",borderwidth=0,relief=FLAT,font=("verdana",22))
btn3.pack(side=LEFT,expand= True,fill="both")

btnp=Button(row3,text="+",borderwidth=0,relief=FLAT,font=("verdana",22))
btnp.pack(side=LEFT,expand= True,fill="both")




btnd=Button(row4,text="/",borderwidth=0,relief=FLAT,font=("verdana",22))
btnd.pack(side=LEFT,expand= True,fill="both")

btno=Button(row4,text="0",borderwidth=0,relief=FLAT,font=("verdana",22))
btno.pack(side=LEFT,expand= True,fill="both")

btndo=Button(row4,text=".",borderwidth=0,relief=FLAT,font=("verdana",22))
btndo.pack(side=LEFT,expand= True,fill="both")

btneq=Button(row4,text="=",borderwidth=0,relief=FLAT,font=("verdana",22))
btneq.pack(side=LEFT,expand= True,fill="both")




btn22=Button(row5,text="x^2",borderwidth=0,relief=FLAT,font=("verdana",14))
btn22.pack(side=LEFT,expand= True,fill="both")

btn33=Button(row5,text="x^3",borderwidth=0,relief=FLAT,font=("verdana",14))
btn33.pack(side=LEFT,expand= True,fill="both")

btnsq=Button(row5,text="C",borderwidth=0,relief=FLAT,font=("verdana",14))
btnsq.pack(side=LEFT,expand= True,fill="both")

btnpr=Button(row5,text="%",borderwidth=0,relief=FLAT,font=("verdana",14))
btnpr.pack(side=LEFT,expand= True,fill="both")



base.mainloop()