with open("day2/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

vals = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

def isWinning(com, you):
    if com == "A" and you == "Y":
        return True
    elif com == "B" and you =="Z":
        return True
    elif com == "C" and you =="X":
        return True
    return False

def isDraw(com,you):
    return ord(com) == ord(you)-23

sum = 0
for i in lines:
    com, you = i.split(" ")
    if isWinning(com,you):
        sum += 6 + vals.get(you)
    elif isDraw(com,you):
        sum += 3 + vals.get(you)
    else:
        sum+=vals.get(you)

print(sum)