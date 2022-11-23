from tkinter import *
from tkinter import messagebox
import tkinter
import openpyxl,xlrd
from openpyxl import Workbook
import os
import pandas as pd
#import numpy as np


MsgBox=messagebox.askquestion("askquestion", "Hello Shreyaa! Have any expense Today ? Then note down the Expense")
if MsgBox=='yes':
    root=Tk()
    root.title('Expenses App')
   # root.configure(background='white')
    root.geometry('400x390')
    frame = tkinter.Frame(root)
    frame.pack()
else:
    messagebox.showinfo("Close Application", "Closing the Application! bye bye")
    root=Tk()
    root.destroy()


def add_data():
    get_year = year.get()
    get_month = month.get().upper()
    get_reason= reason.get().upper()
    get_amount= amount.get()

     #validation
    if get_year == '' or get_month== '' or get_reason == '' or get_amount == '':
        messagebox.showerror("Error", "Error : All fields are required")
    else:
        print("Year: ", get_year, "Month: ", get_month)
        print("reason: ", get_reason, "amount: ", get_amount)
        print("------------------------------------------")

        filepath = r"C:\Users\SHREYA\Desktop\Python\Bash_learning" + "\\" + get_month + "_" +get_year+ ".xlsx"
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["Year", "Month", "Reason", "Amount"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([get_year, get_month, get_reason, get_amount])
        workbook.save(filepath)

#Reset the tab value/clear the values

def clear_data():
    year.delete("0","end")
    month.delete("0","end")
    reason.delete("0","end")
    amount.delete("0","end")

def continue_adding():
    reason.delete("0","end")
    amount.delete("0","end")

def add_amount():
    get_year = year.get()
    get_month = month.get()
    filepath = r"C:\Users\SHREYA\Desktop\Python\Bash_learning" + "\\" + get_month + "_" + get_year+ ".xlsx"
    df = pd.read_excel(filepath)
    Amount=df["Amount"].sum()
    messagebox.showinfo("showinfo", "Total expense for "+ get_month + " is : Rs." + str(Amount))
    #print("Sum: ",df["Amount"].sum())



#design code below
heading=Label(root,text="Note down your monthly expense and Get total expense",font=("poppins",10))
heading.place(x=32,y=28)
year_label=Label(root,text="Year",font=("poppins",10))
year_label.place(x=12,y=78)

year = Entry(root ,width="25",font=("poppins",10))
year.place(x=123,y=78)


month_label=Label(root,text="Month",font=("poppins",10))
month_label.place(x=12,y=128)

month = Entry(root ,width="25",font=("poppins",10))
month.place(x=123,y=128)

Reason_label=Label(root,text="Amount Spent for",font=("poppins",10))
Reason_label.place(x=12,y=178)
reason = Entry(root ,width="25",font=("poppins",10))
reason.place(x=123,y=178)

Amount_label=Label(root,text="Amount in Rs :",font=("poppins",10))
Amount_label.place(x=12,y=220)
amount = Entry(root ,width="25",font=("poppins",10))
amount.place(x=123,y=220)

button =Button(root,text="Enter",font=("poppins",10,'bold'),fg="#ffffff",bg="#528DFF",width=5,relief="raised",command=add_data)
button.place(x=123,y=280)
button =Button(root,text="Continue",font=("poppins",10,'bold'),fg="#ffffff",bg="#528DFF",width=7,relief="raised",command=continue_adding)
button.place(x=190,y=280)
button =Button(root,text="Reset",font=("poppins",10,'bold'),fg="#ffffff",bg="#528DFF",width=5,relief="raised",command=clear_data)
button.place(x=270,y=280)
button =Button(root,text="Get total Amount",font=("poppins",10,'bold'),fg="#ffffff",bg="#528DFF",width=21,relief="raised",command=add_amount)
button.place(x=123,y=330)

# TAmount_label=Label(root,text="Get Total amount",font=("poppins",10))
# TAmount_label.place(x=12,y=380)
# Tamount = Entry(root ,width="25",font=("poppins",10),state=DISABLED)
# Tamount.place(x=123,y=380)


root.mainloop()
