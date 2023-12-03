"""
Project Created By: Bhat Adnan
Dated: 25/11/2023
Project Contents: GUI Tic-tac-toe game using tkinter and classes in python
still incomplete 
"""
from tkinter import *
from tkinter import ttk
import random as r

class nameWindow:
    def __init__(self, master):
        self.frame = Frame(master)
        labelN1 = Label(text="Player One, enter name: ",font=("Cursive",20))
        labelN1.pack(side="top")
        self.var1 = StringVar()
        nameOne = Entry(textvariable=self.var1,width=20,font=("Cursive",20))
        nameOne.pack(side="top")
        labelN2 = Label(text="Player Two, enter name: ",font=("cursive",20))
        labelN2.pack(side="top")
        self.var2 = StringVar()
        nameTwo = Entry(textvariable=self.var2,width=20,font=("cursive",20))
        nameTwo.pack(side="top")
        blank = Label(text="", font=("cursive",20))
        blank.pack(side = "top")

        submit = Button(self.frame, text="Submit", command = self.open ,width=10,font=("cursive",15))
        submit.pack(side="top")
        self.frame.pack(padx=10,pady=10)
    def name(self):
        return self.var1.get(),self.var2.get()
        
        
    def open(self):
        GameWindow = gameWindow(self.name)


class gameWindow:
    def __init__(self,name):
        game = Toplevel()
        self.name = name
        nameOne,nameTwo = self.name()
        players = [nameOne,nameTwo]
        self.frame =Frame(game)
        self.game.counter = 0
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
        reset = Button(text="Restart Game",font=("B612 Mono",15),command=self.restartGame,width=12,height=1,bg="blueviolet")
        reset.pack(side="bottom")
        format1_label = Label(text="",height = 2)
        format1_label.pack(side="bottom")



        frame = Frame(game,highlightbackground="black",highlightthickness=1)
        self.frame.pack()
        for row in range(0,3,1):
            for column in range(0,3,1):
                cells[row][column] = Button(frame, text="",font=("B612 Mono",15),width=8,height=4,
                                            command= lambda row=row, column=column: self.nextTurn(self.row, self.column))
                cells[row][column].grid(row=row,column=column)
            # label=Label(game,text=str("NAme one is :" + nameOne),font=("consolas",30))
            # label.pack(side="top")
            # label1=Label(game,text=str("NAme Two is :"+ nameTwo),font=("consolas",30))
            # label1.pack(side="top")
        
    
    def nextTurn(row,column):
        global player
        
        if cells[row][column]["text"] == "" and Winner() == False:
            
            if player == players[0]:
                
                cells[row][column]["text"] = player
                
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
                
                cells[row][column]["text"] = player
                
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
        curr_Player.config(text =(player + "'s turn"))
        for row in range(3):
            for column in range(3):
                cells[row][column].config(text="",bg="#f0f0f0")

    def gameCounter(self):
        game.counter += 1
        counter_label.config(text=("Times Played: "+str(game.counter)),fg="green")
    
    

         


game = Tk()
game.title("Tic Tac Toe")
game.geometry("400x400")
name = nameWindow(game)
game.mainloop()