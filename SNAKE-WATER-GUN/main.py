import random
'''
1 for snake
-1 for Water
0 Gun
'''
computer = random.choice([1, -1, 0])
youstr = input("Enter your Input: ")
youDict = { "s" : 1, "w" : -1, "g" : 0}
reverseDict = { 1: "s", -1 : "w",0 : "g"}

you = youDict[youstr]   

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if (you == computer):
    print("It's a draw !!")

else:
    if (computer == -1 and you == 1):
        print("you win")
    
    elif (computer == -1 and you == 0):
        print("you lost")
    
    elif (computer == 1 and you == -1):
        print("You lose")
    
    elif (computer == 1 and you == 0):
        print("You win")
    
    elif (computer == 0 and you == 1):
        print("You lose")
    
    elif (computer == 0 and you == -1):
        print("You win")
    
    else:
        print("Something went wrong")



# EXPLANATION ON NEXT PAGE



# if (computer - you == -1 or computer - you == 2):
#     print("You lose !!")

# elif (computer == you):
#     print("It's a draw !!")

# else:
#     print("You won !!")