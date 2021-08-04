import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
print(a[1])
