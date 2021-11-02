#!/usr/bin/env python3

# ncat -e ./1.py 202.38.93.111 10700

import sys
print(open('token.txt','r').read())

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

import re

d=None
uid=None

def d_append(k:str,v:int,id:str)->int:
    # global d,uid
    v%=1<<36
    if k in uid and uid[k]<id:
        return d[k]!=v
    uid[k]=id
    d[k]=v
    return 0

def d_clear(l:list,id:str):
    # global d,uid
    for k in re.findall('[a-z]',str(l)):
        if k in uid and uid[k]>=id:
            del uid[k]

def d_check(k:str,id:str)->int:
    # global d,uid
    if k in uid and uid[k]<id:
        return d[k]
    return None

l_i=[0,]
for i in range(5):
    l_i.append(i+1)
    l_i.append(-i-1)

def g(l:list,ans:int,id:str)->int:
    ans%=1<<36
    if isinstance(l,str):
        return d_append(l,ans,id)

    if len(l)==2:
        if l[0]!='-':
            raise RuntimeError('WTF.l: '+str(l))
        return g(l[1],-ans,id+'1')

    if len(l)!=3:
        raise RuntimeError('WTF.l: '+str(l))


    if l[1]=='+':
        if l[0]==l[2]:
            if ans&1:
                return 1
            if g(l[0],ans//2,id+'0'):
                d_clear(l[0],id+'0')
            elif g(l[2],ans//2,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0
            return 1
        
        if isinstance(l[0],str):
            v=d_check(l[0],id+'0')
            if v is not None:
                if g(l[2],ans-v,id+'2'):
                    d_clear(l[2],id+'2')
                else:
                    return 0
                return 1

        if isinstance(l[2],str):
            v=d_check(l[2],id+'2')
            if v is not None:
                if g(l[0],ans-v,id+'0'):
                    d_clear(l[0],id+'0')
                else:
                    return 0
                return 1

        for i in l_i:
            if g(l[0],ans-i,id+'0'):
                d_clear(l[0],id+'0')
            elif g(l[2],i,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0

            if g(l[0],i,id+'0'):
                d_clear(l[0],id+'0')
            elif g(l[2],ans-i,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0
        return 1


    if l[1]=='-':
        if l[0]==l[2]:
            if ans:
                return 1
            return 0

        if isinstance(l[0],str):
            v=d_check(l[0],id+'0')
            if v is not None:
                if g(l[2],v-ans,id+'2'):
                    d_clear(l[2],id+'2')
                else:
                    return 0
                return 1

        if isinstance(l[2],str):
            v=d_check(l[2],id+'2')
            if v is not None:
                if g(l[0],v+ans,id+'0'):
                    d_clear(l[0],id+'0')
                else:
                    return 0
                return 1

        for i in l_i:
            if g(l[0],ans+i,id+'0'):
                d_clear(l[0],id+'0')
            elif g(l[2],i,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0
        return 1

    if l[1]=='*':
        if l[0]==l[2]:
            if ans<0:
                return 1
            p=int(ans**0.5)
            if p*p!=ans:
                return 1
            if g(l[0],p,id+'0'):
                d_clear(l[0],id+'0')
            elif g(l[2],p,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0
            return 1

        if ans==0:
            if g(l[0],0,id+'0'):
                d_clear(l[0],id+'0')
            else:
                return 0
            if g(l[2],0,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0
            return 1

        if isinstance(l[0],str):
            v=d_check(l[0],id+'0')
            if v is not None:
                if v==0 or ans%v:
                    return 1
                if g(l[2],ans//v,id+'2'):
                    d_clear(l[2],id+'2')
                else:
                    return 0
                return 1

        if isinstance(l[2],str):
            v=d_check(l[2],id+'2')
            if v is not None:
                if v==0 or ans%v:
                    return 1
                if g(l[0],ans//v,id+'0'):
                    d_clear(l[0],id+'0')
                else:
                    return 0
                return 1

        if g(l[0],ans,id+'0'):
            d_clear(l[0],id+'0')
        elif g(l[2],1,id+'2'):
            d_clear(l[2],id+'2')
        else:
            return 0
        if g(l[0],1,id+'0'):
            d_clear(l[0],id+'0')
        elif g(l[2],ans,id+'2'):
            d_clear(l[2],id+'2')
        else:
            return 0
        return 1


    if l[1]=='/':
        if l[0]==l[2]:
            if ans!=1:
                return 1
            return 0

        if ans==0:
            if g(l[0],0,id+'0'):
                d_clear(l[0],id+'0')
            else:
                return 0

            for i in range(1,10):
                if g(l[2],(1<<36)-i,id+'2'):
                    d_clear(l[2],id+'2')
                else:
                    return 0
            return 1
        
        if ans==(1<<36)-1:
            if g(l[2],0,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0

        if isinstance(l[0],str):
            v=d_check(l[0],id+'0')
            if v is not None:
                if v==0 or v<ans:
                    return 1
                p=v//ans
                if v//p!=ans:
                    return 1
                if g(l[2],p,id+'2'):
                    d_clear(l[2],id+'2')
                else:
                    return 0
                return 1

        if isinstance(l[2],str):
            v=d_check(l[2],id+'2')
            if v is not None:
                if v==0:
                    return 1
                for i in range(ans*v,min((ans+1)*v-1,ans*v+10)):
                    if i>=1<<36:
                        return 1
                    if g(l[0],i,id+'0'):
                        d_clear(l[0],id+'0')
                    else:
                        return 0
                return 1

        if g(l[0],ans,id+'0'):
            d_clear(l[0],id+'0')
        elif g(l[2],1,id+'2'):
            d_clear(l[2],id+'2')
        else:
            return 0
        return 1

    if l[1]=='%':
        if l[0]==l[2]:
            if ans:
                return 1
            return 0

        if ans==0:
            if g(l[0],0,id+'0'):
                d_clear(l[0],id+'0')
            else:
                return 0

        if ans==(1<<36)-1:
            if g(l[2],0,id+'2'):
                d_clear(l[2],id+'2')
            else:
                return 0
            return 1
        
        
        if isinstance(l[0],str):
            v=d_check(l[0],id+'0')
            if v is not None:
                p=v-ans
                if p<=ans:
                    return 1
                if g(l[2],p,id+'2'):
                    d_clear(l[2],id+'2')
                else:
                    return 0
                return 1
                # not all cases

        if isinstance(l[2],str):
            v=d_check(l[2],id+'2')
            if v is not None:
                if v<=ans:
                    return 1
                for i in range(10):
                    p=i*v+ans
                    if p>=1<<36:
                        return 1
                    if g(l[0],p,id+'0'):
                        d_clear(l[0],id+'0')
                    else:
                        return 0
                return 1
        
        if g(l[0],ans,id+'0'):
            d_clear(l[0],id+'0')
        elif g(l[2],0,id+'2'):
            d_clear(l[2],id+'2')
        else:
            return 0
        return 1

    raise RuntimeError('WTF.l: '+str(l))



x=ipt()
_n=0
while True:
    s=ipt()
    ans=int(ipt())
    _s=re.sub('[^\(\)]',lambda x:'"'+x.group()+'",',s).replace(')','],').replace('(','[')[:-1]
    l=eval(_s)
    lg(l)
    d={i:1 for i in re.findall('[a-z]',s)}
    uid=dict()
    code=g(l,ans,'')
    _n-=code-1
    lg(d,code,_n)
    _send=' '.join(i+'='+str(d[i]) for i in d)
    pt(_send)
    for i in d:
        s=s.replace(i,str(d[i]))
    try:
        s+='='+str(eval(s))
    except:
        s+='=NaN'
    lg(s)
    lg()
