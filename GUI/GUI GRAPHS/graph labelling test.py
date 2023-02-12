import matplotlib.pyplot as plt# called 'plt' so that its easier to write

# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y, color='green', label = "green")
plt.plot(x, y, color='red', label = "red")



plt.title("Simple Plot")


# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.legend()
#.legend shows the key top left
plt.show()