n=int(raw_input("enter limit:"))
f0=0
f1=1
s=0

if n==1:
    print f0
else:
    while s<n:
        print (f0)
        f=f0+f1
        
        f0=f1
        f1=f
        s+=1
