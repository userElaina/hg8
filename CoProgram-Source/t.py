
import re

lg=print

ans=44998295456
s='(((x/k)*(y*i))*((-x)+(z/j)))'

d={
    'x':0,
    'k':0,
    'y':1,
    'i':68719476735,
    'z':44998295456,
    'j':1,
}

def p2v(x:str)->str:
    x=x[1:-1]
    _=x
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
    # lg(_,x)
    return str(x)

def v()->bool:
    # global d,s,ans
    _s=s
    for i in d:
        _s=_s.replace(i,str(d[i]))
    __s=_s
    _p='\([0-9]*[\+\-\*%/][0-9]+\)'
    _n=0
    while True:
        _n+=1
        if _n>30:
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

print(v())