with open("day10/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", "").split(" "))
xVal = 1
iterNum = 1
dict = {iterNum: xVal}
for line in lines:
    if line == ["noop"]:
        iterNum += 1
    elif line[0] == "addx":
            iterNum += 2
            xVal += int(line[1])
    dict[iterNum] = xVal

points = []

for position in range(240):
    cycle = position + 1
    curVal = dict[cycle] if cycle in dict else dict[cycle-1] if cycle-1 in dict else dict[cycle-2] if cycle-2 in dict else 0
    if -1 <= position % 40 - curVal <= 1:
        points.append(position)

# draw board
for y in range(6):
    for x in range(40):

        # check by row, y*40 gets row becasue each row is 40 long and therefore we can reduce to the x variable
        if x + y * 40 in points: 
            # if the value is in drawn then print a ■ otherwise print a space 
            print("█", end="")
        else:
            print(" ", end="")
    print()