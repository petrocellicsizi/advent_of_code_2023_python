def calc(x):
    to_str_converted = ""
    for digit in x:
        to_str_converted += digit
    num_colour=to_str_converted.split(" ")   
    if("red" == num_colour[2] and int(num_colour[1])>12):
        return False
    elif("blue" == num_colour[2] and int(num_colour[1])>14):
        return False
    elif("green" == num_colour[2] and int(num_colour[1])>13):
        return False
    
def whilecount(x):
    if(x>22):
        return 3
    elif(x>13):
        return 2
    elif(x>5):
        return 1

with open("two.txt", "r", encoding="utf-8") as file:
    szum,counter=0,0
    for gameid, line in enumerate(file, 1):
        good=True
        data=line.strip().split(":")
        pulls=data[1].split(";")
        for j in pulls:
                onehand=j.split(",")
                counter=whilecount(len(j))
                while counter>0:
                    if(calc(onehand[counter-1])==False):
                        good=False
                    counter=counter-1
        if good:
            szum=szum+gameid
print(szum)
                
        
