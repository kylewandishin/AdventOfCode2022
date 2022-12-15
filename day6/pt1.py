with open("day6/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))
#input is only 1 line
line = lines[0]

#look for 4 in a row that are different characters
searchLength = 4
for i in range(len(line)):
    temp = line[i:i+searchLength]
    if all([temp[i] not in temp[:i] + temp[i+1:] for i in range(len(temp))]):
        print(i+searchLength)
        break