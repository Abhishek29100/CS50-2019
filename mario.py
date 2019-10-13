import sys

from cs50 import get_int

# get user input
height = get_int("Height: ")
while height < 1 or height > 8:
    height = get_int("Height: ")

# make pyramid
for i in range(height):
    indent = ""
    for j in range(i + 1, height):
        indent += " "
    block = ""
    for j in range(i + 1):
        block += "#"
    print(indent + block + "  " + block)
