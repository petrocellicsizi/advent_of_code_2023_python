one = open("one.txt", "r") 
text = one.read() 
sorok = text.split("\n") 
one.close()
k = 0
for i in sorok:
    c= False
    z= None
    y= None
    x=i
    for j in x:
        if j.isdigit():
            if c:
                y=j
            else:
                c=True
                z=j
    if(y==None):
        y=z
    k=k+int(y)+int(z)*10
    c= False
    z= None
    y= None
print(k)