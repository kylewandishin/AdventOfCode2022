from heapq import heappop, heappush
with open("day12/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

"""
ok so,
ord(a) = 97, and therefore if we use the system of ord(_)-96 we get the cypher where a=1,b=2... z=26
therefore we can use these new vals to check valid neighbours in a easy to visualise way. however the -96
is now redundant but we will keep if in there.
"""
map =[[ord(i)-96 for i in line] for line in lines]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == -13:
            map[i][j] = 1
            start = i,j
        elif map[i][j] == -27:
            map[i][j] = 26
            end = i,j

def checkNeighbours(i,j):
    # check +1,0  -1,0  0,1  0,-1 by adding those values to i,j and then checking the values at those new coordinates
    for x,y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:     
        ci = i + x
        cj = j + y

        # remove consideration of edge cases
        if not (0 <= ci < len(map) and 0 <= cj < len(map[0])):
            continue   
        # if height is ok then its acceptable
        if map[ci][cj] <= map[i][j] + 1:
            # allows for 2 returns 
            yield ci, cj

# create grid of 'False'
visited = [[False] * len(map[_]) for _ in range(len(map))]
# how many steps, starting row, starting col
heap = [(0, start[0], start[1])]


while True:
    # pop from heap and split to steps, i, j
    steps, i, j = heappop(heap)

    # if alread visited pass
    if visited[i][j]:
        continue
    # set space visited
    visited[i][j] = True

    # check if reached the end
    if (i, j) == end:
        # print how many steps till we get here 
        print(steps)
        # break our loop 
        break

    # for each valid neighbour push steps+1, with coords of valid neighbour 
    for ii, jj in checkNeighbours(i, j):
        heappush(heap, (steps + 1, ii, jj))