from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
def update():
    def contact():
        ncn=e4.get()
        acn=e1.get()
        pin=e2.get()
        rcn=e5.get()
        try:
            if(ncn==rcn):
                conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
                a=conn.cursor()
                #a.execute("select *from emp where id='"+uid+"'")
                #count=a.rowcount
                #if(count>0):
                a.execute("update dep set Contact='"+ncn+"' where Account_no='"+acn+"' and pin='"+pin+"'")
                conn.commit()
                messagebox.showinfo("message","change")
                #else:
                #messagebox.showinfo("message","record not found")
            else:
                messagebox.showinfo("message","not match")
        except:
            conn.rollback()
            messagebox.showinfo("message","not change")
            conn.close()
        up.destroy()
    up=Tk()
    up.title('Welcome to contact page details')
    up.geometry('550x400')
    up.resizable(False,False)
    up.config(bg='lightgreen')
    uframe=Frame(up,bg='lightgreen')
    uframe.pack(pady=16)
    l1=Label(uframe,text='Enter Account No.',font=('arial',20,'bold'),bg='lightgreen')
    l1.grid(row=0,column=0,pady=8)
    acn=StringVar()
    e1=Entry(uframe,textvariable=acn)
    e1.grid(row=0,column=1)
    l2=Label(uframe,text='Enter pin',font=('arial',20,'bold'),bg='lightgreen')
    l2.grid(row=1,column=0,pady=8)
    pin=StringVar()
    e2=Entry(uframe,show='*',textvariable=pin)
    e2.grid(row=1,column=1)
    l3=Label(uframe,text='Enter old contact number!',font=('arial',20,'bold'),bg='lightgreen')
    l3.grid(row=2,column=0,pady=8)
    ocn=StringVar()
    e3=Entry(uframe,textvariable=ocn)
    e3.grid(row=2,column=1)
    l4=Label(uframe,text='Enter new contact number!',font=('arial',20,'bold'),bg='lightgreen')
    l4.grid(row=3,column=0,pady=8)
    ncn=StringVar()
    e4=Entry(uframe,textvariable=ncn)
    e4.grid(row=3,column=1)
    l5=Label(uframe,text='Re-Enter new contact number',font=('arial',20,'bold'),bg='lightgreen')
    l5.grid(row=4,column=0,pady=8)
    rcn=StringVar()
    e5=Entry(uframe,textvariable=rcn)
    e5.grid(row=4,column=1)
    btn=Button(uframe,bd=6,bg='black',fg='lightgreen',font=('arial',20,'bold'),width=6,text='Change',command=contact)
    btn.grid(row=5,column=0,pady=8)
