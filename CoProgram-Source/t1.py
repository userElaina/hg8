#!/usr/bin/env python3

# ncat -e ./t1.py 202.38.93.111 10700

import sys
print(open('token.txt','r').read())
f=open('t1.log','w')

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

l=None
l2=None
d=None
s=None
ans=None

def p2v(x:str)->str:
    x=x[1:-1]
    if x.startswith('-'):
        x=int(x)%(1<<36)
    elif '+' in x or '-' in x or '*' in x:
        x=eval(x)%(1<<36)
    elif '/' in x:
        y=x.split('/')
        x=((1<<36)-1) if y[1]=='0' else (int(y[0])//int(y[1]))
    elif '%' in x:
        y=x.split('%')
        x=int(y[0]) if y[1]=='0' else (int(y[0])%int(y[1]))
    else:
        raise Exception('WTF.p2v: '+x)
    return str(x)

def v()->bool:
    # global d,s,ans
    _s=s
    for i in d:
        _s=_s.replace(i,str(d[i]%(1<<36)))
    __s=_s
    _p='\([0-9]*[\+\-\*%/][0-9]+\)'
    _n=0
    while True:
        _n+=1
        if _n>10:
            raise Exception('WTF.v: '+str(_n)+' '+_s)
        _s=re.sub(_p,lambda x:p2v(x.group()),_s)
        try:
            p=int(_s)
            if p==ans:
                lg(__s,p)
                return True
            else:
                return False
        except:
            None

_dfs_n=0
def dfs(n:int)->bool:
    global _dfs_n
    _dfs_n+=1
    if not _dfs_n%100000:
        lg(_dfs_n,d)
    if _dfs_n>2333333:
        return False
    # global l,l2,d,s,ans
    if n==len(l):
        return v()
    k=l[n]
    for i in l2:
        d[k]=i
        if dfs(n+1):
            return True
    return False


x=ipt()
_m=0
_n=0
while True:
    s=ipt()
    ans=int(ipt())
    l=list()
    d=dict()
    for i in re.findall('[a-z]',s):
        if i not in l:
            l.append(i)
            d[i]=0

    l2=[0,1,-1]
    if ans not in l2:
        l2=l2[:3]+[ans,-ans]
    p=ans//2
    if not ans&1 and '+' in s and p not in l2:
        l2+=[p,-p]
    p=int(ans**0.5)
    if p*p==ans and '*' in s and p not in l2:
        l2+=[p,]
    l2=[i%(1<<36) for i in l2]

    lg('max:',len(l2)**len(l))
    _dfs_n=0
    code=dfs(0)
    _m+=1
    _n+=1 if code else 0
    lg(d,code,_n,'/',_m)
    pt(' '.join(i+'='+str(d[i]) for i in d))
    lg()
