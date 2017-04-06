#!/usr/bin/env pypy 
### implemented as in the following SO post. But Swapped A,a with B,b for concurency
### https://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english

import dhredis as r
import primes
import random


pmin=10000 
pmax=342785791

f = r.factor
amin = 100 * f
amax = 999 * f

a = random.randint(amin, amax)

p = primes.getp(pmin,pmax)
g = primes.getp(pmin,pmax)

r.set("p",p)
r.set("g",g)
print("Deciding on 'a'")
print("Calculating A")

A = g ** a % p
r.set("A",A)

B = r.get("B")

S0 = B ** a % p 
r.set("S0", S0)
print("Secret: %d" % S0)


