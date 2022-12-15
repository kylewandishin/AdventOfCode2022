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

    #  if e1 is in e2 add to the count
    if e1L>=e2L and e1H<=e2H:
        count+=1
    
    #if e2 is in e1 add to the count
    elif e2L>=e1L and e2H<=e1H:
        count+=1
print(count)


