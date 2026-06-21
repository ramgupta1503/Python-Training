   elif (computer == 0 and you == 1):          computer == you  = -1
        print("You lose")
    
    elif (computer == -1 and you == 0):        computer == you = -1     
        print("you lost")
    
    elif (computer == 1 and you == -1):        computer == you = 2 
        print("You lose")

    if (computer == -1 and you == 1):          computer == you = -2    
        print("you win")
    
    elif (computer == 1 and you == 0):         computer == you = 1               
        print("You win")
    
    elif (computer == 0 and you == -1):        computer == you = 1                    
        print("You win")
    


    

if (computer - you == -1 or computer - you == 2):
    print("You lose !!")

elif (computer == you):
    print("It's a draw !!")

else:
    print("You won !!")