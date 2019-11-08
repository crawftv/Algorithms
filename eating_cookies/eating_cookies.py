#!/usr/bin/python

import sys

def eating_cookies(n, cache=None):
    cache = {}
    if n == 0:
        return 1
    for i in range(1,n+1): 
        def e(n):
            count = 0
            def eat(n,x):
                nonlocal count
                s = n-x
                if s==0:
                    count +=1
                elif s in cache:
                    count += cache[s]
                elif s<0:
                    pass
                else:
                    eat(s,3) 
                    eat(s,2)
                    eat(s,1)
            eat(n,0)
            cache[n] = count
            return cache[n]
        e(i)
    return cache[n]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")
