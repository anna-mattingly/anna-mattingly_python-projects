import matplotlib.pyplot as plt
x = [3, 5, 7, 8, 4]
y = [5, 3, 7, 8, 2]
labels = ["Jan", "Feb", "Mar", "April", "May"]
plt.scatter(x, y)
for i, j in enumerate(labels):
    plt.annotate(j, (x[i]+0.10, y[i]), fontsize=10)
plt.show()