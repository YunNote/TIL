import sys

try:
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a + b)
except:
    exit()
