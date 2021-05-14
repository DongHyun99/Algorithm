com_num = int(input()) # 컴퓨터 수
count = int(input()) # 관계의 수
birus_com = []
computer_tree = []

def search(locate):
    if not locate in birus_com:
        birus_com.append(locate)
        for i in computer_tree[locate-1]:
            search(i)

for i in range(0,com_num,1):
    computer_tree.append([])

for i in range(0,count,1):
    com1, com2 = input().split()
    computer_tree[int(com1)-1].append(int(com2))
    computer_tree[int(com2)-1].append(int(com1))

search(1)

print(len(birus_com)-1)
