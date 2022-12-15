
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

sum = 0
for i in range(20,260,40):
    #  essentially a condensed if else series saying that if this value isnt directly in there is the one bellow it in there 
    #  for example in the test.txt there is no dict[220] but dict[219] is so we should just use that 
    sum += i*dict[i] if i in dict else i*dict[i-1] if i-1 in dict else i*dict[i-2] if i-2 in dict else 0

print(sum)