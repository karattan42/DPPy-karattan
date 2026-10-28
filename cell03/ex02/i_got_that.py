#!/usr/bin/python3


def need_stop(first_time=True):
  

    if first_time:
        answer = input("What you gotta say? : ")
    else:
        answer = input("I got that! Anything else? : ")
    
    if answer == "STOP":
        return
    need_stop(False)
need_stop()
    
    

    