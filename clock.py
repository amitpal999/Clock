from tkinter import *
from time import * 

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string) 

    day_string = strftime("%A")
    day_label.config(text=day_string) 

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string) 

    time_label.after(1000,update)

obj= Tk()
obj.title("Amit's Clock")
obj.config(bg="light blue")
time_label= Label(obj,font=("bold",30),fg="red",bg="light green")
time_label.pack(pady=4)

day_label= Label(obj,font=("Ink Free",25),fg="black",bg="yellow")
day_label.pack(pady=6)

date_label= Label(obj,font=("Ink Free",27),fg="black",bg="pink")
date_label.pack(pady=3)

update()
obj.resizable(0,0)
obj.mainloop()