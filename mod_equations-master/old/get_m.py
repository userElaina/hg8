import numpy as np

m=np.zeros((144,145),dtype=int)

f=open('m2.txt','w')

l=[int(j) for i in open('2.txt','r').read().splitlines() for j in i.split()]

for i,j in np.ndindex(12,12):
    y=i*12+j
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



for _n,i in enumerate(m):
    i[-1]=l[_n]
    f.write(' '.join(map(str,i))+'\n')

f2=open('m3.txt','w')

m=[list(map(int,i.split())) for i in open('m2.txt','r').read().splitlines()]

for i in m:
    f2.write(str(i)+'\n')

