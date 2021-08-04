

N=int(input())
count = 0
for _ in range(N) :
    V = input()
    list = [V[0]]
    check = []
    before = V[0]

    for i in range(1, len(V)) :
        if V[i] in list :
            if before != V[i] :
                check.append(1)
        list.append(V[i])
        before = V[i]

    if sum(check) == 0 :
        count += 1
print(count)
