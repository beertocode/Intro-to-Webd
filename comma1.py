n=int(raw_input("enter no. of items in list"))
l=[]
for i in range(n):
    l.append(raw_input())
def comma(s):
    L=list(s)
    t=len(L)/3
    for i in range(t):
        L.insert((-3*i)-(3+i),",")
    if len(L)%4==0:
        L.pop(0)
        return "".join(L)
    else:
        return "".join(L)
m=map(comma,l)
for i in range(len(m)):
    print m[i]
        
