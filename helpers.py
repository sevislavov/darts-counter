import tkinter as tk 
import constants as c

def collect():
    pass 

def body():
    global i
    root = tk.Tk()
    root.geometry("480x960")
    j = 0
    i = 0
    for i in range(9):
        tk.Button(text=i+1, width=7, height=3,command=collect).place(x=j, y=c.my, anchor="w")
        j += 60
    root.mainloop()