# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

words = OrderedDict()

for x in range(int(input())):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values(), sep=" ")