def encode(line, key):
    acc = ""
    for c in line:
        i = ord(c)
        key = key+i
        c = chr(key)
        acc += c


def encode_better(line, key):


    acc = ""
    for i in range(len(line)):
        c = line[i]
        k = key[i % len(key)]
        c = ord(c)
        k = ord(k) - 97
        t = c + k
        acc += chr(t)