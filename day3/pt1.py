# print(27-ord("A")) = -38
# print(1-ord("a")) = -96

with open("day3/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

sum=0
def val(i):
    if i.isupper():
        return ord(i)-38
    return ord(i)-96

for line in lines:
    pack1, pack2 = line[:int(len(line)/2)], line[int(len(line)/2):]
    for i in pack1:
        if pack2.find(i) != -1:
            sum+=val(i)
            break
print(sum)