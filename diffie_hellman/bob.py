#!/usr/bin/env pypy

import random
import dhredis as r

f = r.factor

amin = 1000 * f
amax = 9999 * f
b = random.randint(amin, amax)

p = r.get("p")
g = r.get("g")

print("Deciding on 'b'")
print("Calculating B")
B = g ** b  % p
r.set("B", B)

A = r.get("A")

S1 = A ** b % p 

print("Secret: %d" % S1)
#r.set("S1", S1)



