# Python Program to illustrate Linear Plotting

import matplotlib.pyplot as plt

# year contains the x-axis values
# and e-india & e-bangladesh
# are the y-axis values for plotting

memory = [1, 2, 3, 4, 5, 6]
iterative_memory = [0, 0.084, 0.084, 0.108, 0.132, 0.208, 0.292, 0.472, 0.832, 1.54, 2.956, 5.8]

# plotting of x-axis(year) and
# y-axis(power consumption)
#with different colored labels of two countries

plt.plot(memory, iterative_memory, color='orange',
         label='iterative memory usage')


# naming of x-axis and y-axis
plt.xlabel('Numbers')
plt.ylabel('memory allocation')

# naming the title of the plot
plt.title('Electricity consumption per capita\
 of India and Bangladesh')

plt.legend()
plt.show()