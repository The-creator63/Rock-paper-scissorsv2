from tkinter import*
import random
import tkinter.font as font

computer_score = 0
player_score = 0 
options = [("Rock",0),("Paper",1),("Scissors",2)]#

def computer_wins():
    global computer_score,player_score
    computer_score = computer_score + 1
    winner_lbl.config(text = "Computer wins!")
    computer_score_lbl.config(text = "Computer score: " + str(computer_score))
    player_score_lbl.config(text = "Player score: " + str(player_score))

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x300")

heading_lbl = Label(root,text = "Rock Paper Scissors",font = font.Font(size = 20),fg = "black")
heading_lbl.pack()

winner_lbl = Label(root,text = "The game has begun",font = font.Font(size = 14),fg = "green")
winner_lbl.pack()

frame = Frame(root)
frame.pack()

options_lbl = Label(frame,text = "Your options: ",font = font.Font(size = 12),fg = "black")
options_lbl.grid(row = 0,column = 0)

rock_btn = Button(frame,text = "Rock",font = font.Font(size = 8),width = 15,fg = "black",bg = "grey")
rock_btn.grid(row = 1,column = 1,padx = 6, pady = 5)

paper_btn = Button(frame,text = "Paper",font = font.Font(size = 8),width = 15,fg = "black",bg = "yellow")
paper_btn.grid(row = 1,column = 2,padx = 6, pady = 5)

scissors_btn = Button(frame,text = "Scissors",font = font.Font(size = 8),width = 15,fg = "black",bg = "green")
scissors_btn.grid(row = 1,column = 3,padx = 6, pady = 5)

score_lbl = Label(frame,text = "Score:",font = font.Font(size = 12),fg = "black")
score_lbl.grid(row = 2,column = 0)

player_choice = Label(frame,text = "You selected: ",font = font.Font(size = 12),fg = "black")
player_choice.grid(row = 3, column = 1,pady = 5)

player_score_lbl = Label(frame,text = "Your score: ",font = font.Font(size = 12),fg = "black")
player_score_lbl.grid(row = 3, column = 2,pady = 5)

computer_choice = Label(frame,text = "Computer selected: ",font = font.Font(size = 12),fg = "black")
computer_choice.grid(row = 4,column = 1,pady = 5)

computer_score_lbl = Label(frame,text = "Computer score: ",font = font.Font(size = 12),fg = "black")
computer_score_lbl.grid(row = 4,column = 2,pady = 5)

root.mainloop()