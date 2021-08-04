import sys
loop = list(range(1,int(sys.stdin.readline().rstrip()) +1))
for (i,v) in enumerate(loop):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(i+1 , a + b))