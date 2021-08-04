N=int(input())
score = list(map(int, input().split()))
maxScore = max(score)
sum = 0

for i in range(len(score)) :
    sum += score[i] / maxScore * 100

print(sum / len(score))

