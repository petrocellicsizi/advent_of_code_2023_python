with open("two.txt", "r", encoding="utf-8") as file:
    szum=0
    for gameid, line in enumerate(file, 1):
        maxb,maxg,maxr=0,0,0
        data=line.strip().split(":")
        pulls=data[1].split(";")
        for j in pulls:
            onehand=j.split(",")
            num_colour=j.split(" ")
            for id, i in enumerate (num_colour):
                if "green"==num_colour[id] or "green,"==num_colour[id]:
                    if int(num_colour[id-1])>maxg:
                        maxg=int(num_colour[id-1])
                if "red"==num_colour[id] or "red,"==num_colour[id]:
                    if int(num_colour[id-1])>maxr:
                        maxr=int(num_colour[id-1])
                if "blue"==num_colour[id] or "blue,"==num_colour[id]:
                    if int(num_colour[id-1])>maxb:
                        maxb=int(num_colour[id-1])
        szum+= (maxg * maxb * maxr)
print(szum)
                