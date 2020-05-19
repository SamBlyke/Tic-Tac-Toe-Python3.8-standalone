#Importing the main modules

from subprocess import check_call
from time import sleep
import os

os.system("color 1E")

print("              ______________ TIC TAC TOY _______________")
print();print(" '/e' to exit ")

#Game against Computer will arrive soon. Logic in development.

#os.system("@echo off")
#os.system(r"echo COMPUTER")
#os.system(r"echo 2 PLAYERS")
#check_call(r"""set /p id= PLAY WITH [1/2] : 
#if %id% == 1 (echo    In Developments. Will Arrive soon. )
#if %id% == 2 (pause)""", shell=True)
#os.system(r"set /p id= PLAY WITH [1/2] : & if %id% == 1 (echo  __________ In Developments. Will Arrive soon. & if %id% == 2 (pause)")
#os.system(r"if %id% == 1 (echo  __________ In Developments. Will Arrive soon.  ")
#os.system(r"if %id% == 2 (pause)")



board={1:"-",2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-"}

def out_board(board):
    print("                      %s | %s | %s        1|2|3" %(board[1],board[2],board[3]))
    print("                      __________       ______")
    print("                      %s | %s | %s        4|5|6" %(board[4],board[5],board[6]))
    print("                      ___________      ______")
    print("                      %s | %s | %s        7|8|9" %(board[7],board[8],board[9]))
    print()

out_board(board)
count=0
i="0"
j="X"
ij="0"

def game(i,j,ij):

    count=0
    ij="0"
    num=[str(i) for i in range(1,10)]
    global board
    while True:
        n=input("Enter you choice, PLAYER %s [1-9] : " %j)
        if(str(n)=="/e"):
            os.system("exit()")
            break
        elif(n not in num):
            out_board(board)
            print("            _____Wrong Input, TRY  AGAIN_____")
            continue
        elif(board[(int(n))]!="-"):
            out_board(board)
            print("        ____Already Filled Place. Try Another. _____")
            continue
        n=int(n)
        i=ij
        ij=j
        j=i

        board[n]=ij

        out_board(board)
        count=count+1
        if(count==9):
            break

        else:
            if(count>=3):
                if(board[1]==board[2]==board[3]== "0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[4]=="0" and board[5]=="0" and board[6]=="0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[7]==board[8]==board[9]== "0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[1]==board[5]==board[9]== "0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[3]==board[5]==board[7]== "0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[1]==board[4]==board[7]== "0" ):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[2]==board[5]==board[8]== "0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[3]==board[6]==board[9]== "0"):
                    print("**** PLAYER 0 WON ****")
                    break
                elif(board[1]==board[2]==board[3]== "X"):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[4]=="0" and board[5]=="0" and board[6]=="0"):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[7]==board[8]==board[9]== "X"):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[1]==board[5]==board[9]== "X"):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[3]==board[5]==board[7]== "X"):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[1]==board[4]==board[7]== "X" ):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[2]==board[5]==board[8]== "X"):
                    print("**** PLAYER X WON ****")
                    break
                elif(board[3]==board[6]==board[9]== "X"):
                    print("**** PLAYER X WON ****")
                    break
                else:
                    continue
    
game(i,j,ij)

while True:

    play_again=str(input("Start a match[Y] or quit [N] ? [Y/N] "))
    if(play_again=="y"):

        out_board(board)
        count=0
        i="0"
        j="X"
        ij="0"
        game(i,j,ij)

    elif(play_again=="n"):

        print("EXITING")
        sleep(1)
        break