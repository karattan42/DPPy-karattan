#!/usr/bin/python3


try:
    usr_numinput = int(input())


    if (usr_numinput > 0 ):
        print("This number is positive.")
    elif usr_numinput == 0:
        print('This number is both positive and negative.')
    else:
        print("This number is negative.")

except:
    print("Please enter a valid integer.")
