from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os


def withdraw():
    def draw():
        acn=e1.get()
        pin=e2.get()
        amt=e3.get()
       
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()
            a.execute("select *from dep where Account_no='"+acn+"'and pin='"+pin+"'")
            results=a.fetchall()
            count=a.rowcount
            if(count>0):
                a.execute("update dep set withdraw='"+amt+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("update dep set amount=amount-'"+amt+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("insert into detail(Account_no,pin,Withdraw)values('"+acn+"','"+pin+"','"+amt+"')")
                conn.commit()
                messagebox.showinfo('Information','Withdrawl Successfully')
                #print(amt)
            else:
                messagebox.showinfo("Msg","Invalid AccountNo/Pin")
        except:
            conn.rollback()
            messagebox.showinfo('Information','Withdraw not possible')
            print('not save')
        conn.close()
        wd.destroy()
       
    
    wd=Tk()
    wd.title("Welcome to the Withdraw")
    wd.geometry("500x350")
    wd.resizable(False,False)
    wd.config(bg='lightgreen')
    l1=Label(wd,text='Enter Account Number',font=('arial',20,'bold'),bg='lightgreen')
    l1.grid(row=0,column=0,padx=20,pady=15)
    acn=StringVar()
    e1=Entry(wd,textvariable=acn)
    e1.grid(row=0,column=1,padx=20,pady=15)
    l2=Label(wd,text='Enter Pin',font=('arial',20,'bold'),bg='lightgreen')
    l2.grid(row=1,column=0,padx=20,pady=15)
    pin=StringVar()
    e2=Entry(wd,show='*',textvariable=pin)
    e2.grid(row=1,column=1,padx=20,pady=15)
    l3=Label(wd,text='Enter Amount',font=('arial',20,'bold'),bg='lightgreen')
    l3.grid(row=2,column=0,padx=20,pady=15)
    amt=StringVar()
    e3=Entry(wd,textvariable=amt)
    e3.grid(row=2,column=1,padx=20,pady=15)
    btn=Button(wd,text='Withdraw',font=('arial',20,'bold'),bd=6,bg='black',fg='lightgreen',command=draw)
    btn.grid(row=3,column=0,padx=20,pady=15)
