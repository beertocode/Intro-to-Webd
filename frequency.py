def frequency(L):
    
    s=set(L)
    l1=list(s)
    l1.sort()
    for i in range(len(s)):
        c=L.count(l1[i])
        print (l1[i],":",c)
w=input().split()
frequency(w)
        
        
        
