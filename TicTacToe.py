import random

#declare list
list = [ [1,2,3], 
        [4,5,6], 
        [7,8,9] ]

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
        
       #dis=Display("")
        
       # Display().display()
            
    #loop until games ends
    while True:
        
        #declare com move
        comMove= 0
        
        #get com sym
        if sym == "X":
            comSym = "O"
        elif thing == False:
            comSym="X"
            #declare control for loops
            loop = False
             
        #declare control for loops
        loop = False
        loop2 = False
                     
        
         #check to see if someone wins
         if Win.win(comSym)=True       
        
            
        
#####################################################        
        
class UserClass:
    def userMove(sym):
        #user move
        while loop==False:
            #get input move
                move=int(input("Enter move: "))
                #see if space is taken
                if move != (sym or comSym):
                    #add move
                    for x in list:
                    y=list.index(x)
                    for s in x:
                        b=x.index(s)
                        if s == move:
                            list[y][b]=sym
                            loop=True
                            break     
    
class ComClass:
    def comMove():
    #computer move
        while loop2==False:
            #get move
             comMove=random.randint(1,9)
             #see if space is taken
             if comMove != (sym or comSym):
                 #add move
                 for x in list:
                    y=list.index(x)
                    for s in x:
                        b=x.index(s)
                        if s == comMove:
                            list[y][b]=comSym
                            loop=True
                            break
    
class Display:
    def display():
        #diaplay board
        for x in list:
            print(f"{x}\n")
            
class Win:
    def win(sym):
        #bool for winning
        win=False
        
        #check for all vertical in a row
        i=0
        while i<3:
            if (list[0][i] and list[0][i] and list[2][i])==sym:
                win=True
                break
            else:
                i+=1
         #check for all horizantal in a row
        for x in list:
            if x ==[sym, sym, sym]:
                win=True
                #exit loop
                break
         #check for diagonal
        if list[1][1] and ((list[0][0] and list[2][2]) or (list[0][2] and list[0][2]))==sym:
            win=True
        
        #return bool for win
        return win
