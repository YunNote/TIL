import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(0, N):
    if A[i] < X:
        print(A[i] , end=" ")
