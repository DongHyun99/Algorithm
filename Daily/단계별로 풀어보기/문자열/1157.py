Alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j',
'K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u',
'V','v','W','w','X','x','Y','y','Z','z']
Count_al=[]
count=[]

word = input()

for i in Alphabet:
    Count_al.append(word.count(i))

for i in range(0,52,2):
    count.append(Count_al[i]+Count_al[i+1])

max_val = max(count)
val = None

for i in count:
    if max_val == i:
        if not val == None:
            val = None
            break
        val = count.index(i)

if not val == None:
    print(Alphabet[val*2])
else: print('?')