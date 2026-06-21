# f = open("file.txt")
# print(f.read())
# f.close()


# THE SAME STATEMENT CAN BE PRINT BY USING WITH STATEMENT

with open("file.txt") as f:
    print(f.read())

# BY USING WITH STATEMENT WE DON'T HAVE TO EXPLICITLY CLOSE THE FILE
