string = input()
string_list = string.split(' ')

while(True):
    try:
        del string_list[string_list.index('')]
    except ValueError:
        break

print(len(string_list))