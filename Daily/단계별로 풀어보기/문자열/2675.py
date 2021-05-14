num = int(input())

for i in range(0,num,1):
    re, string = input().split()
    for i in string:
        for j in range(0,int(re),1):
            print(i, end='')
    print()