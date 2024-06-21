# next commit - add error handling and worked on game logic

import tkinter as tk 
import constants as c

count = 0
player_scores = [501, 501]
current_player = 0
player_entries = []
lst_1 = []
lst_2 = []
score_checker_1 = []
score_checker_2 = []
double_pressed = False
tripple_pressed = False


def collect(value):
    global count, current_player, player_scores, double_pressed, tripple_pressed
    players = ["Player 1", "Player 2"]

    if value == "DOUBLE":
        double_pressed = True
    else:
        if double_pressed:
            value *=2
            count -=1
            double_pressed = False
    if value == 25:
        return value
    else:
        if value == "TRIPPLE":
            tripple_pressed= True
        else:
            if tripple_pressed:
                value *=3
                count -=1
                tripple_pressed = False
    count +=1
    player_scores[current_player] -= value 
    player_entries[current_player].delete(0, tk.END)
    player_entries[current_player].insert(0, str(player_scores[current_player]))

    # SMALL ENTRY WIDGETS INSERT SCORE AND UPDATE
    if current_player == 0:
        try: 
            lst_1.append(value)

            first_1.insert(0, str(lst_1[0]))
            lst_1[0] = ""
            lst_2.clear()
            second_1.delete(0,tk.END)
            second_2.delete(0,tk.END)
            second_3.delete(0,tk.END)
            first_2.insert(0, str(lst_1[1]))
            lst_1[1] = ""
        
            first_3.insert(0, str(lst_1[2]))
            lst_1[2] = ""
        except IndexError: 
            pass
    else:
        try:
            lst_2.append(value)
            second_1.insert(0, str(lst_2[0]))
            lst_2[0] = ""
            lst_1.clear()
            first_1.delete(0,tk.END)
            first_2.delete(0,tk.END)
            first_3.delete(0,tk.END)
            second_2.insert(0, str(lst_2[1]))
            lst_2[1] = ""
            second_3.insert(0, str(lst_2[2]))
            lst_2[2] = ""
        except IndexError:
            pass 
    
    if count % 3 == 0:
        current_player = 1 - current_player  # Toggle between 0 and 1

    # print(f"{players[current_player]}'s turn")


def body():
    global x_axis, first_1, player_entries, first_2, first_3
    global second_1, second_2, second_3, first_entry, second_entry
    root = tk.Tk()
    root.geometry("480x700")
    root.title("Darts Counter")
    x_axis = 0
    dx_axis = 0

    #BUTTON LAYOUT
    try:
        for i in range(9):
            tk.Button(text=i+1, width=7, height=3,command=lambda i=i: collect(i+1)).place(x=x_axis, y=c.my, anchor="w")
            tk.Button(text=i+8, width=7, height=3,command=lambda i=i: collect(i+8)).place(x=x_axis, y=c.my+c.y_shift, anchor="w")
            x_axis += c.x_shift
    except IndexError:
        pass 

    for j in range(5):
        tk.Button(text=j+16, width=7, height=3,command=lambda j=j: collect(j+16)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
        dx_axis += c.x_shift

    tk.Button(text=25, width=7, height=3,command=lambda j=j: collect(25)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="DBLE", width=7, height=3,command=lambda j=j: collect("DOUBLE")).place(x=dx_axis+c.x_shift, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="TRPLE", width=7, height=3,command=lambda j=j: collect("TRIPPLE")).place(x=(dx_axis+c.x_shift)+c.x_shift, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="DEL", width=8, height=3,command=lambda j=j: collect("DEL")).place(x=c.mx, y=c.my+(3*(c.y_shift)+2), anchor="center")
    
    # PLAYER 1 LAYOUT
    tk.Label(text="Player 1", font="Ariel, 25").place(x=10, y=10)

    first_entry = tk.Entry(width=10,font="Ariel, 25")
    first_entry.place(x=c.mx, y=10)
    first_entry.insert(0, str("501"))
    player_entries.append(first_entry)


    first_1 = tk.Entry(width=3, font="Ariel, 25")
    first_1.place(x=c.mx, y=60)

    first_2 = tk.Entry(width=3, font="Ariel, 25")
    first_2.place(x=c.mx+65, y=60)
    
    first_3 = tk.Entry(width=3, font="Ariel, 25")
    first_3.place(x=(c.mx+65)+65, y=60)

    # PLAYER 2 LAYOUT

    tk.Label(text="Player 2", font="Ariel, 25").place(x=10, y=120)

    second_entry = tk.Entry(width=10,font="Ariel, 25")
    second_entry.place(x=c.mx, y=120)
    second_entry.insert(0, str("501"))
    player_entries.append(second_entry)


    second_1 = tk.Entry(width=3, font="Ariel, 25")
    second_1.place(x=c.mx, y=170)
    
    second_2 = tk.Entry(width=3, font="Ariel, 25")
    second_2.place(x=c.mx+65, y=170)
    
    second_3 = tk.Entry(width=3, font="Ariel, 25")
    second_3.place(x=(c.mx+65)+65, y=170)

    tk.Button(width=10,text="Quit", command=root.destroy).place(x=c.mx, y=c.height-100, anchor="center")

    root.mainloop()