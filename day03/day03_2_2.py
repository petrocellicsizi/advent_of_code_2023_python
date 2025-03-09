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
    csillagok=[]
    for lineid, line in enumerate (lines):
        for digitid, digit in enumerate (line):
                if digit=="*":
                    csillagok.append((lineid,digitid))
    for csillag in csillagok:
        counter=0
        egyes=0
        k=0
        for szam in szamok:
            if csillag[0]==szam[0] or csillag[0]-1==szam[0] or csillag[0]+1==szam[0]:
                if szam[2]<=csillag[1] and szam[3]>=csillag[1]:
                    if counter==0:
                        egyes=szam[1]
                        counter+=1
                    elif counter==1:
                        print(egyes,szam[1])
                        k=egyes*szam[1]
                    else:
                        break
                elif szam[2]<=csillag[1]-1 and szam[3]>=csillag[1]-1:
                    if counter==0:
                        egyes=szam[1]
                        counter+=1
                    elif counter==1:
                        print(egyes,szam[1])
                        k=egyes*szam[1]
                    else:
                        break
                elif szam[2]<=csillag[1]+1 and szam[3]>=csillag[1]+1:
                    if counter==0:
                        egyes=szam[1]
                        counter+=1
                    elif counter==1:
                        print(egyes,szam[1])
                        k=egyes*szam[1]
                    else:
                        break
        sum+=k
print(sum)