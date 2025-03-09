def first(number,lastid):
    nincsmeg=True
    tizeshatvany=0
    while nincsmeg:
        if number>=10**tizeshatvany and number<10**(tizeshatvany+1):
            nincsmeg=True
            return lastid-(tizeshatvany)
        else:
            tizeshatvany+=1
            continue

def digitcheck(sorid,digitid):
    for szamid,szam in enumerate(szamok):
        if szam[0]==sorid:
            if int(szam[2])<=int(digitid) and int(szam[3])>=int(digitid):
                return szamid

with open("three.txt","r", encoding="utf-8") as file:
    lines = file.readlines()
    last_line = lines[-1]
    szamok=[]
    for lineid, line in enumerate (lines):
        betuid=0
        while betuid<len(line):
            ezszam,utsovolt,vanjel=True,False,False
            kezdes,szamunk,utolsoid=0,0,0
            while ezszam:
                if line[betuid].isdigit():
                    szamunk*=10
                    szamunk+=int(line[betuid])
                    if betuid+1<len(line):
                        betuid+=1
                    else:
                        betuid+=1
                        utsovolt=True
                else:
                    ezszam=False
                    if betuid+1<len(line):
                        betuid+=1
                    else:
                        betuid+=1
                        utsovolt=True
                    if(szamunk>0):
                        utolsoid=betuid-1
                        firstid=first(szamunk,utolsoid)-1
                        szamok.append((lineid,szamunk,firstid,utolsoid-1))
                    szamunk=0
    sum=0
    for lineid, line in enumerate (lines):
        if lineid==0:
            good=[]
            for digitid, digit in enumerate (line):
                if digit=="*":
                    if digitid>0:
                        print("bent")
                        if digitcheck(lineid,digitid-1)!=None:
                            good.append(digitcheck(lineid,digitid-1))
                        if digitcheck(lineid+1,digitid-1)!=None and digitcheck(lineid+1,digitid-1)!=digitcheck(lineid+1,digitid):
                            good.append(digitcheck(lineid+1,digitid-1))
                    if digitid<len(line)-1:
                        print("bent")
                        if digitcheck(lineid,digitid+1)!=None:
                            good.append(digitcheck(lineid,digitid+1))
                        if digitcheck(lineid+1,digitid+1)!=None:
                            good.append(digitcheck(lineid+1,digitid+1))
                    if digitcheck(lineid+1,digitid)!=None and digitcheck(lineid+1,digitid)!=digitcheck(lineid+1,digitid+1):
                        good.append(digitcheck(lineid+1,digitid))
                    print(good)
                    if len(good)==2:
                        sum+=szamok[good[0]][1]*szamok[good[1]][1]
        elif line==last_line:
            good=[]
            for digitid, digit in enumerate (line):
                if digit=="*":
                    if digitid>0:
                        if digitcheck(lineid,digitid-1)!=None:
                            good.append(digitcheck(lineid,digitid-1))
                        if digitcheck(lineid-1,digitid-1)!=None and digitcheck(lineid-1,digitid-1)!=digitcheck(lineid-1,digitid):
                            good.append(digitcheck(lineid-1,digitid-1))
                    if digitid<len(line)-1:
                        if digitcheck(lineid,digitid+1)!=None:
                            good.append(digitcheck(lineid,digitid+1))
                        if digitcheck(lineid-1,digitid+1)!=None:
                            good.append(digitcheck(lineid-1,digitid+1))
                    if digitcheck(lineid-1,digitid)!=None and digitcheck(lineid+1,digitid)!=digitcheck(lineid+1,digitid+1):
                        good.append(digitcheck(lineid-1,digitid))
                    good=list(set(good))
                    if len(good)==2:
                        sum+=szamok[good[0]][1]*szamok[good[1]][1]
        else:
            good=[]
            for digitid, digit in enumerate (line):
                if digit=="*":
                    if digitid>0:
                        if digitcheck(lineid,digitid-1)!=None:
                            good.append(digitcheck(lineid,digitid-1))
                        if digitcheck(lineid+1,digitid-1)!=None and digitcheck(lineid+1,digitid-1)!=digitcheck(lineid+1,digitid):
                            good.append(digitcheck(lineid+1,digitid-1))
                        if digitcheck(lineid-1,digitid-1)!=None and digitcheck(lineid-1,digitid-1)!=digitcheck(lineid-1,digitid):
                            good.append(digitcheck(lineid-1,digitid-1))
                    if digitid<len(line)-1:
                        if digitcheck(lineid,digitid+1)!=None:
                            good.append(digitcheck(lineid,digitid+1))
                        if digitcheck(lineid+1,digitid+1)!=None:
                            good.append(digitcheck(lineid+1,digitid+1))
                        if digitcheck(lineid-1,digitid+1)!=None:
                            good.append(digitcheck(lineid-1,digitid+1))
                    if digitcheck(lineid+1,digitid)!=None and digitcheck(lineid+1,digitid)!=digitcheck(lineid+1,digitid+1):
                        good.append(digitcheck(lineid+1,digitid))
                    if digitcheck(lineid-1,digitid)!=None and digitcheck(lineid+1,digitid)!=digitcheck(lineid+1,digitid+1):
                            good.append(digitcheck(lineid-1,digitid))
                    good=list(set(good))
                    if len(good)==2:
                        sum+=szamok[good[0]][1]*szamok[good[1]][1]
print(sum)