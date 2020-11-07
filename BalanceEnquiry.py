from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
    
def bal():
    def account():
        acn=e1.get()
        pin=e2.get()
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()
            a.execute("select amount from dep where Account_no='"+acn+"'and pin='"+pin+"'")
            results = a.fetchall()
            count = a.rowcount
            if(count>0):
                for row in results:
                    for j in range(0,count):
                        messagebox.showinfo("Your Balance is",row[j])
        except:
            conn.rollback() 
            conn.close()
        wi.destroy()
        
    wi = Tk()
    wi.title("Welcome in PNB ATM")
    wi.geometry("450x250")
    wi.resizable(False,False)
    wi.config(bg='lightgreen')
    l1=Label(wi, text='Enter Account No.',font=('arial',20,'bold'),bg='lightgreen',fg='black')
    l1.grid(row=0,column=0,padx=10,pady=15)
    acn=StringVar()
    e1=Entry(wi,textvariable=acn)
    e1.grid(row=0,column=1,padx=10,pady=15)
    l2=Label(wi,text='Enter pin',font=('arial',20,'bold'),bg='lightgreen',fg='black')
    l2.grid(row=1,column=0,padx=10,pady=15)
    pin=StringVar()
    e2=Entry(wi,show="*",textvariable=pin)
    e2.grid(row=1,column=1,padx=10,pady=15)
    b1=Button(wi, text='Show',font=('arial',20,'bold'),bd=6,bg='black',fg='lightgreen',command=account)
    b1.grid(row=2,column=0,padx=10,pady=15)
