#!/usr/bin/env python3

def happy_new_year():
    start = 10
    while start in range (10, 0, -1):
       print(start)

       start -= 1
       print("Happy New Year!")

def square_integers(int_list):
    return [i ** 2 for i in int_list]

def fizzbuzz():
    for i in range (1, 101):
        if not i % 3 :
            print ("Fizz")
        elif not i % 5:
            print ("Buzz")
        elif not i % 3 and not i % 5 :
            print("FizzBuzz")
        else:
            print(i)
            pass


