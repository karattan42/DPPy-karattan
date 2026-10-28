#!/usr/bin/python3

# try:
#    num_input = int(input("Enter a number less than 25:\n"))
#
#    if num_input > 25:
#        print("Error")
#
#   # while num_input <= 25:
#   #     print(f"Inside the loop, my variable is {num_input}")
#   #     num_input += 1
# except ValueError:
#    print("Error")

try:
    num = int(input("Enter a number less than 25 :\n"))
except ValueError:
    print("Error")
else:
    if num > 25:
        print("Error")
    # range ถ้าสอง arg มันจะไม่นับตัวสุดท้าย
    for i in range(num, 26):
        print(f"Inside the loop, my variable is {i}")
