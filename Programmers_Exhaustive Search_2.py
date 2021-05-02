def find(num_list, a, num):
    if len(num_list) != 0:
        for i in num_list:
            numb = str(num)+str(i)
            a.append(numb)
            b = num_list[:]
            del b[b.index(i)]
            find(b,a,numb)

def solution(numbers):
    count=0
    numbers=list(numbers)
    a=[]
    find(numbers,a,'')
    a = list(set(list(map(int, a))))
    for i in a:
        arg = True
        if i <= 1:
            continue
        for k in range(2,i,1):
            if i % k ==0:
                arg = False
                break
        if arg == True:
            count +=1
    return count

print(solution('011'))