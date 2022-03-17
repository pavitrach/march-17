b=input("Enter your password\n")
m=list(b)
y=[]
l=0
u=0
d=0
s=0
for i in m:
    if (i.islower()):
        l=l+1
    elif (i.isupper()):
        u=u+1
    elif (i.isdigit()):
        d=d+1
    else: 
        s=s+1
if l==0 or u==0 or d==0 or s==0:
    print("Invalid password\n password should contain atleast 1 uppercase,lowercase,digit and symbol")
else:
    print("valid password")
