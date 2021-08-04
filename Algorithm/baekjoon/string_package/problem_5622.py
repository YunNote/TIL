DIAL = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

P = input()
sum = 0
for i in range(len(P)) :

    for j in range(len(DIAL)) :
        if P[i] in DIAL[j] :
            sum += j +3
print(sum)
