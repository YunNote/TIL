A = input().upper()
index = 0
list = {}
count = 0

for i in range(0, len(A)) :
    if A[i] in list.keys()  :
        list[A[i]] += 1
    else:
        list[A[i]] = 0

maxV = max(list.values())
for key in list.keys() :
    if list[key] == maxV :
        index = key
        count += 1

print( count > 1 and '?' or index)