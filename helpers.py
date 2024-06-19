import tkinter as tk 
import constants as c

def collect(value):
    print(value)

def body():
    global x_axis
    root = tk.Tk()
    root.geometry("480x700")
    root.title("Darts Counter")
    x_axis = 0
    dx_axis = 0

    for i in range(9):
        tk.Button(text=i+1, width=7, height=3,command=lambda i=i: collect(i+1)).place(x=x_axis, y=c.my, anchor="w")
        tk.Button(text=i+8, width=7, height=3,command=lambda i=i: collect(i+8)).place(x=x_axis, y=c.my+c.y_shift, anchor="w")
        x_axis += c.x_shift

    for j in range(5):
        tk.Button(text=j+16, width=7, height=3,command=lambda j=j: collect(j+16)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
        dx_axis += c.x_shift

    tk.Button(text=25, width=7, height=3,command=lambda j=j: collect(j+16)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="DBLE", width=7, height=3,command=lambda j=j: collect("DOUBLE")).place(x=dx_axis+c.x_shift, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="TRPLE", width=7, height=3,command=lambda j=j: collect("TRPLE")).place(x=(dx_axis+c.x_shift)+c.x_shift, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="DEL", width=8, height=3,command=lambda j=j: collect("DEL")).place(x=c.mx, y=c.my+(3*(c.y_shift)+2), anchor="center")
   
   

    root.mainloop()