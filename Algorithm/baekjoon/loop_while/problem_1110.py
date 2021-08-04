import sys

N = sys.stdin.readline().rstrip()
V = len(N) > 1 and N or "0" + N
count = 1
while True:
    if int(N) == 0:
        break

    T = V[1] + str((int(V[0]) + int(V[1])) % 10)

    if int(N) == int(T):
        break
    V = T
    count += 1

print(count)
