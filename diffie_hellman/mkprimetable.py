#!/usr/bin/env pypy3

import primes


n = 1000000000
while True:
    print(primes.getp(n-1,n),flush=True)

