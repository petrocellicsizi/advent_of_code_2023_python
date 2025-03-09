def linecheck(line):
    for d in line:
        if d.isdigit():
            continue
        elif d==".":
            continue
        else:
            return True
    return False

def digitcheck(d):
    if d.isdigit():
        return False
    elif d==".":
        return False
    else:
        return True

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

with open("input3.txt","r", encoding="utf-8") as file:
    lines = file.readlines()
    last_line = lines[-1]
    sum=0
    for lineid, line in enumerate (lines):
        if lineid==0:
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
                            if firstid!=0:
                                firstid-=1
                            if utolsoid<len(line)-1:
                                utolsoid+=1
                            if digitcheck(str(line[firstid])):
                                vanjel=True
                            if digitcheck(str(line[utolsoid-1])):
                                vanjel=True
                            if linecheck(lines[lineid+1][firstid:utolsoid]):
                                vanjel=True
                            if vanjel:
                                sum+=szamunk
                        szamunk=0
        elif line==last_line:
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
                            if firstid!=0:
                                firstid-=1
                            if utolsoid<len(line)-1:
                                utolsoid+=1
                            if digitcheck(str(line[firstid])):
                                vanjel=True
                            if digitcheck(str(line[utolsoid-1])):
                                vanjel=True
                            if linecheck(lines[lineid-1][firstid:utolsoid]):
                                vanjel=True
                            if vanjel:
                                sum+=szamunk
                        szamunk=0
        else:
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
                            if firstid!=0:
                                firstid-=1
                            if utolsoid<len(line)-1:
                                utolsoid+=1
                            if digitcheck(str(line[firstid])):
                                vanjel=True
                            if digitcheck(str(line[utolsoid-1])):
                                vanjel=True
                            if linecheck(lines[lineid-1][firstid:utolsoid]):
                                vanjel=True
                            if linecheck(lines[lineid+1][firstid:utolsoid]):
                                vanjel=True
                            if vanjel:
                                sum+=szamunk
                        szamunk=0    
    print(sum)