# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())

a = [input() for x in range(n)]

result = defaultdict(list)

for x in range(m):
    word = input()
    for ind, element in enumerate(a):
        if word == element:
            result[word].append(ind+1)

for item in result.values():
    print(*item)



