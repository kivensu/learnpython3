import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5, 6]
#y_values = [1, 4, 9, 16, 25, 36]

x_values = list(range(1, 101))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s=40, c=y_values,
            cmap=plt.cm.Reds, edgecolor='None')
#title, x, y
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 100, 0, 1100000])
plt.show()
