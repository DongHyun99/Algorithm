a=int(input())
b=[x for x in input().strip().split()]
b = list(map(int, b))
b.sort()
max = 0
if a%2 == 1: # 홀수
    max = b[-1]
    del b[-1]
    a -= 1
    
for i in range(a//2):
    if max < b[i]+b[-(i+1)]:
        max = b[i] + b[-(i+1)]
print(max)