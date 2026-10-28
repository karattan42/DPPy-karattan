#!/usr/bin/python3


try:
    first_input = int(input("Enter the first number: \n"))
    second_input = int(input("Enter the second number: \n"))
    multed = first_input * second_input
    print(f"{first_input} X {second_input} = {multed}")
    if multed > 0:
        print("The result is positive.")
    elif multed == 0:
        print("The result is positive and negative.")
    else:
        print("The result is negative.")

except :
    print("cmon bro put a valid number")
