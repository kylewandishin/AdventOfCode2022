with open("day11/input.txt") as file_in:
    monkeyParts = file_in.read().strip().split("\n\n")

class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.counter = 0

monkeys = []
for i, part in enumerate(monkeyParts):
    """
    make data look like this
    Monkey 1:
        Starting items: 93, 71, 79, 83, 69, 70, 94, 98
        Operation: new = old + 8
        Test: divisible by 11
            If true: throw to monkey 5
            If false: throw to monkey 6
    """
    #convert to array 
    lines = part.split("\n")

    # use map to convert all levels to ints
    items = list(map(int, lines[1][2:].split(" ", 2)[2].split(", ")))

    #convert entire line into array then look at the part thats just new = old (operation) val tehn split that into array 
    operation = lines[2][2:].split(" ", 3)[3].split(" ")

    # look at the line then split it into an array and look at only the last index
    mod = int(lines[3][2:].split(" ")[-1])
    # same idea but to get the number of monkey we are giving the iteme to 
    ifT = int(lines[4][4:].split(" ")[-1])
    ifF = int(lines[5][4:].split(" ")[-1])

    # create monkey object and add to monkeys array
    monkeys.append(Monkey(items,operation,[mod, ifT, ifF]))

mainMod = 1
for i in monkeys:
    mainMod*=i.test[0]

def calcNew(operation, val):
    left, op, right = operation
    assert left == "old"
    match op:
        # operator can only be + and * so no need to factor in subtraction and division
        case "+":
            eval = val+int(right)
        case '*':
            # if its say new = old * old square it otherwise just return val*old
            if right == "old":
                eval = val**2
            else:
                eval = val * int(right)
    return eval%mainMod

# Do the rounds
for round in range(10000):
    for i in range(len(monkeys)):
        curMonkey = monkeys[i]
        for item in curMonkey.items:
            item = calcNew(curMonkey.operation, item)
            # split test array into vals to use
            mod, ifT, ifF = curMonkey.test
            # give new level to whatever monkey the test specifies
            if item % mod == 0:
                monkeys[ifT].items.append(item)
            else:
                monkeys[ifF].items.append(item)

            curMonkey.counter += 1

        # Empty the list of items
        curMonkey.items = []


# make the vals and sort them then multiply the last 2
amounts = sorted([m.counter for m in monkeys])
print(amounts[-1]*amounts[-2])