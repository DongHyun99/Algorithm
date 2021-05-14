s=input()
val = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabet:
    try:
        val.append(s.index(i))
    except ValueError:
        val.append(-1)

print(*val)