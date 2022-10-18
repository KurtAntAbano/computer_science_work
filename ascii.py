ciphername = ""
name = input("input your name")
length =len(name)
for n in range(0,length):
    asciivalue = ord(name[n])
    ciphername += str(asciivalue)

print(name, "in Ascii is", ciphername)