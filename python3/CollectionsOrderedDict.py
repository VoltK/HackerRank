# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()
for x in range(int(input())):
    inputs = input().split()
    if len(inputs) > 2:
        key = inputs[0]+" "+inputs[1]
        if key in items:
            items[key] += int(inputs[2])
        else:
            items[key] = int(inputs[2])
    else:
        #items[inputs[0]] = inputs[1]
        if inputs[0] in items:
            items[inputs[0]] += int(inputs[1])
        else:
            items[inputs[0]] = int(inputs[1])

for key, val in items.items():
    print(key, val)

