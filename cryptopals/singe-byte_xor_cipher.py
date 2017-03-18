#!/usr/vin/env python3

"""
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""

import cpals as c
import operator

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

message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def hexstr2ascii(hexstr):
    string = ""
    for i in range(len(hexstr)//2):
        string += chr(c.hexstr2int(hexstr[:2]))
        hexstr = hexstr[2:]
    return string


def sbx(string, key):
    result = ""
    for c in string:
        result += chr(ord(c) ^ ord(key))
    return result


def weight(string):
    w = 0
    for s in symbol_frq:
        w+= string.count(s) * symbol_frq[s]
    return w


def main():
    score={}
    string = hexstr2ascii(message)

    for key in range(0,256):
        r = sbx(string, chr(key))
        score[key] = weight(r)
        #print(r, weight(r))

    sorted_score = sorted(score.items(), key=operator.itemgetter(1))
    key = sorted_score[-1][0]
    print("heaviest:",sorted_score[-1])
    print(sbx(hexstr2ascii(message), chr(key)))


if __name__ == "__main__":
    main()
