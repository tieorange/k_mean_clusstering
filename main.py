import random

import matplotlib.pyplot as plt
from matplotlib import style
import numpy

style.use("ggplot")

# === CONSTANTS
rand_from = 0
rand_to = 20
amount_points = 150
amount_groups = 3

# generate 3 sets of normally distributed points around
# different means with different variances
# ===== PUNKT #1 random points
group1 = numpy.random.normal(1, 0.2, (100, 2))
group2 = numpy.random.normal(2, 0.5, (300, 2))
group3 = numpy.random.normal(3, 0.3, (100, 2))

# slightly move sets 2 and 3 (for a prettier output)
group2[:, 0] += 2
group3[:, 0] -= 1.5

xy = numpy.concatenate((group1, group2, group3))

# plot colored points

# print(xy)
x = xy[:, 0]
y = xy[:, 1]


# ====== PUNKT 2 find centroids

# get 3 randoms

hl, = plt.plot([], [])


def onclick(event):
    centroids = []
    for r in range(3):
        random_index = random.uniform(0, len(xy))
        centroids.append(xy[random_index])

    # print("centroids = ", centroids)

    centroids = numpy.array(centroids)

    # ====== PUNKT 3 process of magnetizing
    stop = False

    while not stop:
        groups = [[], [], []]
        for idx in range(len(xy)):
            # Eucledean distance
            dist_min = numpy.sqrt((xy[idx][0] - centroids[0][0]) ** 2 + (xy[idx][1] - centroids[0][1]) ** 2)
            min_idx = 0
            for center in range(len(centroids)):
                dist = numpy.sqrt((xy[idx][0] - centroids[center][0]) ** 2 + (xy[idx][1] - centroids[center][1]) ** 2)
                if dist < dist_min:
                    min_idx = center
                    dist_min = dist
            groups[min_idx].append(xy[idx])
        print(len(groups[2]))

        count = 0
        for center in range(len(centroids)):
            new_x, new_y = 0, 0

            for avg in range(len(groups[center])):
                new_x += groups[center][avg][0]
                new_y += groups[center][avg][1]

            new_x /= len(groups[center])
            new_y /= len(groups[center])

            dx = abs(centroids[center][0] - new_x)
            dy = abs(centroids[center][1] - new_y)

            if dx < 0.1 and dy < 0.1:
                count += 1

            centroids[center][0] = new_x
            centroids[center][1] = new_y

        if count == 3:
            stop = True


plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=500, linewidths=4, color='green')
plt.scatter(x, y)

fig = plt.gcf()
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()


# ====