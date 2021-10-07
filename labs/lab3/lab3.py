"""
Timothy Johnston
lab3.py
"""

def average():
    hw = eval(input("How many grades: "))
    x = 0
    for i in range(hw):
        grade = eval(input("Enter Grade on Hw: "))
        x = (x+grade)
    print(x/hw)



def tip_jar():
    x = 0
    for i in range(5):
        y = eval(input("How much is your donation: "))
        x = x+y
    print("Total amount in jar:",x)




def newton():
    x = eval(input("What number: "))
    y = eval(input("How many improvements: "))
    approx = x/2
    for i in range(y):
        approx = (approx +(x/approx))/2
    print(approx)




def sequence():
    x = eval(input("Enter number of terms: "))
    for i in range(1,x+1):
        y = 1+(i//2*2)
        print(y)


def pi():
    x = 1
    term = eval(input("How many terms: "))
    for i in range(term):
        num = 2 + (x//2*2)
        denom = 1 + ((x+1)//2*2)
        x = x*(num/denom)
    print(x*2)



average()
#tip_jar()
#sequence()
#newton()
#pi()