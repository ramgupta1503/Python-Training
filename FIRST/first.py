# # Askin name of user
# name = input("Enter your name: ")

# # Say hello to the user
# print("hello,", end = "????????" )
# print(name)


# # print("hello," , name , sep= "      ")

# print ("hello, , \"friend\"")





# # Askin name of user
# name = input("Enter your name: ")

# # Remove white space from str
# name = name.strip()

# # Capitileze only the first letter in the string
# name = name.capitalize()

# # It capitalize first letter of all the words
# name = name.title()

# # Say hello to the user
# print(f"hello, {name}")


#        OR


# # Askin name of user
# name = input("Enter your name: ")

# # Remove white space from str and capitalize the words
# name = name.strip().title()

# # Say hello to the user
# print(f"hello, {name}")



#        OR



# Askin name of user
name = input("Enter your name: ").strip().title()

# Split user's name into first name and last name
first, last = name.split (" ")

# Say hello to the user
print(f"hello, {first}")
