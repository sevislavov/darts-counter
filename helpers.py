#TODO double out
#TODO del button fix with overthrow
#TODO del button cant go over limit (101, 501....)
#TODO del button switches to the other person
#TODO fix error messages when pressing non int buttons

import tkinter as tk 
import constants as c

count = 0
inside_count = 0
player_scores = [101, 101]
current_player = 0
player_entries = []
lst_1 = []
lst_2 = []
current_throws = []
score_checker_1 = []
score_checker_2 = []
double_pressed = False
tripple_pressed = False
del_counter = 0

def collect(value):
    global count, current_player, player_scores, double_pressed, tripple_pressed, inside_count, del_counter
    players = ["Player 1", "Player 2"]
    # DOUBLE AND TRIPPLE BUTTON LOGIC
    if value == "DOUBLE":
        double_pressed = True
    else:
        if double_pressed:
            value *=2
            double_pressed = False
    
    if value == "TRIPPLE":
        tripple_pressed= True
    else:
        if tripple_pressed:
            if value == 25:
                tripple_pressed= False
                return 25
            else:
                value *=3
                tripple_pressed = False

    if value == "DEL":
        delete()
                
    previous_score = player_scores[current_player]   
    player_scores[current_player] -= value
    current_throws.append(value)
    first_1.config(fg="black") or first_2.config(fg="black") or first_3.config(fg="black") 
    second_1.config(fg="black") or second_2.config(fg="black") or second_3.config(fg="black")

    if player_scores[current_player] < 0 or player_scores[current_player] == 1:
        if current_player == 0:
            if count == 0:
                first_1.config(fg="red")
             
            elif count == 1:
                first_2.config(fg="red")
             
            else:
                first_3.config(fg="red") 
        else:
            if count == 0:
                second_1.config(fg="red")
         
            elif count == 1:
                second_2.config(fg="red")
               
            else:
                second_3.config(fg="red")

        player_scores[current_player] = previous_score
        current_throws.pop()

        update_entries(current_player, value)
        switch_player(True)
        return
    
    elif player_scores[current_player] == 0:
        print(f"Player {current_player + 1} wins!")
        reset_game()
        return
    update_entries(current_player, value)
    update_score()

    count +=1
    if count % 3 == 0:
        switch_player(False) 
    print("outside" + str(count))

def delete():
    global current_player, count, current_throws, dell

    if current_player == 0:
        if count == 0:
            print(count)
            count = 3
            current_player = 1
            second_3.delete(0, tk.END)
            lst_2.pop(-1)
            player_scores[1] += current_throws[-1]
            current_throws.pop(-1)
            player_entries[1].delete(0, tk.END)     
            player_entries[1].insert(0, str(player_scores[0]))
            count -= 1
        else:
            player_scores[0] += current_throws[-1]
            current_throws.pop(-1)
            player_entries[0].delete(0, tk.END)
            player_entries[0].insert(0, str(player_scores[0]))

            if count == 1:
                first_1.delete(0, tk.END)
                lst_1.pop(-1)
                count -= 1
            elif count == 2:
                first_2.delete(0, tk.END)
                lst_1.pop(-1)
                count -= 1
            elif count == 3:
                first_3.delete(0, tk.END)
                lst_1.pop(-1)
                count -= 1

    else:
        if count == 0 and current_player == 1:
            count = 3
            current_player = 0
            first_3.delete(0, tk.END)
            lst_1.pop(-1)
            player_scores[0] += current_throws[-1]
            current_throws.pop(-1)
            player_entries[0].delete(0, tk.END)     
            player_entries[0].insert(0, str(player_scores[0]))
            count -= 1
        else:
            player_scores[1] += current_throws[-1]
            current_throws.pop(-1)
            player_entries[1].delete(0, tk.END)
            player_entries[1].insert(0, str(player_scores[1]))

            if count == 1:
                second_1.delete(0, tk.END)
                lst_2.pop(-1)
                count -= 1

            elif count == 2:
                second_2.delete(0, tk.END)
                lst_2.pop(-1)
                count -= 1
            else:
                second_3.delete(0, tk.END)
                lst_2.pop(-1)
                count -= 1
                
def switch_player(after_throw):
    global current_player, count
    current_player = 1 - current_player  # Toggle between 0 and 1
    count = 0

def update_score():
    player_entries[current_player].delete(0, tk.END)
    player_entries[current_player].insert(0, str(player_scores[current_player]))

def reset_game():
    global player_scores, lst_1, lst_2, current_throws, current_player, count
    player_scores = [101, 101]
    lst_1.clear()
    lst_2.clear()
    current_throws.clear()
    current_player = 0
    count = 0
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    first_entry.insert(0, str(101))
    second_entry.insert(0, str(101))
    first_1.delete(0, tk.END)
    first_2.delete(0, tk.END)
    first_3.delete(0, tk.END)
    second_1.delete(0, tk.END)
    second_2.delete(0, tk.END)
    second_3.delete(0, tk.END)

def update_entries(player, value):
    if player == 0:
        lst_1.append(value)
        print(f"lst_1: {lst_1}")
        try: 
            
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

def body():
    global x_axis, first_1, player_entries, first_2, first_3
    global second_1, second_2, second_3, first_entry, second_entry
    global bull, dell
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

    bull = tk.Button(text=25, width=7, height=3, command=lambda j=j:collect(25)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="DBLE", width=7, height=3,command=lambda j=j: collect("DOUBLE")).place(x=dx_axis+c.x_shift, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text=0, width=7, height=3,command=lambda j=j: collect(0)).place(x=c.mx-60, y=(c.my+(3*(c.y_shift)))-25)
    tk.Button(text="TRPLE", width=7, height=3,command=lambda j=j: collect("TRIPPLE")).place(x=(dx_axis+c.x_shift)+c.x_shift, y=c.my+(2*(c.y_shift)), anchor="w")

    dell = tk.Button(text="DEL", width=7, height=3, command=lambda j=j: collect("DEL")).place(x=c.mx+30, y=c.my+(3*(c.y_shift)+2), anchor="center")

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