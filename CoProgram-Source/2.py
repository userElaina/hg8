s=open('2.txt','r').read().split('\n')

d=dict()
l=set()

for i,x in enumerate(s):
    if x.startswith('('):
        l.add(x)
        try:
            n=int(s[i+1])
        except:
            continue
        if x in d:
            if n not in d[x]:
                d[x].append(n)
        else:
            d[x]=[n,]

import json

s=json.dumps(d,indent=4)
open('2.json','w').write(s)

import re
import sympy
f=open('3.txt','w')
_n=0
for i in sorted(l):
    d=dict()
    for j in re.findall('[\+\-\%][a-z]',i):
        d.setdefault(j[-1],0)
    for j in re.findall('[/\*\%][a-z]',i):
        d.setdefault(j[-1],1)
    for j in re.findall('[a-z]',i):
        d.setdefault(j,0)
    a=re.findall('^[^a-z]*[a-z]',i)[0]
    n=False
    for j in a:
        if j=='-':
            n=~n
    d[a[-1]]='-_' if n else '_'
    
    s=i+'\n'
    i=re.sub('z-z')
    print(i)
    # for j in d:
    #     s+=j+'='+str(d[j])+' '
    # s=s[:-1]+'\n'
    s+=str(d).replace(' ','')+'\n'
    s+=str(sympy.simplify(i)).replace(' ','')+'\n'
    _n+=1
    f.write(s)
