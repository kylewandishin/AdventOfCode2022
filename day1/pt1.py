with open("day1/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

highest = 0
sum = 0

for i in lines:
    if sum>highest:
        highest = sum
    if i == "":
        sum = 0
    else:
        sum+=int(i)

# 72478
print(highest)