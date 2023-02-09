import matplotlib.pyplot as plt# called 'plt' so that its easier to write

# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y, color='green')
# x and y can be from a passed parameter
# x and y can be a list instead of variables e.g plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# Adding the title
plt.title("Simple Plot")
# 'simple plot' can be take from input variables

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()



#
# # Python program to show pyplot module
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.axis([0, 6, 0, 20])
##plot.axis([xmin, xmax, ymin, ymax])
# plt.show()