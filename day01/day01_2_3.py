def parse(num):
    if num == "one" or num=="eno":
        return "1"
    elif num == "two" or num=="owt":
        return "2"
    elif num == "three" or num=="eerht":
        return "3"
    elif num == "four" or num=="ruof":
        return "4"
    elif num == "five" or num=="evif":
        return "5"
    elif num == "six" or num=="xis":
        return "6"
    elif num == "seven" or num=="neves":
        return "7"
    elif num == "eight" or num=="thgie":
        return "8"
    elif num == "nine" or num=="enin":
        return "9"

listageci={"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
listageci2={"eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"}
min,irtszamunk,indexirtszam=1000,None,None
digitszamunk,indexdigitszam=None,None
first,last=None,None
line2=None
sum=0
with open("one.txt", "r", encoding="utf-8") as file:
    for line in file:
        min=1000
        indexirtszam,indexdigitszam=100,100
        for irtszam in listageci:
            if irtszam in line:
                indexirtszam=line.find(irtszam)
                if indexirtszam<min:
                    min=indexirtszam
                    irtszamunk=irtszam
        for digitid,digit in enumerate(line):
            if digit.isdigit():
                digitszamunk=digit
                indexdigitszam=digitid
                break
        if(indexdigitszam<min):
            first=digitszamunk
        else:
            first=parse(irtszamunk)
        line2 = line[::-1]
        min=1000
        indexirtszam,indexdigitszam=100,100
        for irtszam in listageci2:
            if irtszam in line2:
                indexirtszam=line2.find(irtszam)
                if indexirtszam<min:
                    min=indexirtszam
                    irtszamunk=irtszam
        for digitid,digit in enumerate(line2):
            if digit.isdigit():
                digitszamunk=digit
                indexdigitszam=digitid
                break
        if(indexdigitszam<min):
            last=digitszamunk
        else:
            last=parse(irtszamunk)
        sum=sum+10*int(first)+int(last)
    print(sum)