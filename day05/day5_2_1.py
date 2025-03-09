def convo(seed,converter):
    if seed<converter[1] or seed>converter[1]+converter[2]-1:
        return (seed,False)
    else:
        seed=seed+(converter[0]-converter[1])
        return (seed,True)

with open("five.txt","r", encoding="utf-8") as file:
    lines = file.readlines()
    line1=lines[0]
    seeds=[]
    seednums=line1.strip().split(" ")
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
    min=0
    counter1=1
    while len(seednums)>counter1+1:
        a=int(seednums[counter1])
        b=int(seednums[counter1+1])
        print(counter1,len(seednums))
        counter1+=2
        counterbent=a
        while counterbent<a+b+1:
            newnum=counterbent
            for id, converter in enumerate(converteralles):
                    length=len(converter)
                    flake=(newnum,False)
                    counter=0
                    while counter<length:
                        flake=convo(int(newnum),converter[counter])
                        newnum=flake[0]
                        if flake[1]:
                            counter = length
                        else:
                            counter+=1
                    print("NYUGI")
            if min==0 or newnum<min:
                min=newnum
            counterbent+=1
    print(min)