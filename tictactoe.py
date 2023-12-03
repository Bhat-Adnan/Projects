"""
Project Created By: Bhat Adnan
Dated: 25/11/2023
Project Contents: GUI Tic-tac-toe game using tkinter in python 
"""
from tkinter import *
import random as r

a = input("Enter Player One's name : ").title().strip()
b = input("Enter Player Two's name: ").title().strip()
def nextTurn(row,column):
    global player
    global cut
    
    if cells[row][column]["text"] == "" and Winner() == False:
        
        if player == players[0]:
            
            cells[row][column]["text"] = cuts[0]
            
            if Winner() is False:
                player = players[1]
                curr_Player.config(text=(players[1]+"'s turn"))
            
            elif Winner() is True:
                curr_Player.config(text=(players[0] + " has Won!"))
            
            elif Winner() == "Draw":
                for row in range(3):
                    for column in range(3):
                        cells[row][column].config(text=(game_over[0]),bg="red",fg="white")
                curr_Player.config(text=("It is a Draw!"))

        else:
            
            cells[row][column]["text"] = cuts[1]
            
            if Winner() is False:
                player = players[0]
                curr_Player.config(text=(players[0] + "'s turn"))
            
            elif Winner() is True:
                curr_Player.config(text=(players[1] + " has Won!" ))
            
            elif Winner() == "Draw":
                for row in range(3):
                    for column in range(3):
                        cells[row][column].config(text=(game_over[0]),bg="red",fg="white")
                curr_Player.config(text=("It is a Draw!"))

def Winner():
    for row in range(0,3,1):
        if cells[row][0]["text"] == cells[row][1]["text"] == cells[row][2]["text"] != "":
            cells[row][0].config(bg="#7b03fc")
            cells[row][1].config(bg="#7b03fc")
            cells[row][2].config(bg="#7b03fc")
            return True
    for column  in range(0,3,1):
        if cells[0][column]["text"] == cells[1][column]["text"] == cells[2][column]["text"] != "":
            cells[0][column].config(bg="#03d3fc")           #colours selected using color picker 
            cells[1][column].config(bg="#03d3fc")
            cells[2][column].config(bg="#03d3fc")
            return True
    if cells[0][0]["text"] ==  cells[1][1]["text"] == cells[2][2]["text"] != "":
        cells[0][0].config(bg="#ecfc03")
        cells[1][1].config(bg="#ecfc03")
        cells[2][2].config(bg="#ecfc03")
        return True
    elif cells[0][2]["text"] == cells[1][1]["text"] == cells[2][0]["text"] != "":
        cells[0][2].config(bg="#ecfc03")
        cells[1][1].config(bg="#ecfc03")
        cells[2][0].config(bg="#ecfc03")
        return True
    elif emptySpaces() == False:
        return "Draw"                
    else:
        return False
        
        
def emptySpaces():
    spacesleft = 9
    for row in range(3):
        for column in range(3):
            if cells[row][column]["text"] != "":
                spacesleft -= 1
    
    if spacesleft == 0:
        return False
    else:
        return True
             
def restartGame():
    global player
    gameCounter()
    player = r.choice(players)
    cut = r.choice(cuts)
    curr_Player.config(text =(player + "'s turn"))
    for row in range(3):
        for column in range(3):
            cells[row][column].config(text="",bg="#f0f0f0",fg="black")

def gameCounter():
    game.counter += 1
    counter_label.config(text=("Times Played: "+str(game.counter)),fg="green")
    
     
game = Tk()
game.title("Tic Tac Toe")
game.geometry("500x600")
game.resizable(False,False)
game.counter = 0
players = [a,b]
cuts = ["X","O"]
cut = r.choice(cuts)
game_over=["Game\nOver!"]
player = r.choice(players)
cells = [[0,0,0],
         [0,0,0],
         [0,0,0]]

counter_label = Label(text="First Game!",font=("B612 Mono",18),fg="green")
counter_label.pack(side="top", expand=True, fill=X)
curr_Player = Label(text=player + "'s turn", font=("B612 Mono",40))
curr_Player.pack(side="top")
format_label = Label(text="",height = 3)
format_label.pack(side="bottom")
made_By = Label(text="Made By Bhat Adnan",font=("B612 Mono",15))
made_By.pack(side ="bottom",fill=X,expand=True) 
reset = Button(text="Restart Game",font=("B612 Mono",15),command=restartGame,width=12,height=1,bg="blueviolet")
reset.pack(side="bottom")
format1_label = Label(text="",height = 2)
format1_label.pack(side="bottom")



frame = Frame(game,highlightbackground="black",highlightthickness=1)
frame.pack()
for row in range(0,3,1):
    for column in range(0,3,1):
        cells[row][column] = Button(frame, text="",font=("B612 Mono",15),width=8,height=4,
                                    command= lambda row=row, column=column: nextTurn(row, column))
        cells[row][column].grid(row=row,column=column)


game.mainloop()