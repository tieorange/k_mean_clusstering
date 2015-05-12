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

graph = plt.scatter(x, y)

def onclick(event):
    centroids = []
    for r in range(3):
        random_index = random.uniform(0, len(xy))
        centroids.append(xy[random_index])

    centroids = numpy.array(centroids)

    # ====== PUNKT 3 process of magnetizing
    stop = False

    while not stop:
        groups = [[], [], []]
        for idx in range(len(xy)):
            # Eucledean distance
            dist_min = numpy.sqrt((xy[idx][0] - centroids[0][0]) ** 2 + (xy[idx][1] - centroids[0][1]) ** 2)
            min_idx = 0
            for center_idx in range(len(centroids)):
                dist = numpy.sqrt((xy[idx][0] - centroids[center_idx][0]) ** 2 + (xy[idx][1] - centroids[center_idx][1]) ** 2)
                if dist < dist_min:
                    min_idx = center_idx
                    dist_min = dist
            groups[min_idx].append(xy[idx])
        print(len(groups[2]))

        count = 0
        for center_idx in range(len(centroids)):
            new_x, new_y = 0, 0

            for avg_idx in range(len(groups[center_idx])):
                new_x += groups[center_idx][avg_idx][0]
                new_y += groups[center_idx][avg_idx][1]

            new_x /= len(groups[center_idx])
            new_y /= len(groups[center_idx])

            dx = abs(centroids[center_idx][0] - new_x)
            dy = abs(centroids[center_idx][1] - new_y)

            if dx < 0.1 and dy < 0.1:
                count += 1

            centroids[center_idx][0] = new_x
            centroids[center_idx][1] = new_y

        if count == 3:
            stop = True

    centroids = numpy.array(centroids)
    update_line(graph, centroids)


def update_line(hl, new_data):
    plt.clf()
    plt.scatter(x, y)

    plt.scatter(new_data[:, 0], new_data[:, 1], s=500, c='g', marker='x')
    plt.draw()


fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.ion()
plt.show()
# ====