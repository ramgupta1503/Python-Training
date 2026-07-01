def main():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

p = main()
meow(p)



# OR

def main():                              # For returning value      
    number = get_number()
    meow(number)

def get_number():                        # For input number       
    while True:
        n = int(input("What's n? "))    
        if n > 0:
            return n
     
def meow(n):                             # For output meow
    for _ in range(n): 
        print("meow")
    

main()