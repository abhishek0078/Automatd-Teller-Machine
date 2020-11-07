from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import os
def mini():
    def show():
        
        acn=e1.get()
        pin=e2.get()
        conn=pymysql.connect(host="localhost",user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("select *from detail where Account_no='"+acn+"'and pin='"+pin+"'")
        #a.execute("select *from detail")
        var=a.fetchall()
        count=a.rowcount
        a.execute("select *from dep where Account_no='"+acn+"'and pin='"+pin+"'")
        nm=a.fetchall()
        num=4
        sw=Tk()
        mi.destroy()
        sw.title('Customer Details')
        w, h = sw.winfo_screenwidth(), sw.winfo_screenheight()
        sw.geometry("%dx%d+0+0" % (w, h))
        sw.config(bg='lightgreen')
        #sw.resizable(False,False)
        cd=Frame(sw,bg='lightgreen')
        cd.pack()
        if(count>0):
            #text=Text(cd,font="vendata 15",width=80,height=count+3,bg='lightgreen')
            text=Text(cd,font=("vendata",15,'bold'),width=70)
            headlb=Label(cd,text="CUSTOMER DETAILS",font=('vendata',20,'bold'),width=40,bg='black',fg='white')
            headlb.grid(row=1,padx=10,pady=10)
            text.insert(END,"\nName\t\tContact\t\tTotal Amount\n")
            text.grid(row=num,column=0)
            for i in nm:
                text.insert(END,"\n{0}\t\t{1}\t\t{2}\n--------------------------------------------------------------------------------------------------------".format(i[0],i[1],i[2]))
            text.insert(END,"\nAccount No\t\tDeposit\t\tWithdraw\t\tTime\n--------------------------------------------------------------------------------------------------------")
            text.grid(row=num,column=0)
            for i in var:
                text.insert(END,"\n\n{0}\t\t{1}\t\t{2}\t\t{3}".format(i[0],i[1],i[2],i[3]))
                num+=1
        else:
            messagebox.showinfo("Msg","Invalid AccountNo/Pin")

    mi=Tk()
    mi.title('Welcome to main page')
    mi.geometry('400x230')
    mi.config(bg='lightgreen')
    mi.resizable(False,False)
    mframe=Frame(mi,bg='lightgreen')
    mframe.pack(pady=15)
    l1=Label(mframe,text='Enter Account No.',font=('arial',20,'bold'),bg='lightgreen')
    l1.grid(row=0,column=0,pady=10)
    acn=StringVar()
    e1=Entry(mframe,textvariable=acn)
    e1.grid(row=0,column=1,pady=10)
    l2=Label(mframe,text='Enter Pin',font=('arial',20,'bold'),bg='lightgreen',fg='black')
    l2.grid(row=1,column=0,pady=10)
    pin=StringVar()
    e2=Entry(mframe,show='*',textvariable=pin)
    e2.grid(row=1,column=1,pady=10)
    btn=Button(mframe,padx=10,bd=6,bg='black',fg='lightgreen',font=('arial',15,'bold'),width=6,text='Show',command=show)
    btn.grid(row=2,column=0,pady=10)
    mi.mainloop()

