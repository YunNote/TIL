import sys
S = sys.stdin.readline().rstrip()

list = [-1 for _ in range(26)]

for i in range(len(S)) :

    index = ord(S[i]) - 97

    if int(list[index]) == -1 :
        list[index] = i

for i in range(len(list)) :
    print(list[i] , end=' ')


