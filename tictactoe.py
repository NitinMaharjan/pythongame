from tkinter import *
import random


def next_turn(row , column):
    global player
    if button[row][column]["text"]=="" and check_winner() is False:
        if player == players[0] :
            button[row][column]["text"]=player
            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            elif check_winner() == "tie":
                label.config(text=("Tie"))
        else:
            button[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "tie":
                label.config(text=("Tie"))




def check_winner():
    for row in range(3):
        if button[row][0]["text"] == button[row][1]["text"] ==button[row][2]["text"] != "":
            button[row][0].config(bg="green")
            button[row][1].config(bg="green")
            button[row][2].config(bg="green")
            return True
    for column in range(3):
        if button[0][column]["text"] == button[1][column]["text"] ==button[2][column]["text"] != "":
            button[0][column].config(bg="green")
            button[1][column].config(bg="green")
            button[2][column].config(bg="green")
            return True
    if button[0][0]["text"]==button[1][1]["text"]==button[2][2]["text"]!="":
        button[0][0].config(bg="green")
        button[1][1].config(bg="green")
        button[2][2].config(bg="green")
        return True
    if button[0][2]["text"]==button[1][1]["text"]==button[2][0]["text"]!="":
        button[0][2].config(bg="green")
        button[1][1].config(bg="green")
        button[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        return "tie"
    else :
        return False

def empty_spaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if button[row][column]["text"]!="":
                spaces-=1

    if spaces==0:
        return False


def new_game():
    global player
    player = random.choice(players)
    label.config(text=(player)+" turn")
    for row in range(3):
        for column in range(3):
            button[row][column].config(text="", bg="#f0f0f0")


window = Tk() #hivcgbhjh
window.title("tictactoe")
players = ["X", "O"]
player = random.choice(players)
button = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
label = Label(text=player + " turn", font=("timesnewroman", 40))
label.pack(side="top")

reset_button = Button(text="reset", font=("timesnewroman", 20), command=new_game)
reset_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        button[row][column] = Button(frame, text="", font=("timesnewroman", 40), width=5, height=2,
                                     command=lambda row= row, column= column: next_turn(row, column))
        button[row][column].grid(row=row, column=column)
window.mainloop()
