BandA = 0
BandB = 0
BandC = 0
BandD = 0

for i in range(365):
    temp = int(input("input todays temperature"))
    if temp <= 10:
        BandA += 1
    elif temp <= 20:
        BandB += 1
    elif temp <= 30:
        BandC += 1
    elif temp > 31:
        BandD += 1
print("Band A:", BandA)
print("Band B:", BandB)
print("Band C:", BandC)
print("Band D:", BandD)
