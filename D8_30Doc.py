import sys
n = int(input())
phonebook = {}
for i in range(0, n):
    entry = str(input()).split(' ')
    name = entry[0]
    phone_number = int(entry[1])
    phonebook[name] = phone_number

lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phonebook:
        print(name + '=' + str( phonebook[name] ))
    else:
        print('Not found')