#!/usr/bin/env python3

"""
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
"""

import cpals as c

b1 = "1c0111001f010100061a024b53535009181c"
b2 = "686974207468652062756c6c277320657965"

correct = "746865206b696420646f6e277420706c6179"


def main():


    result = c.int2hexstr(c.hexstr2int(b1) ^ c.hexstr2int(b2))

    print("result :", result)
    print("correct:", correct)

    if result == correct:
        print("Ok, looks good...")

if __name__ == "__main__":
    main()
