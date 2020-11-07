from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
def fast():
    def insert(amt):
        acn=e1.get()
        pin=e2.get()
        #amt=e3.get()
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()
            a.execute("select *from dep where Account_no='"+acn+"'and pin='"+pin+"'")
            results=a.fetchall()
            count=a.rowcount
            if(count>0):
                a.execute("update dep set withdraw=withdraw+'"+str(amt)+"'where Account_no ='"+acn+"'and pin='"+pin+"'")
                a.execute("update dep set amount=amount-'"+str(amt)+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("insert into detail(Account_no,pin,Withdraw)values('"+acn+"','"+pin+"','"+str(amt)+"')")
                conn.commit()
                #print('save')
                messagebox.showinfo("Withdrawal successfull",amt)
            else:
                messagebox.showinfo("Msg","Invalid AccountNo/Pin")
        except:
            conn.rollback()
            print('not save')
            messagebox.showinfo("Withdrawal unsuccessfull",amt)
        conn.close()
        ft.destroy()
    ft=Tk()
    ft.title('Welcome to Fast Cash')
    ft.geometry('450x300')
    ft.resizable(False,False)
    ft.config(bg='grey')
    fframe=Frame(ft,bg='grey')
    fframe.pack(padx=10,pady=30)
    l1=Label(fframe,text='Enter account no.',font=('arial',20,'bold'),fg='lightgreen',bg='grey')
    l1.grid(row=0,column=0)
    acn=StringVar()
    e1=Entry(fframe,textvariable=acn)
    e1.grid(row=0,column=1)
    l2=Label(fframe,text='Enter pin',font=('arial',20,'bold'),fg='lightgreen',bg='grey')
    l2.grid(row=1,column=0)
    pin=StringVar()
    e2=Entry(fframe,show='*',textvariable=pin)
    e2.grid(row=1,column=1)
    btn1=Button(fframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="200",command=lambda:insert(200))
    btn1.grid(row=2,column=0,padx=8,pady=10)
    btn2=Button(fframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="500",command=lambda:insert(500))
    btn2.grid(row=2,column=1,padx=8,pady=10)
    btn3=Button(fframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="1000",command=lambda:insert(1000))
    btn3.grid(row=3,column=0,padx=8,pady=10)
    btn4=Button(fframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="2000",command=lambda:insert(2000))
    btn4.grid(row=3,column=1,padx=8,pady=10)
