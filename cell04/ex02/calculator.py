#!/usr/bin/python3

try:
    num = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    print("Thank you!")

    def print_result(x, y):
        print(f"{x} + {y} = {x + y}")
        print(f"{x} - {y} = {x - y}")
        print(f"{x} / {y} = {x / y:g}")
        print(f"{x} * {y} = {x * y}")

    print_result(num, num2)
except ValueError:
    print("lol")
