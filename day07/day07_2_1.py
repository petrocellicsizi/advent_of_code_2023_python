Dict ={}#'A':14,'K':13,'Q':12,'J':11,'T':10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2
Dict['2']=2
Dict['3']=3
Dict['4']=4
Dict['5']=5
Dict['6']=6
Dict['7']=7
Dict['8']=8
Dict['9']=9
Dict['T']=10
Dict['J']=1
Dict['Q']=12
Dict['K']=13
Dict['A']=14

def j_counter(hand):
  counter=0
  for x in hand:
    if x=='J':
      counter+=1
  return counter     
  
def isfiveofakind(hand):
  hand=str(hand)
  counter=0
  max=0
  while counter<len(hand):
    if max<hand.count(hand[counter]):
      max=hand.count(hand[counter])
    counter+=1
  return all(ele == hand[0] for ele in hand) or max==4 and j_counter(hand)==1 or len(set(hand))+3 == len(hand) and max==3 and j_counter(hand)==2 or len(set(hand))+3 == len(hand) and max==3 and j_counter(hand)==3 or max==4 and j_counter(hand)==4

def isfourofakind(hand):
  hand=str(hand)
  counter=0
  max=0
  while counter<len(hand):
    if max<hand.count(hand[counter]):
      max=hand.count(hand[counter])
    counter+=1
  return max==4 and j_counter(hand)==0 or max==3 and len(set(hand))+2 == len(hand) and j_counter(hand)==1 or len(set(hand))+2 == len(hand) and max==2 and j_counter(hand)==2 or max==3 and len(set(hand))+2 == len(hand) and j_counter(hand)==3

def isfullhouse(hand):
  hand=str(hand)
  counter=0
  max=0
  while counter<len(hand):
    if max<hand.count(hand[counter]):
      max=hand.count(hand[counter])
    counter+=1
  return len(set(hand))+3 == len(hand) and max==3 and j_counter(hand)==0 or len(set(hand))+2 == len(hand) and max==2 and j_counter(hand)==1

def isthreeofakind(hand):
  hand=str(hand)
  counter=0
  max=0
  while counter<len(hand):
    if max<hand.count(hand[counter]):
      max=hand.count(hand[counter])
    counter+=1
  return max==3 and len(set(hand))+2 == len(hand) and j_counter(hand)==0 or len(set(hand))+1 == len(hand) and j_counter(hand)==1 or len(set(hand))+1 == len(hand) and j_counter(hand)==2

def istwopair(hand):
  hand=str(hand)
  counter=0
  max=0
  while counter<len(hand):
    if max<hand.count(hand[counter]):
      max=hand.count(hand[counter])
    counter+=1
  return len(set(hand))+2 == len(hand) and max==2 and j_counter(hand)==0

def isonepair(hand):
  return len(set(hand))+1 == len(hand) and j_counter(hand)==0 or len(set(hand)) == len(hand) and j_counter(hand)==1
    
def ishighcard(hand):
  return len(set(hand)) == len(hand) and j_counter(hand)==0

print(isonepair("1234J"))

with open("seven.txt","r", encoding="utf-8") as file:
    bids=[]
    highhands=[]
    onepairs=[]
    twopairs=[]
    threeofakinds=[]
    fullhouses=[]
    fourofakinds=[]
    fiveofakinds=[]
    for id,line in enumerate(file):
        data=line.strip().split()
        hand=data[0]
        bid=data[1]
        bids.append(bid)
        if isfiveofakind(hand):
            c=0
            place=False
            if len(fiveofakinds)==0:
                fiveofakinds.append((hand,bids[id]))
                continue
            while c<len(fiveofakinds):
                for x in range(5):
                    if Dict[fiveofakinds[c][0][x]]==Dict[hand[x]]:
                        continue
                    elif Dict[fiveofakinds[c][0][x]]<Dict[hand[x]]:
                        break
                    elif Dict[fiveofakinds[c][0][x]]>Dict[hand[x]]:
                        place=True
                        break
                if place:
                    fiveofakinds.insert(c,(hand,bids[id]))
                    break
                if c==len(fiveofakinds)-1:
                    fiveofakinds.append((hand,bids[id]))
                    break
                c+=1

        elif isfourofakind(hand) or isfullhouse(hand):
            counter=0
            max=0
            while counter<len(hand):
                if max<hand.count(hand[counter]):
                    max=hand.count(hand[counter])
                counter+=1
            if isfourofakind(hand):
                c=0
                place=False
                if len(fourofakinds)==0:
                    fourofakinds.append((hand,bids[id]))
                    continue
                while c<len(fourofakinds):
                    for x in range(5):
                        if Dict[fourofakinds[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[fourofakinds[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[fourofakinds[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        fourofakinds.insert(c,(hand,bids[id]))
                        break
                    if c==len(fourofakinds)-1:
                        fourofakinds.append((hand,bids[id]))
                        break
                    c+=1
            elif isfullhouse(hand):
                c=0
                place=False
                if len(fullhouses)==0:
                    fullhouses.append((hand,bids[id]))
                    continue
                while c<len(fullhouses):
                    for x in range(5):
                        if Dict[fullhouses[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[fullhouses[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[fullhouses[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        fullhouses.insert(c,(hand,bids[id]))
                        break
                    if c==len(fullhouses)-1:
                        fullhouses.append((hand,bids[id]))
                        break
                    c+=1
        elif isthreeofakind(hand) or istwopair(hand):
            counter=0
            max=0
            while counter<len(hand):
                if max<hand.count(hand[counter]):
                    max=hand.count(hand[counter])
                counter+=1
            if isthreeofakind(hand):
                c=0
                place=False
                if len(threeofakinds)==0:
                    threeofakinds.append((hand,bids[id]))
                    continue
                while c<len(threeofakinds):
                    for x in range(5):
                        if Dict[threeofakinds[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[threeofakinds[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[threeofakinds[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        threeofakinds.insert(c,(hand,bids[id]))
                        break
                    if c==len(threeofakinds)-1:
                        threeofakinds.append((hand,bids[id]))
                        break
                    c+=1
            elif istwopair(hand):
                c=0
                place=False
                if len(twopairs)==0:
                    twopairs.append((hand,bids[id]))
                    continue
                while c<len(twopairs):
                    for x in range(5):
                        if Dict[twopairs[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[twopairs[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[twopairs[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        twopairs.insert(c,(hand,bids[id]))
                        break
                    if c==len(twopairs)-1:
                        twopairs.append((hand,bids[id]))
                        break
                    c+=1
        elif isonepair(hand):
            c=0
            place=False
            if len(onepairs)==0:
                onepairs.append((hand,bids[id]))
                continue
            while c<len(onepairs):
                for x in range(5):
                    if Dict[onepairs[c][0][x]]==Dict[hand[x]]:
                        continue
                    elif Dict[onepairs[c][0][x]]<Dict[hand[x]]:
                        break
                    elif Dict[onepairs[c][0][x]]>Dict[hand[x]]:
                        place=True
                        break
                if place:
                    onepairs.insert(c,(hand,bids[id]))
                    break
                if c==len(onepairs)-1:
                        onepairs.append((hand,bids[id]))
                        break
                c+=1
        elif ishighcard(hand):
            c=0
            place=False
            if len(highhands)==0:
                highhands.append((hand,bids[id]))
                continue
            while c<len(highhands):
                for x in range(5):
                    if Dict[highhands[c][0][x]]==Dict[hand[x]]:
                        continue
                    elif Dict[highhands[c][0][x]]<Dict[hand[x]]:
                        break
                    elif Dict[highhands[c][0][x]]>Dict[hand[x]]:
                        place=True
                        break
                if place:
                    highhands.insert(c,(hand,bids[id]))
                    break
                if c==len(highhands)-1:
                    highhands.append((hand,bids[id]))
                    break
                c+=1
    print("highhand",highhands)
    print("onepair",onepairs)
    print("twopair",twopairs)
    print("threeofkind",threeofakinds)
    print("fullhouses",fullhouses)
    print("fourofakind",fourofakinds)
    print("fiveofakind",fiveofakinds)
    place=1
    sum=0
    for hh in highhands:
        sum+=int(hh[1])*place
        place+=1
    for hh in onepairs:
        sum+=int(hh[1])*place
        place+=1
    for hh in twopairs:
        sum+=int(hh[1])*place
        place+=1
    for hh in threeofakinds:
        sum+=int(hh[1])*place
        place+=1
    for hh in fullhouses:
        sum+=int(hh[1])*place
        place+=1
    for hh in fourofakinds:
        sum+=int(hh[1])*place
        place+=1
    for hh in fiveofakinds:
        sum+=int(hh[1])*place
        place+=1
    print(sum)