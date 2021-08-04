import sys
N = int(input())
sum = 0

value = sys.stdin.readline().rstrip()
for i in range(0, N) :
    sum += int(value[i])

print(sum)


