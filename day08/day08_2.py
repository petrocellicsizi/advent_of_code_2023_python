with open("eight.txt","r", encoding="utf-8") as file:
    data=[]
    vissz=[]
    stepc=0
    names=[]
    leftandrights=[]
    good=[]
    id=0
    next=None
    gotcha=False
    counter=0
    starters=[]
    starterids=[]
    for i,line in enumerate(file):
        if i==0:
            directions=line
        elif i==1:
            continue
        else:
            data=(line.strip().split("="))
            names.append((data[0].strip(" "),i-2))
            if data[0].strip(" ")[2]=="A":
                starters.append(data[0].strip(" "))
                starterids.append(i-2)
            leftandrights.append((data[1][2:5],data[1][7:10]))
    while gotcha==False:
        good=[]
        for stid, starter in enumerate(starters):
            id=starterids[stid]
            if directions[counter]=='L':
                next=leftandrights[id][0]
            elif directions[counter]=='R':
                next=leftandrights[id][1]
            for i,needed in enumerate(names):
                if needed[0]==next:
                    starterids[stid]=i
            starters[stid]=(next)
            next01=starterids[stid]
            good.append((next,next01))
        stepc+=1
        counter+=1
        hm=0
        for starter in starters:
            if starter[2]=="Z":
                hm+=1
        if hm==len(starters): 
            gotcha=True
        if len(directions)==counter+1:
            counter=0
        print(stepc)
print(stepc)
        
