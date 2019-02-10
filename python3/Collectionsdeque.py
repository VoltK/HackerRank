# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for x in range(int(input())):
    op, _, num = input().partition(" ")
    eval(f'd.{op}({num})')

print(*d)