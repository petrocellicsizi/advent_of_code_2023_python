with open("four.txt","r+", encoding="utf-8") as file:
    lines = file.readlines()
    i=0
    cardnumbers,counts,pieces=[],[],[]
    sum=0
    for lineid, line in enumerate(lines,1):
        data=line.strip().split(" ")
        cardname=line.split(":")
        itshalftime=False
        winningnumbers=[]
        yournumbers=[]
        cardnames=line.split(":")
        for cardname in cardnames:        
            cardnumber=cardnames[0].replace(" ","")[4:]
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
        cardnumbers.append(int(cardnumber))
        counts.append(int(counter))
        pieces.append(1)
        i+=1
    for xid, x in enumerate(cardnumbers):
        count=counts[xid]
        while count>0:
            pieces[xid+count]+=pieces[xid]
            count-=1
        sum+=pieces[xid]
    print(sum)