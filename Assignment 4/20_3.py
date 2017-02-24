alice = open('alice.txt', 'r')

count = {}

for line in alice:
    for word in line.split():
        word = word.lower()  
        if word.isalpha():     # ignore numbers
            if word in count: 
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = count.keys()

def count_all():
    for word in sorted(keys):
        print("{0:18}{1}".format(word,count[word]))

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")        
print("Word\t\t  Count")
print("=======================")
count_all()


