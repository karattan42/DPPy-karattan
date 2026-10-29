#!/usr/bin/python3

text = input("Give me a number: ")
try:
    num = int(text)
    print("This number is integer")
except ValueError:
    try:
        num = float(text)
        print("This number is float")
    except ValueError:
        print("That's not a valid float!")