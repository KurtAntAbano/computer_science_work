f = open("myfile.txt", "r")
c = f.read()
print(c)
f.close()

f = open("myfile.txt", "w")
f.write("THURSDAY")





# split()
# splits lines when having spaces
# split(",") splits everytime there is a ,
# default is splitting everytime there is a space