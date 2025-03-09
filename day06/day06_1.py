with open("six.txt","r", encoding="utf-8") as file:
    for i,line in enumerate(file):
        if i==0:
            times=[int(x) for x in line.strip().split() if x.isdecimal()]
        else:
            distances=[int(x) for x in line.strip().split() if x.isdecimal()]
sum=1
for id,time in enumerate (times):
    c=0
    for i in range(1,(time)):#1-től timeig
        pushtime=time-i
        runtime=time-pushtime
        distance=pushtime*runtime
        if distance>distances[id]:
            c+=1
    sum*=c
    print(c*2)
print(sum)
print(9//2)
