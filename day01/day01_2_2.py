def whatareyou(stringecske):
    if "one" in stringecske:
        return 1
    elif "two" in stringecske:
        return 2
    elif "three" in stringecske:
        return 3
    elif "four" in stringecske:
        return 4
    elif "five" in stringecske:
        return 5
    elif "six" in stringecske:
        return 6
    elif "seven" in stringecske:
        return 7
    elif "eight" in stringecske:
        return 8
    elif "nine" in stringecske:
        return 9

one = open("one.txt", "r") 
text = one.read() 
sorok = text.split("\n") 
one.close()
listageci={"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
firstletters="otfsen"
first,k="",0
for i in sorok:
    for x in i:
        if x.isdigit:
            first=x
        if x in firstletters:
            first=whatareyou(i[x:(x+5)])
    k=+first
print(k)
