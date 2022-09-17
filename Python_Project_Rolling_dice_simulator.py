
#!/usr/bin/env python3
import random
from tkinter import *

root = Tk() #referes to tkinter window
root.geometry("600x600")

label = Label(root,text='',font=("arial",300))
label_desc = Label(root,text='',font=("arial",10))

def roll_the_dice():
    value =['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
    result= random.choice(value)
    label.configure(text=result)
    label.pack()
    if result =='\u2680':
        label_desc.configure(text='You rolled One! Roll the dice again')
        label_desc.place(x=200,y=450)
    elif result =='\u2681':
        label_desc.configure(text='You rolled Two! Roll the dice again')
        label_desc.place(x=200,y=450)
    elif result =='\u2682':
        label_desc.configure(text='You rolled Three! Roll the dice again')
        label_desc.place(x=200,y=450)
    elif result =='\u2683':
        label_desc.configure(text='You rolled Four! Roll the dice again')
        label_desc.place(x=200,y=450)
    elif result =='\u2684':
        label_desc.configure(text='You rolled Five! Roll the dice again')
        label_desc.place(x=200,y=450)
    else:
        label_desc.configure(text='You rolled Six! Roll the dice again')
        label_desc.place(x=200,y=450)



button_1 =Button(root,text="Roll the dice",command=roll_the_dice)
button_1.place(x=250,y=0)


root.mainloop()
