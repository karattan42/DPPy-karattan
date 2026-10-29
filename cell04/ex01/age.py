#!/usr/bin/python3


try:
    age = int(input("Please tell me your age: "))

    print(f"You are currently {age} years old")

    for i in range(1, 4):
        year = i * 10
        print(f"In {year} you'll be {age + year} years old.")
except ValueError:
    print("Please input valid number")
