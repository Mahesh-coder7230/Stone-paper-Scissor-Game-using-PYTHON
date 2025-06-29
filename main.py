import random
'''
1-stone
-1-paper
0-scissor

'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
youDict ={"Stone":1 ,"Paper":-1,"Scissor":0}
reverseDict={1:"Stone",-1:"Paper",0:"Scissor"}
you= youDict[youstr]
print(f"You Choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer==you):
    print("DRAW!!!")
else:

    if(computer==-1 and you==1):
        print("Computer win!!!")
    elif(computer==-1 and you==0):
        print("You win!!!")
    elif(computer==1 and you==-1):
        print("You win!!!")
    elif(computer==1 and you==0):
        print("Computer win!!!")
    elif(computer==0 and you==-1):
        print("Computer win!!!")
    elif(computer==0 and you==1):
        print("You win!!!")
    else:
        print("Something Went wrong!!!")