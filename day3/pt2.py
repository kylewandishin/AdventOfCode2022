with open("day3/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace("\n", ""))

sum=0
def val(i):
    if i.isupper():
        return ord(i)-38
    return ord(i)-96

# for groups of 3 in all the packs
for i in range(0, int(len(lines)), 3):
    # separate into groups and sort from shortest to longest
    group = lines[i : i+3]
    group.sort(key=len)
    # divide into indivisual strings
    p1,p2,p3 = group[0],group[1],group[2]

    # for every value in the longest string 
    for j in range(len(p3)):
        # see if it is in both of the others
        if p2.find(p3[j]) != -1 and p1.find(p3[j]) != -1:
                # add val of badge to sum
                sum+=val(p3[j])
                break

print(sum)