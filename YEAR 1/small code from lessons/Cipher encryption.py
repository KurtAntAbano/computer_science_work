ciphername = "ζ = ʃ Θ d σ ÷ ʃ β d σ  "
length =len(ciphername)
for n in range(0,length):
    asciivalue = ord(ciphername[n])
    ciphername += str(asciivalue)
    print(ciphername)