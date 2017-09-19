import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
pod=0
nod=0

for i in range(0,n):
    for j in range(0,n):
        if i==j:
            pod = pod + 1
            print int(a[i])
            
print pod           
