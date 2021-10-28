"""
Name: Timothy Johnston
lab9.py
"""

from graphics import *
import math


def addTen(nums):
    nums[0] = 5
    for i in range(len(nums)):
        nums[i] = nums[i]+10






def squareEach(nums):
    nums[0] = 5
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2





def sumList(nums):
    nums[0] = 5
    acc = 0
    for i in range(len(nums)):
        nums[i] = nums[i]+acc

    return acc





def toNumbers(strList):
    strList[0] = 5
    for i in range(len(strList)):
        strList[i] = float(strList[i])



def writeSumOfSquares():

    ifn = input()
    infile = open(ifn, "r")
    outfile = open("thing.txt","w+")
    for line in infile:
        line = line.split
        sumList()
        squareEach()
        toNumbers()
        outfile.write(line)

def starter():
    weight = eval(input("Enter weight: "))
    numWins = eval(input("Enter number of wins: "))

    if weight >= 150 and weight < 160 and numWins >=5:

        print("Is a Starter")

    elif weight > 199 or numWins > 20:

        print("Is a Starter")

    else:
        print("Does not Start")


def leapYear(year):

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Is a leap year")

    else:
        print("Not a leap year")


def circleOverlap():
    win = GraphWin("circleOverlap", 400,400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    radius2 = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle2 = Circle(p2, radius2)
    circle.draw(win)
    circle2.draw(win)
    win.getMouse()
    win.close()

    distance = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    if distance <= radius + radius:
        print("it overlaps")
    else:
        print ("does not overlap")






def main():

    w = [1, 5, 8]
    addTen(w)

    x = [5, 2, -3]
    squareEach(x)

    y = [2, 4, 6]
    sumList(y)

    z = [6, 8, 9]
    toNumbers(z)
    print(w, x, y, z)

    #writeSumOfSquares()
    starter()
    leapYear(2007)
    circleOverlap()

    pass


main()