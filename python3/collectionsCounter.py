# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoes = int(input())
sizes = Counter(map(int, input().split()))

sum_ = 0

for x in range(int(input())):
    size, cost = map(int, input().split())
    if sizes[size]:
        sum_ += cost
        sizes[size] -= 1
print(sum_)

