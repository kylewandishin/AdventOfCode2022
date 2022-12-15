import numpy as np
with open("day8/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

trees = []
for line in lines:
    # convert to matrix by turning each line into array of chars
    trees.append(list(map(int, line)))

max = 0


for r in range(len(trees)):
    for c in range(len(trees[r])):
        #set the bounds to the edges to start
        upHBound,upVBound = len(trees[r])-1,len(trees[c])-1
        lowHBound,lowVBound = 0,0
        curTree = trees[r][c]

        #sum = 1 because *= will always equal 0 if it starts as 0
        sum = 1

        # iterate through all numbers to the left backwards to find the closest value
        for i in reversed(range(0, c)):
            if trees[r][i] >= curTree:
                lowHBound = i
                break
        
        # iterate through all to the right
        for i in range(c+1, len(trees[r])):
            if trees[r][i] >= curTree:
                upHBound = i
                break
        
        # iterate through all above numbers in reverse to find closest val
        for i in reversed(range(0, r)):
            if trees[i][c] >= curTree:
                lowVBound = i
                break

        # iterate trhough all numbers under
        for i in range(r+1, len(trees[c])):
            if trees[i][c] >= curTree:
                upVBound = i
                break
        
        # multiply together all the distances
        for i in [r-lowVBound, upVBound-r,c-lowHBound, upHBound-c]:
            sum*=i if i >0 else 1
        if sum>max:
            max = sum

print(max)
