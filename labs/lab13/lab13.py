"""
Name: Timothy Johnston
lab13.py
"""
from random import randint

def is_in_binary(search_val, values):
    mid = len(values)//2
    while search_val != values[mid] and len(values)!= 1:
        if search_val < values[mid]:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values)//2
    if search_val == values[mid]:
        return True
    return False


def selection_sort(values):

    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def get_area(rect):

    return randint(1, 100)


def rect_sort(rectangles):

    d = { }
    areas = []
    for rect in rectangles:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]

def trades(filename):
    infile=open(filename,"r")
    data = infile.read().split()
    for line in data:

#Not sure about the loop










def main():
    x = [5, 2, 1, 3]
    print(x)
    print(is_in_binary(7, [1,2,3,4,5,6]))
    selection_sort(x)
    print(x)

    pass


main()