input()
array = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for x in array:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print(happiness)


