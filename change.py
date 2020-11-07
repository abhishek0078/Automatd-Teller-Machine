from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
def change():
    def pin():
        acn=e1.get()
        ol=e2.get()
        np=e3.get()
        cn=e4.get()
        try:
            
            if(np==cn):
                conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
                a=conn.cursor()
                a.execute("select *from dep where Account_no='"+acn+"'and pin='"+ol+"'")
                results=a.fetchall()
                count=a.rowcount
                if(count>0):
                    a.execute("update dep set pin='"+np+"' where Account_no='"+acn+"' and pin='"+ol+"'")
                    a.execute("update detail set pin='"+np+"'where Account_no='"+acn+"' and pin='"+ol+"'")
                    conn.commit()
                    messagebox.showinfo("message","change")
                else:
                    messagebox.showinfo("message","Invalid AccountNo/Pin")
            else:
                messagebox.showinfo("message","not match password")
        except:
            conn.rollback()
            messagebox.showinfo("message","not change")
            conn.close()
        ch.destroy()

    ch=Tk()
    ch.title('Welcome to the main page')
    ch.geometry('550x400')
    ch.resizable(False,False)
    ch.config(bg='lightgreen')
    cframe=Frame(ch,bg='lightgreen')
    cframe.pack(pady=30)
    l1=Label(cframe,text='Enter Account',font=('arial',20,'bold'),bg='lightgreen')
    l1.grid(row=0,column=0,padx=5,pady=10)
    act=StringVar()
    e1=Entry(cframe,textvariable=act)
    e1.grid(row=0,column=1,padx=5,pady=10)
    l2=Label(cframe,text='Enter old pin!',font=('arial',20,'bold'),bg='lightgreen')
    l2.grid(row=1,column=0,padx=5,pady=10)
    opin=StringVar()
    e2=Entry(cframe,show='*',textvariable=opin)
    e2.grid(row=1,column=1,padx=5,pady=10)
    l3=Label(cframe,text='Enter new pin!',font=('arial',20,'bold'),bg='lightgreen')
    l3.grid(row=2,column=0,padx=5,pady=10)
    npin=StringVar()
    e3=Entry(cframe,show='*',textvariable=npin)
    e3.grid(row=2,column=1,padx=5,pady=10)
    l4=Label(cframe,text='Re-Enter new pin',font=('arial',20,'bold'),bg='lightgreen')
    l4.grid(row=3,column=0,padx=5,pady=10)
    rpin=StringVar()
    e4=Entry(cframe,show='*',textvariable=rpin)
    e4.grid(row=3,column=1,padx=5,pady=10)
    btn=Button(cframe,bd=6,fg='lightgreen',bg='black',font=('arial',20,'bold'),width=6,text='Change',command=pin)
    btn.grid(row=4,column=0,padx=10,pady=20)
