import sys
a = int(sys.stdin.readline().rstrip())
for i in range(0, a) :
    print(sum(map(int, sys.stdin.readline().rstrip().split())))