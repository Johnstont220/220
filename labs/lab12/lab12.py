"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint



def find_and_remove_first(list, value):
    #while list, value
    try:
        i = list.index(value)
        list[i] = "Timothy Johnston"
    except:
        pass

def read_data(filename):

    file = open(filename, "r")
    data = file.read()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i+=1


def is_in_linear(search_val, values):
    i = 0
    while i < len(search_val):
        if values == search_val:
            return True
        i+=1
        return False


def good_input():

    x = eval(input("Enter number: "))
    while x > 10 and x < 1:
        x = eval(input("The number is not in range 1, 10. Try again: "))
        return x


def num_digits():

    num = eval(input("Enter positive integer: "))
    while num > 1:
        digits = 0
        while num != 0:
            num//=10
            digits+=1
        num = eval(input("Enter positive integer: "))


def hi_lo_game():

    num = randint(1,100)
    guessed = 0
    guess = eval(input("Enter guess: "))
    while guess != num and guessed != 7:
        guessed+=1
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        if guess != num and guessed != 7:
            guess = eval(input("Guess again: "))
        if guess == num:
             print("You won! in", guessed, "guesses")
        elif guessed == 7:
             print("You lost. The number was", num )





def main():
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()