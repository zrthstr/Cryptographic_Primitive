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

hex_aph = "0123456789abcdef"
base_aph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base_padding = "="

hex_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
correct = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex2base(hex_string):
    return int2base_str(hex_str2int(hex_string))

def int2base_str(integer):
    base_string = ""
    while integer > 64:
        base_string = base_aph[integer % 64] + base_string
        integer //= 64
    base_string = base_aph[integer % 64] + base_string
    #base_string = base_string + base_padding * (len(base_string) - (len(base_string) // 3 )* 3 )
    return base_string
    
    

def hex_str2int(hex_string):
    raw = 0
    for c in hex_string:
        raw = int(raw * 16)
        raw += hex_aph.index(c)
    return raw

def test():
    for r in range(64**5):
        print("%d --> : %s " % (r, int2base_str(r)))

def test2():
    for r in ["00", "0000", "0001", "000000", "000001"]:
        print("%s --> : %s " % (r, hex2base(r)))

def main():
    base_out = hex2base(hex_in)
    if correct == base_out:
        print("success!")
    print("base_out : %s" % base_out)
    print("correct  : %s" % correct)

    #test()
    #test2()

if __name__ == "__main__":
    main()
