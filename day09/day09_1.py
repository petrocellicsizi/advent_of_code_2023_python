szamok=[]
data=[]
goon=True
ujszam=[]
with open("try.txt","r", encoding="utf-8") as file:
    for i,line in enumerate(file):
        data.append(line.strip().split())
        szamok.append(data)
        c=1
        while goon:
            for szamid,szam in enumerate(szamok[c-1]):
                if szamid-1==len(szamok[c-1]):
                    break
                else:
                    szamok[c][szamid]=szamok[c-1][szamid+1]-szam
        if all(ele == 0 for ele in szamok[c]):
            goon=False
print(szamok)