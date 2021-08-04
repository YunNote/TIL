import sys

C=int(sys.stdin.readline().rstrip())

for _ in range(C) :
    list = sys.stdin.readline().rstrip().split();
    N = int(list[0])
    score = [int(i) for i in list[1:]]
    avg = sum(score) / N
    count = 0
    for i in range(N) :
        if score[i] > avg :
            count += 1
    print("{:.3f}%".format(count / N * 100))

