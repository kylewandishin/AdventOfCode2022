import os

with open("day7/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

dict = {} 
holder = {} 

for line in lines:
    if line[0] == '$':
        ignore, doThis, *ddir = line.split()
        if doThis == 'cd':
            path = ddir[0]
            if path == '/': 
                curdir = path 
            else:
                curdir = os.path.normpath(os.path.join(curdir, path))
            if curdir not in dict: 
                dict[curdir] = []
                holder[curdir] = 0

    else: 
        fsize, fname = line.split()
        if fsize != 'dir': 
            holder[curdir] += int(fsize)
        else: 
            dict[curdir].append(os.path.normpath(os.path.join(curdir, fname)))

def calculateDirsize(name):
    size = holder[name] 
    for i in dict[name]: 
        if i in dict:
            size += calculateDirsize(i)
    return size

sum = 0
for i in dict:
    temp = calculateDirsize(i)
    if temp < 100000:
        sum += temp

print(sum)