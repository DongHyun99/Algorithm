from typing import Coroutine


N = int(input())
count = 99
# 1~99까지는 무조건 등차수열이므로 100이상인 N은 이부분을 빼고 계산한다.

if N < 100:
    print(N)

else:
    for i in range(100,N+1,1):
        t=str(i)
        term = int(t[2])-int(t[1])
        if (int(t[1])-int(t[0])) == term:
            count += 1
    print(count)