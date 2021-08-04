list = [int(input()) for _ in range(3)]
result = [0 for _ in range(10)]
v=1
for i in range(3) :
    v *= list[i];

v = str(v)
for i in range(0 , len(v)) :
    result[int(v[i])] += 1

for i in range(len(result)) :
    print(result[i])