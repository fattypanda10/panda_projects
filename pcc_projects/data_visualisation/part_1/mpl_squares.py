import matplotlib.pyplot as plt


def set_props():
    plt.style.use("seaborn")
    ax.set_xlabel("x_vals", fontsize=15)
    ax.set_ylabel("y_vals", fontsize=15)
    ax.set_title("PLOT")
    ax.tick_params(axis="both", which="major", labelsize=15)


x_vals = range(1, 5000)
y_vals = [i**3 for i in x_vals]

fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, s=20)
set_props()
# ax.axis([0, 1000, 0, 1000000])
plt.show()
# plt.savefig("squares.png", bbox_inches='tight')
