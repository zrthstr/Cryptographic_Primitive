#!/usr/bin/env python3

import random
import dhredis as r

amin = 1000
amax = 9999
b = random.randint(amin, amax)

p = r.get("p")
g = r.get("g")

print("Deciding on 'b'")
print("Calculating B")
B = g ** b  % p
r.set("B", B)

A = r.get("A")

S1 = A ** b % p 
r.set("S1", S1)



