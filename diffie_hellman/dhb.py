
import getp
import random
import dhredis as r

amin = 1000
amax = 9999
a = random.randint(amin, amax)

p = r.get("p")
g = r.get("g")
print("got p: %d, g: %d" % (p, g))

B = g ** a  % p
r.set("B", B)
print "set B:",B

A = r.get("A")
## GET B
S = B ** a % p 

print "S:", S




