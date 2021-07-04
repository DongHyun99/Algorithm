import sys

sys.setrecursionlimit(99999) # recursion error 방지

location = [] # 좌표, 처음에는 0으로 초기화 하고 배추의 위치는 1로 표시한다. 
M, N = 0,0 # M: 가로길이, N: 세로 길이
where = [] # 배추의 위치를 저장하는 2차원 배열

def discover(): # 최소 벌레 수를 출력하는 함수, where 값을 move에 전달하고 최소 벌레를 +1 한다.
    bug = 0
    while(len(where)!=0):
        move(where[0][0],where[0][1])
        bug += 1
    print(bug)                   

def move(i, j): # i,j 위치는 1이 확정이므로 0으로 고치고 where list에서 그 위치를 삭제한다. 그 후 오른쪽과 아래쪽에 대해서 recursion
    location[i][j] = 0
    where.remove([i,j])
    
    if j+1 < M and location[i][j+1] == 1:
        move(i,j+1)
    if j-1 >= 0 and location[i][j-1] == 1:
        move(i,j-1)
    if i+1 < N and location[i+1][j] == 1:
        move(i+1,j)
    if i-1 >= 0 and location[i-1][j] == 1:
        move(i-1,j)
    

T = int(input()) # 테스트 케이스 개수 T

for i in range(0,T,1):
    where=[] # where 초기화
    M, N, K = map(int,input().split(' ')) # 가로, 세로, 배추의 수를 받아온다.
    location = [[0 for p in range(M)] for o in range(N)] # 0으로 초기화된 배추 밭을 만든다.
    for i in range(0,K,1):
        X,Y = map(int,input().split(' ')) # 배추 위치를 받아온다.
        location[Y][X] = 1 # 배추위치 표시
        where.append([Y, X]) # 배추위치를 추가
    discover()
© 2021 GitHub, Inc.