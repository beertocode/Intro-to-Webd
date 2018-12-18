N=int(input())
l=[]
for i in range(N):
    p=input().split()
    l.append(p)
c=len(l)
k=[]
v=[]
for o in range(c):
    k.append(l[o][0])
    v.append(l[o][1])
l1=list(set(k))
q=len(l1)
for h in range(q):
    t=k.count(l1[h])
    s= k.index(l1[h])
    f=int(v[s])
    a=t*f
    print (l1[h]," ",a)
    

