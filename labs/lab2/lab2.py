"""
Timothy Johnston
lab2.py

"""

import math

def sum_of_threes():

    bound = eval(input("What is your bound?: "))
    x = 0
    for i in range (0, bound+1, 3):
        x = i + x
    print(x)

def multiplication_table():

    for h in range (1, 11):
        for l in range(1, 11):
            print(h*l, end=" ")
        print()

def triangle_area():
    a = eval(input("Enter length of a: "))
    b = eval(input("Enter length of b: "))
    c = eval(input("Enter length of c: "))
    s = (a+b+c)/2
    A = math.sqrt(s*(s - a)*(s-b)*(s-c))

    print(round(A))

def sumSquares():

    a = eval(input("Enter lower bound: "))
    b = eval(input("Enter upper bound: "))
    x = 0
    for i in range(a, b+1):
        x = x + i**2
    print(x)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    x = 1
    for i in range(exponent):
        x = base * x
    print(x)

#sum_of_threes()
#multiplication_table()
#sumSquares()
#power()




