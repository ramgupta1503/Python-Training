import sys

# try:
#     print("Hello, My name is", sys.argv[1])                # argv = argument vector
# except IndexError:
#     print("Too few Arguments")

if len(sys.argv) < 2:
    sys.exit("Too few Arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many Arguments")


# Print name tags
# print("hello, my name is", sys.argv[1])

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg) 


# slices = Slice is a subset of data structure like a list.