#!/usr/bin/env python3

"""
Convert hex to base64
The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

"""

hex_alphabet = "0123456789abcdef"
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_padding = "="

hex_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
correct = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def slicer(string, leng):
    while len(string) > leng:
        head = string[:leng]
        string = string[leng:]
        yield head
    yield string

def hex2base(hex_string):
    pass
    #return int2base_str(hex_str2int(hex_string))

def main():
    by = ""
    for sl in slicer(hex_in, 3):
        word = 0
        for s in sl:
            word = word * 16 + hex_alphabet.index(s)
        by += str(word)

    print("by", by)

    base = ""
    for sl in slicer(by, 4):
        print("converting slice:", sl)
        sl = int(sl)
        word = ""
        for c in range(2):
            position = int(sl / 64)
            letter = base64_alphabet[position]
            word =  word + base64_alphabet[position] 
            print("adding letter:", letter, "position:", position)
            #word = letter + word
            sl = int(sl) // 64
        base += str(word)

    print(base)


    #print("base",base)

    base_out = hex2base(hex_in)
    if correct == base_out:
        rint("success!")
    print("base_out : %s" % base_out)
    print("correct  : %s" % correct)

    #test()
    #test2()

if __name__ == "__main__":
    main()
