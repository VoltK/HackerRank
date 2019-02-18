# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

word, k = input().split()



print(*["".join(comb) for comb in permutations(sorted(word), int(k))], sep="\n")
