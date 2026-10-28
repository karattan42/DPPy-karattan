#!/usr/bin/python3

num = int(input("Enter a number \n"))

try:
    for i in range(10):
        print(f"{i} X {num} = {i * num}")
except ValueError:
    print("Error pls input a valid number")
