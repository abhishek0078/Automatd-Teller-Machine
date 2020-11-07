from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os

def dep():
    def insert():
        amt=e3.get()
        acn=e1.get()
        pin=e2.get()
        
        
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()
            a.execute("select *from dep where Account_no='"+acn+"'and pin='"+pin+"'")
            results=a.fetchall()
            count=a.rowcount
            if(count>0):
                a.execute("update dep set Deposit='"+amt+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("update dep set amount=amount+'"+amt+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("insert into detail(Account_no,pin,Deposit)values('"+acn+"','"+pin+"','"+amt+"')")
                conn.commit()
                messagebox.showinfo("Deposit Successfull",amt)
            else:
                messagebox.showinfo("Msg","Invalid AccountNo/Pin")
        except:
            conn.rollback()
            messagebox.showinfo("Deposit Unsuccessfull","not save")
        conn.close()
        dc.destroy()
    
    dc=Tk()
    dc.title("Welcome to the Deposit")
    dc.geometry("500x350")
    dc.resizable(False,False)
    dc.config(bg='lightgreen')
    l1=Label(dc,text='Enter Account Number',font=('arial',20,'bold'),bg='lightgreen',fg='black')
    l1.grid(row=0,column=0,padx=20,pady=15)
    Account_no=StringVar()
    e1=Entry(dc,textvariable=Account_no)
    e1.grid(row=0,column=1,padx=20,pady=15)
    l2=Label(dc,text='Enter Pin',font=('arial',20,'bold'),bg='lightgreen',fg='black')
    l2.grid(row=1,column=0,padx=20,pady=15)
    pin=StringVar()
    e2=Entry(dc,show='*',textvariable=pin)
    e2.grid(row=1,column=1,padx=20,pady=15)
    l3=Label(dc,text='Enter Amount',font=('arial',20,'bold'),bg='lightgreen',fg='black')
    l3.grid(row=2,column=0,padx=20,pady=15)
    amount=StringVar()
    e3=Entry(dc,textvariable=amount)
    e3.grid(row=2,column=1,padx=20,pady=15)
    btn=Button(dc,text='Deposit',bd=6,width=13,font=('arial',20,'bold'),bg='black',fg='lightgreen',command=insert)
    btn.grid(row=3,column=0,padx=20,pady=15)
    

