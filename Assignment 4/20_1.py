x = input("Enter a sentence").lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

count = {}

for i in x:
    if i in alphabet:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1

keys = count.keys()

for i in sorted(keys):
    print(i, count[i])
    sorted(i)

