from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os

def transfer():
    def fund():
        def dpt():
            tf.destroy()
            acn= e1.get()
            pin = e2.get()
            amt =e3.get()
            acnt=e4.get()
            pn=e5.get()
            try:
                conn = pymysql.connect(host = 'localhost',user ='root',password ='',db ='atm')
                a = conn.cursor()
                a.execute("update dep set amount=amount-'"+amt+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("update dep set withdraw=withdraw+'"+amt+"'where Account_no='"+acn+"'and pin='"+pin+"'")
                a.execute("insert into detail(Account_no,pin,Withdraw)values('"+acn+"','"+pin+"','"+amt+"')")
                a.execute("update dep set amount=amount+'"+amt+"'where Account_no='"+acnt+"'")
                #a.execute("update detail set deposit=deposit+'"+amt+"'where Account_no='"+acnt+"'")
                #a.execute("update transfer set Total_amount = Total_amount+' "+amt+" ' where Account_no = ' "+acc_no+" ' and ifsc = ' "+code+" '"
                a.execute("insert into detail(Account_no,Deposit,pin)values('"+acnt+"','"+amt+"','"+pn+"')")
                conn.commit()
                messagebox.showinfo("Transfer successfully",amt)
            except:
                conn.rollback()
                messagebox.showinfo("Transfer unsuccessfull")
            conn.close()
            hd.destroy()
            
        hd=Tk()
        hd.title('Welcome to transfer page')
        hd.geometry('650x550')
        hd.resizable(False,False)
        hd.config(bg='lightgreen')
        hframe=Frame(hd,bg='lightgreen')
        hframe.pack(padx=10,pady=20)
        l1=Label(hframe,text='Enter account number from',font=('arial',20,'bold'),bg='lightgreen')
        l1.grid(row=0,column=0,padx=30,pady=20)
        acnf=StringVar()
        e1=Entry(hframe,textvariable=acnf)
        e1.grid(row=0,column=1,padx=30,pady=20)
        l2=Label(hframe,text='Enter pin',font=('arial',20,'bold'),bg='lightgreen')
        l2.grid(row=1,column=0,padx=30,pady=20)
        pin=StringVar()
        e2=Entry(hframe,show='*',textvariable=pin)
        e2.grid(row=1,column=1,padx=30,pady=20)
        l3=Label(hframe,text='Enter amount',font=('arial',20,'bold'),bg='lightgreen')
        l3.grid(row=2,column=0,padx=30,pady=20)
        amt=StringVar()
        e3=Entry(hframe,textvariable=amt)
        e3.grid(row=2,column=1,padx=30,pady=20)
        l4=Label(hframe,text='Enter account number to',font=('arial',20,'bold'),bg='lightgreen')
        l4.grid(row=3,column=0,padx=30,pady=20)
        acnt=StringVar()
        e4=Entry(hframe,textvariable=acnt)
        e4.grid(row=3,column=1,padx=30,pady=20)
        l5=Label(hframe,text='Enter IFSC',font=('arial',20,'bold'),bg='lightgreen')
        l5.grid(row=4,column=0,padx=30,pady=20)
        ifsc=StringVar()
        e5=Entry(hframe,show='*',textvariable=ifsc)
        e5.grid(row=4,column=1,padx=30,pady=20)
        btn=Button(hframe,padx=10,bd=8,fg='lightgreen',bg='black',font=('arial',20,'bold'),width=6,text='Deposited',command=dpt)
        btn.grid(row=5,column=0,padx=8,pady=10)
        
        
    tf=Tk()
    tf.title("Transfer Fund")
    tf.geometry("550x300")
    tf.resizable(False,False)
    tf.config(bg='grey')
    tframe=Frame(tf,bg='grey')
    tframe.pack(padx=10,pady=20)
    l1=Label(tframe,padx=10,text="Select the Option",font=('arial',20,'bold'),bg='grey')
    l1.grid(row=0,column=0,pady=10)
    btn1=Button(tframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="HDFC",command=fund)
    btn1.grid(row=1,column=0,padx=8,pady=10)
    btn2=Button(tframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="PNB",command=fund)
    btn2.grid(row=2,column=0,padx=8,pady=10)
    btn3=Button(tframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="STATE",command=fund)
    btn3.grid(row=1,column=1,padx=8,pady=10)
    btn4=Button(tframe,padx=10,bd=6,fg='black',font=('arial',20,'bold'),bg='lightgreen',width=6,text="ICICI",command=fund)
    btn4.grid(row=2,column=1,padx=8,pady=10)





    

