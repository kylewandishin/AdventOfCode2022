with open("day9/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))


class Knot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = []
        

    def move(self, dir):
        if dir == 'R':
            self.x += 1
        elif dir == 'L':
            self.x -= 1
        elif dir == 'U':
            self.y += 1
        elif dir == 'D':
            self.y -= 1

    def follow(self, head):
        dx = head.x - self.x
        dy = head.y - self.y

        # if its within 1 space in any direction then stay put
        if abs(dx) <= 1 and abs(dy) <= 1:
            return
        
        # if there is no distance horizontally add go up if the difference is exactly 2 otherwise go down
        elif dx == 0:
            self.y += 1 if dy == 2 else -1

        #same process inverse direction
        elif dy == 0:
            self.x += 1 if dx == 2 else -1
        
        # else more diagonally towards the head
        else:
            self.y += 1 if dy > 0 else -1
            self.x += 1 if dx > 0 else -1

    # check if we have already visited this point and if not add it to the list
    def checkVisited(self):
        if [self.x, self.y] not in self.visited:
            self.visited.append([self.x, self.y])


# make knots for the head and tail
head = Knot(0, 0) 
tail = Knot(0, 0)


for line in lines:
    #split each line into the direction and how many times you want to move that direction
    dir, times = line.split()

    # move and follow the pieces however many times specified above
    for _ in range(0, int(times)):
        head.move(dir)
        tail.follow(head)
        tail.checkVisited()

# print the lenght of the visited array which contains only unique points
print(len(tail.visited))
