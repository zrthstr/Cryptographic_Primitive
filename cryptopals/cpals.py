#!/usr/bin/env python3


#import operator

hex_alphabet = "0123456789abcdef"
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_padding = "="

symbol_frq = {
'a':8.167,
'b':1.492,
'c':2.782,
'd':4.253,
'e':12.702,
'f':2.228,
'g':2.015,
'h':6.094,
'i':6.966,
'j':0.153,
'k':0.772,
'l':4.025,
'm':2.406,
'n':6.749,
'o':7.507,
'p':1.929,
'q':0.095,
'r':5.987,
's':6.327,
't':9.056,
'u':2.758,
'v':0.978,
'w':2.360,
'x':0.150,
'y':1.974,
'z':0.074,
' ':10.0
}


def hexstr2ascii(hexstr):
    string = ""
    for i in range(len(hexstr)//2):
        string += chr(hexstr2int(hexstr[:2]))
        hexstr = hexstr[2:]
    return string


def sbx(string, key):
    """ single byte xor """
    result = ""
    for c in string:
        result += chr(ord(c) ^ ord(key))
    return result


def weight(string):
    w = 0
    for s in symbol_frq:
        w+= string.count(s) * symbol_frq[s]
    return w


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

