#!/usr/bin/env python3

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

message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def main():
    score={}
    string = c.hexstr2ascii(message)

    for key in range(0,256):
        r = c.sbx(string, chr(key))
        score[key] = c.weight(r)

    sorted_score = sorted(score.items(), key=operator.itemgetter(1))
    key = sorted_score[-1][0]

    print("heaviest:",sorted_score[-1])
    print(c.sbx(c.hexstr2ascii(message), chr(key)))


if __name__ == "__main__":
    main()
