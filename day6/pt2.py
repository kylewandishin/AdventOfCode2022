#############################################################
#        same code as pt 1 but different length var         #
#############################################################

with open("day6/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))
line = lines[0]

str=""
searchLength = 14
for i in range(len(line)):
    temp = line[i:i+searchLength]
    if all([temp[i] not in temp[:i] + temp[i+1:] for i in range(len(temp))]):
        print(i+searchLength)
        break