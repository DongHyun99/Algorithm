'''
oxo oxx xxo xox
xox xxo oxx oxo
'''
test_case = int(input())

def case_0 (location:int, index1:list, index2:list):
    return index2[location+1]+index1[location+2]

def case_1 (location:int, index1:list, index2:list):
    return index2[location+2]

def case_2 (location:int, index1:list, index2:list):
    return index1[location+2]

def case_3 (location:int, index1:list, index2:list):
    return index1[location+1]+index2[location+2]

for i in range(0,test_case,1):
    length = int(input())
    index1 = input().split(' ')
    index2 = input().split(' ')
    index1 = map(index2,int)
    index2 = map(index2,int)
    val=[index1[0],index2[0]]
    for j in range(0,(length-1)//2,2):
        zero = val[0]+case_0(j, index1, index2)
        one = val[0]+case_1(j, index1, index2)
        two = val[1]+case_2(j, index1, index2)
        three = val[1]+case_3(j, index1, index2)
        if zero>two:
            val[0] = zero
        else: val[0] = two
        if one>three:
            val[1] = one
        else: val[1] = three
        print(val)
    if(length-1)%2 == 1:
        val[0] += index2[length-1]
        val[1] += index1[length-1]
    print(max(val))