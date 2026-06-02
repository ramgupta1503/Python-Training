# list = Shopping list (collection of same type of items)
# tuple = Fixed Menu
# Set = Bag of unique items
# Dictionary = Dictionary with word meaning


# LISTS ----> (Always stored in a large bracket)

# fruits = ["apple" , "mango" , "banana" , "cherry"]
# print(fruits)

# fruits.append("litchi") # .append is used to add new data type in sequence
# print(fruits)

# fruits.remove("apple") # .remove is used to remove any data type from the list
# print(fruits)


# TUPLE ----> (Always stored in a small bracket)

# coordinates = (99.25 , 45.47)
# print(coordinates)


# SETS ----> (Always stored in a curved brackets, Alwaya contains unique items)

# students = {"Ram " , "Rudra" , "Arnav" , "Yuvraj"}
# print(students)

# students.add("Shubh")
# print(students)

# in sets we use .add instead of .append because
# in sets order is not defined and .append add items at the end


# DICTIONARY ---->

# student = {
#     "Name" : "Ram",
#     "Age" : 20,
#     "Course" : "CSE",
# }
 
# print(student)
# print(student["Name"])

# student["Grade"] = "A"
# print(student)






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