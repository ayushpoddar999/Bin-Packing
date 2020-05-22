import matplotlib.pyplot as plt

y = [0.8821, 0.8853, 0.8847, 0.8842, 0.8905, 0.8920, 0.8897, 0.8889, 0.8854, 0.8834, 0.8928, 0.8872, 0.8904, 0.8865, 0.8958]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
plt.ylim(0,1)
plt.xlim(1,15)
plt.plot(x, y)


plt.xlabel('N Iterations/Generations')
plt.ylabel('Fitness')

plt.title('Performance of GA')

plt.show()
