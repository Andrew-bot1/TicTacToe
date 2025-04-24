import random

#function to display the board
def display():
    #diaplay board
    for x in list:
        print(f"{x}\n")

#function to see if anyone wins
def win(sym):
    #bool for winning
    win=False
    
    #check for all vertical in a row
    for i in range(3):
        if list[0][i]==sym and list[1][i]==sym and list[2][i]==sym:
            win=True
            break
    #check for all horizantal in a row
    for x in list:
        if x ==[sym, sym, sym]:
            win=True
            #exit loop
            break
    #check for diagonal
    if list[1][1]==sym and ((list[0][0]==sym and list[2][2]==sym) or (list[0][2]==sym and list[2][0]==sym)):
        win=True

    #return bool for win
    return win

#function to add user move
def userMove(sym,comSym):
    loop=False
    #user move
    while loop==False:
        #get input move
        move=int(input("Enter move: "))
        #see if space is taken
        if move != sym and move !=comSym:
            #add move
            for x in list:
                y=list.index(x)
                for s in x:
                    b=x.index(s)
                    if s == move:
                        list[y][b]=sym
                        loop=True
                        break  
                    
#funciton to add computer move                   
def comMove(comSym,sym):
    loop=False
    #computer move
    while loop==False:
        #get move
        comMove=random.randint(1,9)
        #see if space is taken
        if comMove != sym and comMove !=comSym:
            #add move
            for x in list:
                y=list.index(x)
                for s in x:
                    b=x.index(s)
                    if s == comMove:
                        list[y][b]=comSym
                        loop=True
                        break                         

#run program until user wants to exit
while True:
    #ask if user wants to exit
    exit = input("Do you want to exit? y/n ").lower()
    #exit if user wants to
    if exit=="y":
        break
    else:
        #get user input on symbol
        sym=input("X or O: ").upper()
        
        #declare thing
        thing=False
        
       #declare list
        list = [ [7,8,9], 
                [4,5,6], 
                [1,2,3] ]
        #display board
        display()
            
    #loop until games ends
    while True:
        #get com sym
        if sym == "X":
            comSym = "O"
        elif thing == False:
            comSym="X"
            #get computer move
            comMove(comSym,sym)
            #display board
            display()
            #set thing to true
            thing =True
        #get user move
        userMove(sym,comSym)
        #check to see if user wins
        if win(sym):
            print("You win!")
            break
        #get computer move
        comMove(comSym,sym)
        #check to see if computer wins
        if win(comSym)==True:
            print("You lose!")
            break 
        #display board
        display()
