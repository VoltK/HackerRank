input()
set_a = set(map(int, input().split())) 
input()
set_b = set(map(int, input().split()))

symmetric_differance = list(set_a.difference(set_b)) + list(set_b.difference(set_a))
symmetric_differance.sort()
for x in symmetric_differance:
    print(x)
