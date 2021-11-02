import numpy as np

m=np.zeros((144,145),dtype=int)

f=open('n2.txt','w')

l=[int(j) for i in open('2.txt','r').read().splitlines() for j in i.split()]

con=[26,28,38,39,40,50,52,79,80,81,91,103,105,115,116,117]

for i,j in np.ndindex(12,12):
    y=i*12+j
    if y in con:
        continue
    m[y,y]=3
    if i>=1:
        m[(i-1)*12+j,y]=2
    if i<=10:
        m[(i+1)*12+j,y]=2
    if i>=2:
        m[(i-2)*12+j,y]=1
    if i<=9:
        m[(i+2)*12+j,y]=1
    if j>=1:
        m[i*12+j-1,y]=2
    if j<=10:
        m[i*12+j+1,y]=2
    if j>=2:
        m[i*12+j-2,y]=1
    if j<=9:
        m[i*12+j+2,y]=1

m=list(m.T)
for i in con[::-1]:
    m=m[:i]+m[i+1:]
m=np.array(m).T

for _n,i in enumerate(m):
    i[-1]=l[_n]
    f.write(' '.join(map(str,i))+'\n')

f2=open('n3.txt','w')

m=[list(map(int,i.split())) for i in open('n2.txt','r').read().splitlines()]

for i in m:
    f2.write(str(i)+'\n')

