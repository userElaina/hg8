#!/usr/bin/env python3

# ncat -e ./t2.py 202.38.93.111 10800

import sys
print(open('token.txt','r').read())
f=open('t2.log','w')

def lg(*args):
    s=' '.join([str(i) for i in args])
    f.write(s+'\n')
    f.flush()
    return s

def pt(*args):
    s=lg(*args)
    print(s)
    return s

def ipt():
    x=input()
    lg(x)
    if 'flag' in x:
        raise ValueError(x)
    return x

import re

def func(ans:int)->str:
    if ans==0:
        return '(x-x)'

    s='(x/x)'
    for i in bin(ans)[3:]:
        if i=='1':
            s='((x/x+x/x)*'+s+'+x/x)'
        else:
            s= '(x/x+x/x)*'+s+''
    return s

for _i in range(20):
    _=''
    for i in range(5):
        s=ipt()
        while not s.startswith('x'):
            s=ipt()
        a=re.findall('[0-9]+',s)
        x=int(a[0])
        y=int(a[1])
        ans=int(a[2])
        _x=func(x)
        _y=func(y)
        _ans=func(ans)
        if i:
            _='if((x<='+_x+'&&'+_x+'<=x),('+_ans+'),('+_+'))'
        else:
            _=_ans
    pt(_)