# QUESTION --1

# favouritecolors = {"red" , "black" , "green" , "blue"}
# print(favouritecolors)

# favouritecolors.add("red")
# print(favouritecolors)

# QUESTION --2

# fruits = ["banana" , "mango" , "Orange" , "litchi"]
# print(fruits[0])
# print(fruits[3])

# QUESTION --3

# n1 = int(input("Enter first number : "))
# n3 = int(input("Enter second number : "))
# n2 = int(input("Enter third number : "))
# n4 = int(input("Enter fourth number : "))
# n5 = int(input("Enter fifth number : "))

# numbers = [n1 , n2 , n3 , n4 , n5]
# unique_numbers = set(numbers)
# print(unique_numbers)

# QUESTION --4

# marks = {
#     "Math" : 80 ,
#     "Science" : 75 ,
#     "English" : 90
# }
# print(marks.keys())
# print(marks.values())
# print(marks)
# average = sum(marks.values())/len(marks)
# print("Average is " , average)

# QUESTION --5

age = int(input("Enter your age : "))
if 0 < age < 13 :
    print("Child")
if 13 < age < 19 :
    print("Teenager")
if age > 19 :
    print("Adult")
if age < 0 :
    print("Invalid Input")