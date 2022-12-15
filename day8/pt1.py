import numpy as np
with open("day8/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

trees = []
for line in lines:
    trees.append(list(map(int, line))) # convert to matrix by turning each line into array of chars
treesT = np.array(trees).T # create a transposed version of matrix to easily iterate

"""
TESTING

(tested with test.txt)
r ,c= 2,3
# left
print([h >= trees[r][c]  for h in trees[r][:c]])
# right
print([h >= trees[r][c]  for h in trees[r][c+1:]])
# up
print([h >= trees[r][c]  for h in treesT[c][:r]])
# down
print([h >= trees[r][c]  for h in treesT[c][r+1:]])

"""

sum = 0
for r in range(len(trees)):
    for c in range(len(trees[0])):
        curTree=trees[r][c]

        # automatically add to sum if it is on the edge
        if r == 0 or c == 0 or r == len(trees)-1 or c == len(trees[0])-1:
            sum+=1

        #separated for readability however could use one giant if statment with or's to condence code
        elif not any(num >= curTree for num in trees[r][:c]):
            sum+=1
        elif not any(num >= curTree for num in trees[r][c + 1:]):
            sum+=1
        elif not any(num >= curTree for num in treesT[c][:r]):
            sum+=1
        elif not any(num >= curTree for num in treesT[c][r+1:]):
            sum+=1

print(sum)
