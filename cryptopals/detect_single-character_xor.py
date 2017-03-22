#!/usr/bin/env python3


"""
Detect single-character XOR
One of the 60-character strings in this filei(https://cryptopals.com/static/challenge-data/4.txt) has been encrypted by single-character XOR.

Find it.
"""
import cpals as c
import operator

in_file = "detect_single-character_xor.txt"

def main():
    table = []

    with open(in_file) as f:
        for i, line in enumerate(f):
            line_ascii = c.hexstr2ascii(line)
            for key in range(0,256):
                xored = c.sbx(line_ascii, chr(key))
                table.append([c.weight(xored), chr(key), i, xored])

    sorted_score = table.sort(key=lambda x: int(x[0]))
    for t in (table[-3:]):
        print(t)

if __name__ == "__main__":
    main()
