class Stack:
    def __init__(self, arr):
        self.items = arr

    # items check the None:
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    # item append:
    def push(self,item):
        self.items.append(item)
    
    # top of stack:
    def top(self):
        return self.items[len(self.items)-1]

    # item delete or pop:
    def pop(self):
        return self.items.pop()

# no idea how to actually make this with just reading from text
s = [Stack(['T','V','J','W','N','R','M','S'][::-1]),
Stack((['V','C','P','Q','J','D','W','B'][::-1])),
Stack(['P','R','D','H','F','J','B'][::-1]),
Stack(['D','N','M','B','P','R','F'][::-1]),
Stack(['D','T','P','R','V','H'][::-1]),
Stack(['T','P','B','C'][::-1]),
Stack(['L','P','R','J','B'][::-1]),
Stack(['W','B','Z','T','L','S','C','N'][::-1]),
Stack(['G','S','L'][::-1])]

#  same as usual except im getting rid of the first 10 lines
with open("day5/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))
lines = lines[10:]

def cleanLine(line):
    line = line.replace("move "," ")
    line = line.replace(" from "," ")
    line = line.replace(" to "," ")
    return line

for line in lines:
    # get rid of text so its only nums tehn separate into variables
    line = cleanLine(line)
    m,f,t = tuple(int(x) for x in line.split())

    # for however many moves take the top of the from stack and add it to the to stack
    for i in range(m):
        temp = s[f-1].top()
        s[t-1].push(temp)
        s[f-1].pop()

# combine into string
a=""
for i in s:
    a+=i.top()
print(a)