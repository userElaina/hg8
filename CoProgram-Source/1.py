#!/usr/bin/env python3

# ncat -e ./1.py 202.38.93.111 10700

import sys
print(open('token.txt','r').read())

_p='(\([a-z][\+\-\*%/][a-z]\))|(\(-[a-z]\))'



f=open('co.log','w')

def lg(*args):
    s=' '.join([str(i) for i in args])
    f.write(s+'\n')
    return s

def pt(*args):
    s=lg(*args)
    print(s)
    return s

def ipt():
    x=input()
    lg(x)
    return x


x=ipt()
# x=ipt()

for i in range(1000):
    x=ipt()
    n=int(ipt())
    print()