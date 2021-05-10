"""
생성자는 수열 d(n)보다 항상 작은수이다.
따라서 1~10000까지 생성자의 List를 작성 후 1~10000까지의 수 중에 없는 수를 나열해 보면 될것이다.
"""

d_list=[]
for i in range(1,10000,1):
    val = i
    v_list =[]
    indices = 1
    while True:
        if len(str(val)) == 1:
            v_list.append(val*(10**(indices-1)+1))
            break
        a = divmod(val, 10)
        v_list.append(a[1]*(10**(indices-1)+1))
        val = a[0]
        indices += 1
    d_list.append(sum(v_list))

d_list = list(set(d_list))
t_list = list(set(range(1,10001)) - set(d_list))
t_list.sort()
print(*t_list, sep='\n')
