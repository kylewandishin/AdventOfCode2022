# no idea how to actually make this with just reading from text
s = [['T','V','J','W','N','R','M','S'],
['V','C','P','Q','J','D','W','B'],
['P','R','D','H','F','J','B'],
['D','N','M','B','P','R','F'],
['B','T','P','R','V','H'],
['T','P','B','C'],
['L','P','R','J','B'],
['W','B','Z','T','L','S','C','N'],
['G','S','L']
]

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

    temp = s[f-1][:m]
    s[f-1] = s[f-1][m:] 
    s[t-1]=temp+s[t-1]

# combine into string
a=""
for i in s:
    a += i[0] if i != [] else ""
print(a)