"""
Name: Timothy Johnston
Lab8.py
"""
from encryption import encode
from encryption import encode_better



def number_words(in_file_name, out_file_name):

    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i)+ " " + word + "\n")
            i+=1



def hourly_wages(in_file_name, out_file_name):

    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")

    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        r = wage + 1.65
        wage = r * int(parts[3])
        outfile.write(parts[0] + parts[1] + " " + str(wage) + "\n")



def calc_check_sum(isbn):

    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += (pos*int(isbn[i]))

    return acc

def send_message(file, friend):

    infile = open(file, "r")
    outfile = open(friend + "message.txt", "w+")
    for line in infile:
        outfile.write(line)

def send_safe_message(file, friend, key):

    infile = open(file, "r")
    outfile = open(friend + "message.txt", "w+")
    for line in infile:
        outfile.write(encode(line,key))


def send_uncrackable_message(file, friend, pad):

    infile = open(file, "r")
    outfile = open(friend + "message.txt", "w+")
    padfile = open(pad, "r")
    key = padfile.read()
    for line in infile:
        outfile.write(encode_better(line,key))


def main():
    number_words("Walrus.txt", "surlaw.txt")
    hourly_wages("hourly_wages.txt", "finalhwages.txt")
    calc_check_sum("1223545")
    send_message("message.txt", "friend")
    send_safe_message()
    send_uncrackable_message()
    pass

main()