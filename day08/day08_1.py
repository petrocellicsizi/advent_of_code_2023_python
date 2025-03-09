with open("try2.txt","r", encoding="utf-8") as file:
    data=[]
    vissz=[]
    stepc=0
    names=[]
    leftandrights=[]
    id=0
    next=None
    gotcha=False
    counter=0
    for i,line in enumerate(file):
        if i==0:
            directions=line
        elif i==1:
            continue
        else:
            data=(line.strip().split("="))
            names.append((data[0].strip(" "),i))
            if data[0].strip(" ")=="AAA":
                id=i-2
            leftandrights.append((data[1][2:5],data[1][7:10]))
    while gotcha==False:
        vissz.append((directions[counter],counter))
        if directions[counter]=='L':
            next=leftandrights[id][0]
            print(directions[counter],next)
            stepc+=1
        elif directions[counter]=='R':
            next=leftandrights[id][1]
            print(directions[counter],next)
            stepc+=1
        counter+=1
        if next=='ZZZ':
            gotcha=True
        for i,needed in enumerate(names):
            if needed[0]==next:
                id=i
            else:
                continue
        if len(directions)==counter+1:
            counter=0
    print(stepc)
        
