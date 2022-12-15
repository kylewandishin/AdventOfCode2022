with open("day2/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

vals = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
    "A" : 1,
    "B" : 2,
    "C" : 3
}

lose = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}

win = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}

sum = 0
for i in lines:
    com, out = i.split(" ")
    if out == "Y":
        sum+= 3 + vals.get(com)
    if out == "X":        
        sum+= vals.get(lose.get(com))
    if out == "Z":
        sum+= 6 + vals.get(win.get(com))
    
print(sum)
