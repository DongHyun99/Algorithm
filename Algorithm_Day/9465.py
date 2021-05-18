test_case = int(input())

for i in range(0,test_case,1):
    length = int(input())
    index1 = input().split(' ')
    index2 = input().split(' ')
    index = [index1, index2]
    index_sec = index1+index2

def max_sticker(index:list, index_sex:list, length:int):
    index_sort = sorted(index_sec).reverse()
    while(True):
        location = index_sec.index(max(index_sort)) # 나중에 index_sort와 index_sec의 값을 초기화 해줘야 함
        if location//length == 1: # 2행일 때 위치를 맞춰준다.
            location = location % length
        if location == 0: # 가장 왼쪽인 경우 왼쪽은 고려하지 않아도 됨
            val1=index[0][0]-index[0][1]-index[1][0]
            val2=index[1][0]-index[1][1]-index[0][0]
            if val1 
