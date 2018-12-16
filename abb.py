def abb(s):
    l=len(s)
    
    m=""
    for i in range(l):
        if s[i]==" ":
            m=m+(s[i+1])
    return (s[0])+m
n=int(raw_input("enter no. of items in list"))
l=[]
for i in range(n):
    l.append(raw_input())
k=map(abb,l)
for j in range(len(k)):
    print k[j]

    
    



        
