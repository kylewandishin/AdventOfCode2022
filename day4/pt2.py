with open("day4/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

count=0
for i in lines:
    # split everything down into each elves upper and lower bounds as ints
    e1,e2 = i.split(",")
    e1L,e1H = tuple(int(x) for x in e1.split("-"))
    e2L,e2H = tuple(int(x) for x in e2.split("-"))

    #if e2(H/L) is in the range of e1 add 1
    if e2L in range(e1L,e1H+1) or e2H in range(e1L,e1H+1):
        count+=1
    
    #if e1(H/L) is in the range of e2 add 1
    elif e1L in range(e2L,e2H+1) or e1H in range(e2L,e2H+1):
        count+=1
print(count)


