def cal(i):
    x=i
    z = None
    y = None
    c = False
    first=10
    last=0
    counter=0
    for j in x:
        counter=+1
        if j.isdigit():
            if c:
                y=j
                last=counter
            else:
                c=True
                z=j
                first=counter
    if(y==None):
        last=first
        y=z
    k=[first,last,z,y]
    return k

one = open("one.txt", "r") 
text = one.read() 
sorok = text.split("\n") 
one.close()
listageci={"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
k=0
minid=None
minszam=10
maxid=None
maxszam=0
canbemore=True
z=None
for i in sorok:
    counter1=0
    z=cal(i)
    for n in listageci:
        counter1+= 1
        if n != None and n in i:
            e=i.find(n)
            if e<minszam:
                minszam=e
                minid=counter1
            if e>maxszam:
                maxszam=e
                maxid=counter1
            while canbemore:
                if n != None and n in i[e+1:-1]:
                    e=i.find(n)
                    if e<minszam:
                        minszam=e
                        minid=counter1
                    if e>maxszam:
                        maxszam=e
                        maxid=counter1
                else:
                    canbemore=False
            if(minid>z[0]):
                minszam=z[2]
            if(maxid<z[1]):
                maxszam=z[3]
            k=k+minszam*10+maxszam
        else:
            for i in sorok:
                x=i
                c= False
                z= None
                y= None
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
print(k)
