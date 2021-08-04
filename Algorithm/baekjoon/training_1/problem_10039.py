import sys

sum = 0
SIZE = 5

for i in range(0, SIZE) :
    score = int(sys.stdin.readline().rstrip())
    if score < 40 :
        sum += 40
    else:
        sum += score

print(int(sum / SIZE))