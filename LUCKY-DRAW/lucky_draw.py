import random

print("You have 10 attempts to find correct number")
print("If you got the right answer you will get the icecream otherwise nothing")

for i in range (1,10):
    n = int(input("Choose a number from 1 to 10\n"))

    set = {1,2,3,4,5,6,7,8,9,10}
    i = random.choice(list(set))

    if n == i :
        print("CONGRATULATIONS !! You Won")
        print("The number is " , i)
        break
    else :
        print("You lost !!")
        print("The number is " , i)

print("THANK YOU !!")
print("If you like this game play more !!")
