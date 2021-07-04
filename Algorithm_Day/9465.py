'''
oxo oxx xxo xox
xox xxo oxx oxo
'''
test_case = int(input())

for i in range(test_case):
    length = int(input())
    index1 = list(map(int, input().split(' ')))
    index2 = list(map(int, input().split(' ')))
    val=[index1[0],index2[0]]
    if length==2:
        val[0] += index2[length-1]
        val[1] += index1[length-1]
    elif length !=1:
        for j in range(0,(length-2),2):
            zero = val[0]+index2[j+1]+index1[j+2]
            one = val[0]+index2[j+2]
            two = val[1]+index1[j+2]
            three = val[1]+index1[j+1]+index2[j+2]
            val[0] = max(zero, two)
            val[1] = max(one, three)
        if(length-1)%2 == 1:
            val[0] += index2[length-1]
            val[1] += index1[length-1]
    print(max(val))