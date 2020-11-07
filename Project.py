from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
from deposit import*
from withdrawl import*
from BalanceEnquiry import*
from statement import*
from fastcash import*
from change import*
from update import*
from transfer import*

win=Tk()
win.title("Welcome in PNB ATM")
win.config(bg="grey")
w, h = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry("%dx%d+0+0" % (w, h))
head=Label(win,text='ATM MACHINE',fg='black',bg='lightblue',font=("Times",46,"bold"),bd=20,relief='sunken',highlightthickness=15)
head.pack()
mframe=Frame(win,bg='grey')
mframe.pack(padx=80,pady=30)

btn1=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Deposit Cash",command=dep)
btn1.grid(row=1,column=0,padx=40,pady=18)
btn2=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Withdraw Cash",command=withdraw)
btn2.grid(row=2,column=0,padx=40,pady=18)
btn3=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Balance Enquiry",command=bal)
btn3.grid(row=3,column=0,padx=40,pady=18)
btn4=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Transfer Fund",command=transfer)
btn4.grid(row=4,column=0,padx=40,pady=18)
btn5=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Mini Statement",command=mini)
btn5.grid(row=1,column=1,padx=40,pady=18)
btn6=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Fast Cash",command=fast)
btn6.grid(row=2,column=1,padx=40,pady=18)
btn7=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Change Pin",command=change)
btn7.grid(row=3,column=1,padx=40,pady=18)
btn8=Button(mframe,padx=40,bd=10,fg='black',bg='lightblue',font=('arial',25,'bold'),width=18,text="Update Contact",command=update)
btn8.grid(row=4,column=1,padx=40,pady=18)
