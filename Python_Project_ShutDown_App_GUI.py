from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1") #1 sec
def restart_time():
    os.system("shutdown /r /t 20") # restarts in 20sec
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1 ")


#create a object st call Tk() class
root = Tk()
root.title("ShutDown-App")
root.geometry("500x500")
root.config(bg="Blue")

r_button = Button(root,text="Restart",font=("Time New Roman", 20,"bold"),
relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(root,text="Restart time",font=("Time New Roman",20,"bold")
,relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lt_button = Button(root,text="Log Off",font=("Time New Roman",20,"bold"),
relief=RAISED,cursor="plus",command=logout)
lt_button.place(x=150,y=270,height=50,width=200)

St_button = Button(root,text="ShutDown",font=("Time New Roman",20,"bold"),
relief=RAISED,cursor="plus",command=shutdown)
St_button.place(x=150,y=370,height=50,width=200)

root.mainloop()
