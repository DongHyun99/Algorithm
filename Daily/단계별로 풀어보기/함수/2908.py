num1, num2 = input().split(' ')

num3=0
num4=0
k1=1
k2=1

for i in num1:
    num3 += k1*int(i)
    k1 *= 10

for  i in num2:
    num4 += k2*int(i)
    k2 *= 10

print(max(num3,num4))