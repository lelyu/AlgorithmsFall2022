import random


def hash(x, m):
    return x % m

def hashtable(n, m):
    # generating n random intergers from 0 to 99999999 and put them in a list
    ls = []
    for i in range(n):
        ls.append(random.randint(0, 99999999))
    table = {}
    # populate the table with empty list
    for i in range(m):
        table[i] = []
    for i in ls:
        # compute the hash code (index inside the dictionary)
        index = hash(i, m)
        table[index].append(i)

    # i is the index
    maxLength = 0
    maxIndex = 0
    for i in table:
        if len(table[i]) > maxLength:
            maxLength = len(table[i])
            maxIndex = i
    return len(table[maxIndex])
    

print("i: ")
longest = 0
for i in range(10):
   length =  hashtable(60, 30)
   if length > longest:
    longest = length

print(longest)

print("ii: ")
longest = 0
for i in range(10):
   length =  hashtable(60, 1000)
   if length > longest:
    longest = length

print(longest)

print("iii: ")
longest = 0
for i in range(10):
   length =  hashtable(60, 4)
   if length > longest:
    longest = length

print(longest)