# Enter your code here. Read input from STDIN. Print output to STDOUT

k,arr = int(input()),list(map(int, input().split()))
rooms = {}
for x in arr:
    if str(x) not in rooms:
        rooms[str(x)] = 1
    else:
        rooms[str(x)] += 1
for key, value in rooms.items():
    if value == 1:
        print(key)

