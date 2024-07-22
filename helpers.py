import tkinter as tk 
import constants as c

starting_score = int(input("Please enter the amount of points you would like to start on>  "))
straight_or_double = int(input("For straight out press 0 for double out press 1> "))
player_one = str(input("Please enter your name Player 1> "))
player_two = str(input("Please enter your name Player 2> "))

count = 0
inside_count = 0
player_scores = [starting_score, starting_score]
current_player = 0
player_entries = []
lst_1 = []
lst_2 = []
current_throws = []
score_checker_1 = []
score_checker_2 = []
double_pressed = False
tripple_pressed = False
delete_pressed = False
del_counter = 0
last_throw_was_double = False

def collect(value):
    global count, current_player, player_scores, double_pressed, tripple_pressed, inside_count, del_counter
    global last_throw_was_double
    last_throw_was_double = False

    # DOUBLE AND TRIPPLE BUTTON LOGIC

    if value == "DOUBLE":
        double_pressed = True
    else:
        if double_pressed:
            value *=2
            double_pressed = False
            last_throw_was_double = True

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

    first_1.config(fg="#5bffd3") or first_2.config(fg="#5bffd3") or first_3.config(fg="#5bffd3") 
    second_1.config(fg="#5bffd3") or second_2.config(fg="#5bffd3") or second_3.config(fg="#5bffd3")

    #CHANGE THE COLOR OF THE TURN WHEN AN OVERTHROW HAPPENS

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
    
    elif player_scores[current_player] == 0 and straight_or_double == 0:
        print(f"Player {current_player + 1} wins!")
        reset_game()
        return
    
    elif player_scores[current_player] == 0 and straight_or_double == 1 and last_throw_was_double:
        print(f"Player {current_player + 1} wins with a double out!")
        reset_game()
        return
    elif player_scores[current_player] == 0 and not last_throw_was_double:
        # If player hits zero without a double, revert the score
        player_scores[current_player] = previous_score
        current_throws.pop()
        update_entries(current_player, value)
        switch_player(True)
        return
    
    update_entries(current_player, value)
    update_score()

    count +=1
    if count % 3 == 0:
        switch_player(False) 
    print("outside" + str(count))

def delete():
    # DELETE LAST TURN
    global current_player, count, current_throws, dell, delete_pressed
    delete_pressed = True
    if current_player == 0:
        if count == 0 and delete_pressed:
            current_player = 1
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
        if count == 0:
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
    # Update big entry widgets 
    player_entries[current_player].delete(0, tk.END)
    player_entries[current_player].insert(0, str(player_scores[current_player]))

def reset_game():
    # Reset game after a leg is won
    global player_scores, lst_1, lst_2, current_throws, current_player, count
    player_scores = [starting_score, starting_score]
    lst_1.clear()
    lst_2.clear()
    current_throws.clear()
    current_player = 0
    count = 0
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    first_entry.insert(0, str(starting_score))
    second_entry.insert(0, str(starting_score))
    first_1.delete(0, tk.END)
    first_2.delete(0, tk.END)
    first_3.delete(0, tk.END)
    second_1.delete(0, tk.END)
    second_2.delete(0, tk.END)
    second_3.delete(0, tk.END)

def update_entries(player, value):
    # Update smaller entry box widgets
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
    # GUI and design
    global x_axis, first_1, player_entries, first_2, first_3
    global second_1, second_2, second_3, first_entry, second_entry
    global bull, dell
    root = tk.Tk()
    root.geometry("480x853")
    root.title("Darts Counter")
    x_axis = 0
    dx_axis = 0

    bg = tk.PhotoImage(file="assets/other/background.png")
    one_png = tk.PhotoImage(file="assets/nums/one.png")
    two_png = tk.PhotoImage(file="assets/nums/two.png")
    three_png = tk.PhotoImage(file="assets/nums/three.png")
    four_png = tk.PhotoImage(file="assets/nums/four.png")
    five_png = tk.PhotoImage(file="assets/nums/five.png")
    six_png = tk.PhotoImage(file="assets/nums/six.png")
    seven_png = tk.PhotoImage(file="assets/nums/seven.png")
    eight_png = tk.PhotoImage(file="assets/nums/eight.png")


    nine_png = tk.PhotoImage(file="assets/nums/nine.png")
    ten_png = tk.PhotoImage(file="assets/nums/ten.png")
    eleven_png = tk.PhotoImage(file="assets/nums/eleven.png")
    twelve_png = tk.PhotoImage(file="assets/nums/twelve.png")
    thirteen_png = tk.PhotoImage(file="assets/nums/thirteen.png")
    fourteen_png = tk.PhotoImage(file="assets/nums/fourteen.png")
    fifteen_png = tk.PhotoImage(file="assets/nums/fifteen.png")
    sixteen_png = tk.PhotoImage(file="assets/nums/sixteen.png")

    seventeen_png = tk.PhotoImage(file="assets/nums/seventeen.png")
    eighteen_png = tk.PhotoImage(file="assets/nums/eighteen.png")
    nineteen_png = tk.PhotoImage(file="assets/nums/nineteen.png")
    twenty_png = tk.PhotoImage(file="assets/nums/twenty.png")
    bullseye = tk.PhotoImage(file="assets/nums/twentyfive.png")
    zero = tk.PhotoImage(file="assets/nums/zero.png")

    double = tk.PhotoImage(file="assets/other/double.png")
    triple = tk.PhotoImage(file="assets/other/triple.png")
    del_ = tk.PhotoImage(file="assets/other/del.png")
    quit_ = tk.PhotoImage(file="assets/other/quit.png")


    background_label = tk.Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    nums_1 = [
        one_png, two_png, three_png, four_png, five_png, six_png, seven_png, eight_png
    ]

    nums_2 = [
        nine_png, ten_png, eleven_png, twelve_png, thirteen_png, fourteen_png, fifteen_png, sixteen_png
    ]

    nums_3 = [
        seventeen_png, eighteen_png, nineteen_png, twenty_png
    ]
    #BUTTON LAYOUT
    try:
        for i in range(9):
            tk.Button(text=i+1, image=nums_1[i], border=0, borderwidth=3, command=lambda i=i: collect(i+1)).place(x=x_axis, y=c.my, anchor="w")
            tk.Button(text=i+9, image=nums_2[i], border=0, borderwidth=3, command=lambda i=i: collect(i+9)).place(x=x_axis, y=c.my+c.y_shift, anchor="w")
            x_axis += c.x_shift
    except IndexError:
        pass 

  
    for j in range(4):
        tk.Button(text=j+17, image=nums_3[j], border=0, borderwidth=3, command=lambda j=j: collect(j+17)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
        dx_axis += c.x_shift
   

    bull = tk.Button(text=25, image=bullseye, border=0, borderwidth=3, command=lambda j=j:collect(25)).place(x=dx_axis, y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="DBLE", image=double, border=0, borderwidth=3, command=lambda j=j: collect("DOUBLE")).place(x=dx_axis+2*(c.x_shift), y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text=0, image=zero, border=0, borderwidth=3, command=lambda j=j: collect(0)).place(x=dx_axis+(c.x_shift), y=c.my+(2*(c.y_shift)), anchor="w")
    tk.Button(text="TRPLE", image=triple, border=0, borderwidth=3, command=lambda j=j: collect("TRIPPLE")).place(x=(dx_axis+c.x_shift)+2*(c.x_shift), y=c.my+(2*(c.y_shift)), anchor="w")

    dell = tk.Button(text="DEL", image=del_,  border=0, borderwidth=3, command=lambda j=j: collect("DEL")).place(x=c.mx, y=c.my+(3*(c.y_shift)+2), anchor="center")

    # PLAYER 1 LAYOUT
    
    tk.Label(text=player_one, font="Ariel, 25", bg="#1c2143", fg="#5bffd3").place(x=10, y=10)

    first_entry = tk.Entry(width=10,font="Ariel, 25", bg="#1c2143", bd=3, fg="#5bffd3")
    first_entry.place(x=c.mx, y=10)
    first_entry.insert(0, str(starting_score))
    player_entries.append(first_entry)


    first_1 = tk.Entry(width=3, font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    first_1.place(x=c.mx, y=60)

    first_2 = tk.Entry(width=3, font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    first_2.place(x=c.mx+65, y=60)
    
    first_3 = tk.Entry(width=3, font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    first_3.place(x=(c.mx+65)+65, y=60)

    # PLAYER 2 LAYOUT

    tk.Label(text=player_two, font="Ariel, 25", bg="#1c2143", fg="#5bffd3").place(x=10, y=120)

    second_entry = tk.Entry(width=10,font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    second_entry.place(x=c.mx, y=120)
    second_entry.insert(0, str(starting_score))
    player_entries.append(second_entry)


    second_1 = tk.Entry(width=3, font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    second_1.place(x=c.mx, y=170)
    
    second_2 = tk.Entry(width=3, font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    second_2.place(x=c.mx+65, y=170)
    
    second_3 = tk.Entry(width=3, font="Ariel, 25", bg="#1c2143", fg="#5bffd3")
    second_3.place(x=(c.mx+65)+65, y=170)

    tk.Button(text="Quit", image=quit_, command=root.destroy).place(x=c.mx, y=c.height-100, anchor="center")

    root.mainloop()