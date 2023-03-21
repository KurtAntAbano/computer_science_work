size = 11
hashTable = []

for i in range(0, size):
    hashTable.append(" ")


def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])  # ord converts string into ASCII

    return sum % tablesize


for n in range(4):
    s = input("enter a value ")
    slot = hash(s, size)
    hashTable[slot] = s

print(hashTable)

# search the item

f = input("where is my item? ... enter one item ")
index = hash(f, size)  # find the hash value

# printing the item

if hashTable[index] != " ":
    print("found at  ", index)
else:
    print(f, " not in your list")