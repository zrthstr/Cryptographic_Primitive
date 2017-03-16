### https://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english


import dhredis as r
import getp
import random

pmin=100
pmax=999
amin = 1000
amax = 9999

a = random.randint(amin, amax)

p = getp.getp(pmin,pmax)
g = getp.getp(pmin,pmax)

r.set("p",p)
r.set("g",g)

print("set p: %d, g: %d" % (p, g))

A = g ** a % p

#B = g ** b % p
#print "B:",B
r.set("A",A)

B = r.get("B")

S = B ** a % p 
print "S:", S




