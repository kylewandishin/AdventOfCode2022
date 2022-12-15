with open("day1/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

elves = []
sum = 0

#  make an array of the sums of each elf
for i in lines:
    if i == "":
        elves.append(sum)
        sum = 0
    else:
        sum+=int(i)
elves.append(sum)

# sort elves in reverse so we can add the first 3 indecies
elves = sorted(elves, reverse=True)

print(f"{elves[0]+elves[1]+elves[2]}")