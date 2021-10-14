"""
Name: Timothy Johnston
Lab7.py
"""
import math

def cash_conversion():

    cash = eval(input("Enter number: "))
    print("$"+ '{:.2f}'.format(cash))


def encode():
    s = input("Enter a message: ")
    k = eval(input("Enter a key value: "))
    acc = ""
    for c in s:
        i = ord(c)
        k = k+i
        c = chr(k)
        acc += c
    print(acc)

def sphere_area(radius):

    area = (4)*(math.pi)*(radius**2)
    return area


def sphere_volume(radius):

    volume = (4/3)*(math.pi)*(radius**3)
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc+=i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = i*3
    return acc

def encode_better():

    s = input("Enter message: ")
    key = input("Enter key: ")
    acc = ""
    for i in range(len(s)):
        c = s[i]
        k = key[i % len(key)]
        c = ord(c)
        k = ord(k) - 97
        t = c + k
        acc += chr(t)

    print(acc)





def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(6))
    print(sum_n(7))
    print(sum_n_cubes(3))
    encode_better()
    pass


main()
