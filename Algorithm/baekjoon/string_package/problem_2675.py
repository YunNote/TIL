T = int(input())

for _ in range(T):
    R, S = input().split()

    for i in range(0, len(S)) :
        print(S[i] * int(R), end='')
    print()