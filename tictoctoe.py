# Created by Sanket Mote 
# For college project - Topic - Python Gui
# Project Name -  Tic-Toc-Toe 
# Created game using Tkinter 
# importing tkinter modlue 

from tkinter import *
from tkinter import messagebox
import random as rm 

# function for  defining width of one frame
def frame(frame):         
    frm = Button(frame,bg="white",width=3,padx=4,font=('arial',60,'bold'),bd=10,relief="flat")
    return frm 

#Function to change the operand for the next player 

def change_player():             
    global a
    global player
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
    for i in [player1,player2]:
        if not(i==player):
            player=i
            break

# Function to Resets the game
def reset():                
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=rm.choice(['O','X'])

#Checks for victory or Draw

def check():                
    for i in range(3):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
            messagebox.showinfo("Congrats!!","'"+player+"' has won")
            reset()
        if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
            messagebox.showinfo("Congrats!!","'"+player+"' has won")
            reset()   
        elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
            messagebox.showinfo("Tied!!","The match ended in a draw")
            reset()


def click(row,col):
    b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
    check()
    change_player()
    label.config(text=player+"'s Chance")

def submit(): 
    global flg
    global player1
    global player2
    player1 = player1_entry.get() 
    player2 = player2_entry.get() 
    messagebox.showinfo("Note","To play please exit both Windows")
    print("The Player 1  is : " + player1) 
    print("The Player 2  is : " + player2) 
    flg=0


            
  

flg = 1
if flg==1:
    root1 = Tk()
    root1.title("Player Detail") 
    name_var= StringVar() 
    name_var1= StringVar() 
    player1_label = Label(root1, text = 'Enter Player 1 Detail ',font=('calibre',10, 'bold')) 
    
    player1_entry = Entry(root1,textvariable =name_var,font=('calibre',10,'normal')) 

    player2_label = Label(root1, text = 'Enter Player 2 Detail',font=('calibre',10, 'bold')) 
    
    player2_entry = Entry(root1, textvariable = name_var1,font=('calibre',10,'normal')) 

    sub_btn=Button(root1,text = 'Submit',command = submit) 

    player1_label.grid(row=0,column=0) 
    player1_entry.grid(row=0,column=1) 
    player2_label.grid(row=1,column=0) 
    player2_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1) 
    root1.mainloop()


if flg==0:
    root = Tk()
    root.title("Tic-Tac-Toe")
    a = rm.choice(['O','X'])   
    player = rm.choice([player1,player2])   
    colour={'O':"deep sky blue",'X':"lawn green"}
    b=[[],[],[]]
    for i in range(3):
            for j in range(3):
                    b[i].append(frame(root))
                    b[i][j].config(command= lambda row=i,col=j:click(row,col))
                    b[i][j].grid(row=i,column=j)
    label=Label(text=player+"'s Chance",font=('arial',20,'bold'))
    label.grid(row=3,column=0,columnspan=3)

    root.mainloop()
