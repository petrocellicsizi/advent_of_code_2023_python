with open("six.txt","r", encoding="utf-8") as file:
    for i,line in enumerate(file):
        if i==0:
            time=int("".join([x for x in line.strip().split() if x.isdecimal()]))
        else:
            distance="".join([x for x in line.strip().split() if x.isdecimal()])

c=0
time = time+1 if time%2==1 else time+2
for i in range(1,(time)//2):#1-től timeig
    pushtime=(time)-i
    runtime=(time)-pushtime
    distance1=pushtime*runtime
    if distance1>int(distance):
        c+=1
print(c*2)

    