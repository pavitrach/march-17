b=input()
l=list(b)
y=[]
for i in l:
    if i=='a'or i=='A'or i=='e'or i=='E'or i=='i'or i=='I'or i=='o'or i=='O'or i=='u'or i=='U':
        continue
    else:
        y.append(i)
for i in y:
    print(i,end='')

        
