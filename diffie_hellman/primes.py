#!/usr/bin/env pypy

import math
import sys
import random
from linecache import getline

prime_file_list = "primes.lst"


def find_p_upto(upto):
    
    found = [2,3,5]
    c = 5

    while True:
        c +=2
        for f in found:
            if f > math.sqrt(c):
                found.append(c)
                break
            elif c % f == 0:
                break
        if c > upto:
            for f in found:
                print(f)
            sys.exit()


def getp(pmin=0, pmax=1*10**60):
        num_lines = sum(1 for line in open(prime_file_list))
        while True:
            prime = int(getline(prime_file_list, random.randint(0, num_lines)))
            if pmin <= prime <= pmax:
                return prime


if __name__ == "__main__":
    #print ("Found prime from range [%d - %d]: %d"  % ( pmin, pmax, getp()))
    #getp()
    find_p_upto(10**7)
