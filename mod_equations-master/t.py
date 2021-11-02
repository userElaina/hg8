a=[int(j) for i in open('2.txt','r').read().splitlines() for j in i.split()]

print(len(a),a)