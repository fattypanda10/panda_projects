from random import choice

import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # starting point is origin
        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        while len(self.x_vals) < self.num_points:
            # x coordinates
            x_step = RandomWalk.get_step()
            # y coordinates
            y_step = RandomWalk.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # new coordinates
            x = self.x_vals[-1] + x_step
            y = self.y_vals[-1] + y_step

            self.x_vals.append(x)
            self.y_vals.append(y)

    @staticmethod
    def get_step():
        direction = choice([1, -1])
        distance = choice(range(5))
        return direction * distance


rw = RandomWalk(10_000)
rw.fill_walk()
plt.style.use("classic")
point_numbers = range(rw.num_points)
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.scatter(rw.x_vals[0], rw.y_vals[0], c="red", s=100, edgecolors="none")
ax.scatter(rw.x_vals[-1], rw.y_vals[-1], c="green", s=100, edgecolors="none")

# plot
# ax.plot(rw.x_vals, rw.y_vals, c='red')

# scatter plot
ax.scatter(
    rw.x_vals, rw.y_vals, c=point_numbers, cmap=plt.cm.Blues, s=1, edgecolor="none"
)
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
plt.show()
