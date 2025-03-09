with open("four.txt","r", encoding="utf-8") as file:
    lines = file.readlines()
    for lineid, line in enumerate(lines,1):
        data=line.strip().split(" ")
        cardnumber=0
        itshalftime=False
        winningnumbers=[]
        yournumbers=[]
        cardnames=line.split(":")
        for cardname in cardnames:        
            cardnumber=cardnames[0].replace(" ","")[4:]
        print(cardnumber)