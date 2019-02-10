# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = raw_input().split()
poly = raw_input().replace('x', nums[0])

if eval(poly) == int(nums[1]):
    print True
