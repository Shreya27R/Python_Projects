from tkinter import *
from plyer import notification
from PIL import Image ,ImageTk
from tkinter import messagebox
import time

root = Tk()
root.title("Notifier-APP")
root.geometry("500x300")
img = Image.open("Notifier.png")
resized_image= img.resize((100,80), Image.LANCZOS)
tkimage=ImageTk.PhotoImage(resized_image)

#get details

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time =time1.get()
    #validation
    if get_title == '' or get_msg =='' or get_time =='':
        messagebox.showerror("Alert, all fields are required")
    else:
        int_time = int(float(get_time))
        min_to_sec =int_time*60
        messagebox.showinfo("notifier set","set notification?")
        #The screen will disappear once clicked okay
        root.destroy()
        time.sleep(min_to_sec)
        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="notification",
                            app_icon="ico.ico",
                            timeout=10)

img_label =Label(root,image=tkimage).grid()

#Label 1
label = Label(root,text="Title to notify", font=("poppins",10))
label.place(x=12,y=75)

#Entry 1
title = Entry(root ,width="25",font=("poppins",10))
title.place(x=123,y=78)

#lable_2
m_label = Label(root,text="Display Message", font=("poppins",10))
m_label.place(x=12,y=128)

#Entry 2
msg = Entry(root ,width="40",font=("poppins",10))
msg.place(x=123,y=128,height=30)


#label-3
time_label = Label(root,text="Set time", font=("poppins",10))
time_label.place(x=12,y=175)

#Entry 3
time1 = Entry(root ,width="5",font=("poppins",10))
time1.place(x=123,y=175)


#label 4
time_min_label = Label(root ,text="min",font=("poppins",10))
time_min_label.place(x=178,y=175)

#button_1

button =Button(root,text="SET-NOTIFICATION",font=("poppins",10,'bold'),fg="#ffffff",bg="#528DFF",width=20,relief="raised",
command=get_details)
button.place(x=170,y=230)




#root.resizable(0,0)
root.mainloop()
