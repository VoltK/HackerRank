import numpy

lst = []

for x in range([int(x) for x in input().split()][0]):
    lst.append(input().split())

arr = numpy.array(lst, int)

print(numpy.transpose(arr), arr.flatten(), sep='\n' )


