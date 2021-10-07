#Timothy Johnston
#lab6.py


def name_reverse():

    x = input("Enter name:")
    x = x.split()
    print(x[1] + "," + x[0])

def company_name():
    x = input("Enter domain:")
    x = x.split(".")
    print(x[1])


def initials():
    n = eval(input("How many names: "))
    for i in range(n):
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        print(first[0] + last[0])

def names():
    x = input("Enter names: ")
    x = x.split(",")
    for name in x:
        parts = name.split()
        print(parts[0][0] + parts[1][0])


def thirds():
    t = eval(input("How many sentences: "))
    for i in range(t):
        s = input("sentence: ")
        print(s[2:len(s):3])

def word_average():
    x = input("Enter sentence: ")
    a = 0
    x = x.split()
    for word in x:
         a = len(word) + a
    print(a/len(x))

def pig_latin():
    x = input("")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + "ay", end =" ")
    print(x)



#name_reverse()
#company_name()
#thirds()
##initials()
##word_average()
names()
#pig_latin()