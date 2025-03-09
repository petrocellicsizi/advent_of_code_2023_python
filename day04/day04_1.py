with open("four.txt","r+", encoding="utf-8") as file:
    lines = file.readlines()
    sum=0
    for lineid, line in enumerate(lines,1):
        data=line.strip().split(" ")
        itshalftime=False
        winningnumbers=[]
        yournumbers=[]
        for digit in data:
            if digit.isdigit() and itshalftime:
                yournumbers.append(int(digit))
            if digit=="|":
                itshalftime=True
            if digit.isdigit() and itshalftime==False:
                winningnumbers.append(int(digit))
        counter=0
        for yournumber in yournumbers:
            for winnumber in winningnumbers:
                if yournumber==winnumber:
                    counter+=1
        if counter>0:
            sum+=2**(counter-1)
    print(sum)