#!/usr/bin/python3

try:
    num = float(input("Give me a number: "))
    print(f"Rounded up: {num:.0f}")
except ValueError:
    print("That's not a valid float!")