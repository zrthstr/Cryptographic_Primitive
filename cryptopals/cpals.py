#!/usr/bin/env python3


hex_alphabet = "0123456789abcdef"
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_padding = "="

def hex2base(hex_string):
    return int2base64str(hexstr2int(hex_string))


def hexstr2int(hexstr):
    i = 0
    for h in hexstr:
        i = i * 16 + hex_alphabet.index(h)
    return i

def int2base64str(i):
    base = ""
    while i >= 64:
        base = base64_alphabet[i % 64 ] + base
        i //= 64
    base = base64_alphabet[i % 64 ] + base

    while len(base) % 3:
        base = base + base64_padding
    return base


def int2hexstr(i):
    h = ""
    while i >= 16:
        h = hex_alphabet[i % 16] + h
        i //= 16 
    return hex_alphabet[i % 16] + h


def test_int2hexstr():
    for i in range(35):
        print("%d \t-->\t0x%s" % (i, int2hexstr(i)))
    for i in range(35,100,12):
        print("%d \t-->\t0x%s" % (i, int2hexstr(i)))
    for i in range(100,2000,123):
        print("%d \t-->\t0x%s" % (i, int2hexstr(i)))


def test_hex2base():
    for e in range(100):
        print("0x%x --> \t\t\tbase64: %s" %( e,  hex2base(int2hexstr(e))))
    print(" - ")
    for e in range(100, 2000, 31):
        print("0x%x --> \t\tbase64: %s" %( e,  hex2base(int2hexstr(e))))
    print(" - ")
    for e in range(2000, 200000, 1001):
        print("0x%x --> \t\tbase64: %s" %( e,  hex2base(int2hexstr(e))))

def test():
    test_int2hexstr()
    test_hex2base()


if __name__ == "__main__":
    test()



