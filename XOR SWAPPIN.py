x = 10
y = 11

x = x ^ y
y = x ^ y
x = x ^ y


print (x,y)

# Here we dont need to use another variable
# x XOR x will always equel 0
# for example if x == y, the program will XOR x and y and see wether it equels 0
# use XOR to find the difference