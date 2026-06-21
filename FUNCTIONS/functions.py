# def greet() :
#     print("hello world")

# greet()




# def add(a , b) :
#     return a + b

# x = int(input("Enter first number : "))
# y = int(input("Enter second number : "))
# result = add(x,y)
# print("Sum is " , result)



# PRIME NUMBER 

# x = int(input("Enter the number : "))
# y = "no prime"
# z = "prime"

# def prime(x) :
#     if x < 2 :
#         return y
#     for i in range(2,x):
#         if x % i == 0 :
#             return y
#     else :
#         return z

# result = prime(x)
# print(result)




# QUESTION 

# def aboutme() :
#     print("RAM GUPTA")
#     print("My age is 20")
#     print("Currently living in Greater Noida")

# aboutme()



# SQUARE OF A NUMBER

# x = int(input("Enter the number : "))
# def square(num) :
#     return num*num

# result = square(x)
# print(result)






# def goodDay(naam, antt):
    # print("Good day," , naam)
    # print(antt)
# 
# name = input("Enter your name: ")
# ending = input("Write your ending: ")
# 
# 
# 
# goodDay(name, ending)'





# def goodDay(name, ending):
#     print("Good Day, " , name)
#     print(ending)
#     return 

# a = goodDay("Ram" , "Thank You !!")
# print(a)





# def avg():
#     a = int(input("Enter the marks: "))
#     b = int(input("Enter the marks: "))
#     c = int(input("Enter the marks: "))

#     avg = (a+b+c)/3
 
#     return avg
 
# average = avg()
# print("Average is " , average)





def rem (l , word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Harry" ,  "Rohan" , "Shubham" , "an"]

print(rem(l, "an"))