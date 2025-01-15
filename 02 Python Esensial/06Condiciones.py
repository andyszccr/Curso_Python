a=1
b=1
c=True

d=10
e=5
f=1

if(a>b):
    print("a is greater than b")
elif(a==b):
    print("b is equal to a")
else:
    print("b is greater than a")
    

if(c):
    print("c is true")
else:
    print("c is false")
    
if(type(c) is bool):
    print("c is a boolean")
    
    
if d>e and d>f:
    print("d is the greatest")
elif e>d and e>f:
    print("e is the greatest")
else:
    print("f is the greatest")
    