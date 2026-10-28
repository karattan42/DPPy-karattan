#!/usr/bin/python3

import sys


if len(sys.argv) > 1:
    print("none")
else:
    for i in range(10):
        print(f"Table de 0:", end=" ")
        for j in range(10):
            print(i*j,end=" ")
        print()
        
            
        