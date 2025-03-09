def convo(converter,seed,id,breakdown):
    breakdown=breakdown
    id=id
    conva=converter[1]
    convb=converter[1]+converter[2]-1
    seeda=seed[0]
    seedb=seed[1]
    seed2a=0
    seed2b=0
    if conva>seedb:
        return (False,False,id,breakdown)
    elif conva<=seedb and conva>seeda:
        seed2a=conva+(converter[0]-converter[1])
        seed2b=seedb+(converter[0]-converter[1])
        seedb=conva-1
        del breakdown[id]
        breakdown.insert(id,(seed2a,seed2b))
        breakdown.append((seeda,seedb))
        id+=1
        return(True,False,id,breakdown)
    elif convb>=seedb and conva<=seeda:
        seeda=seeda+(converter[0]-converter[1])
        seedb=seedb+(converter[0]-converter[1])
        breakdown.pop(id)
        breakdown.append((seeda,seedb))
        id+=1
        return (True,True,id,breakdown)
    elif seeda<=convb and seedb>convb:
        seed2a=seeda+(converter[0]-converter[1])
        seed2b=convb+(converter[0]-converter[1])
        seeda=convb+1
        breakdown[id]=(seed2a,seed2b)
        breakdown.append((seeda,seedb))
        id+=1
        return (True,False,id,breakdown)
    elif seeda>convb:
        return (False,False,id,breakdown)

with open("five.txt","r", encoding="utf-8") as file:
    lines = file.readlines()
    line1=lines[0]
    seeds=[]
    seednums=line1.split(" ")
    counter=1
    while len(seednums)>counter+1:
        a=int(seednums[counter])
        b=int(seednums[counter+1])
        counter+=2
        counterbent=a
        seeds.append((int(a),int(a)+int(b)-1))
    converters=[]
    converters1=[]
    converters2=[]
    converters3=[]
    converters4=[]
    converters5=[]
    converters6=[]
    converters7=[]
    borders=[]
    where_to_convert=0
    converteralles=[]
    for lineid, line in enumerate(lines):
        converter=[]
        if lineid==0:
            continue
        elif line=='\n':
            continue
        elif line[0].isdigit()==False:
            where_to_convert+=1
            continue
        else:
            line=line.split(" ")
            converter.append(int(line[0]))
            converter.append(int(line[1]))
            converter.append(int(line[2]))
            if where_to_convert==1:
                converters1.append(converter)
            elif where_to_convert==2:
                converters2.append(converter)
            elif where_to_convert==3:
                converters3.append(converter)
            elif where_to_convert==4:
                converters4.append(converter)
            elif where_to_convert==5:
                converters5.append(converter)
            elif where_to_convert==6:
                converters6.append(converter)
            elif where_to_convert==7:
                converters7.append(converter)
    converteralles.append(converters1)
    converteralles.append(converters2)
    converteralles.append(converters3)
    converteralles.append(converters4)
    converteralles.append(converters5)
    converteralles.append(converters6)
    converteralles.append(converters7)
    min=None
    for seedid,seed in enumerate(seeds):
        breakdown=[]
        breakdown.append(seed)
        for id, converter in enumerate(converteralles):
            length=len(converter)
            flake=(False,False,id,breakdown)
            counter=0
            id=0
            while id<len(breakdown):
                while counter<length:
                    flake=convo(converter[counter],breakdown[id],id,breakdown)
                    #print(breakdown,id)
                    breakdown=flake[3]
                    id=flake[2]
                    print(id)
                    if flake[0] == False and flake[1]== False:
                        counter+=1
                    elif flake[0] == True and flake[1]== True:
                        break
                    else:
                        continue 
                if counter==length:
                    id=len(breakdown)
        for a in breakdown:
            print(a)
            if min==None or min>a[0]:
                min=a[0]
    print(min)