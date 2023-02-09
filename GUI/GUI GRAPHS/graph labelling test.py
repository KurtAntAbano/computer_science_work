import matplotlib.pyplot as plt# called 'plt' so that its easier to write

# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, color='green', label="test")
plt.plot(y, color='red', label="testred")



plt.title("Simple Plot")


# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
plt.legend()