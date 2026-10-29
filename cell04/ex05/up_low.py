#!/usr/bin/python3

try:
    text = input()
    print(f"{text.swapcase()}")
except ValueError:
    print("That's not a valid string!")