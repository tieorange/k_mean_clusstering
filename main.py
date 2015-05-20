import random

import matplotlib.pyplot as plt
from matplotlib import style
import numpy

style.use("ggplot")


def start():
    centroids = get_centroids()
    moving_centroids(centroids)
    update_line(numpy.array(centroids))

    generate_normal_distribution()


def onclick(event):
    start()


def update_line(new_data):
    plt.clf()
    plt.scatter(x, y)

    plt.scatter(new_data[:, 0], new_data[:, 1], linewidths=4, s=500, c='g', marker='x')
    plt.draw()

def get_centroids():
    # ====== PUNKT 2 find centroids
    centroids = []
    for r in range(3):
        random_index = random.uniform(0, len(xy))
        centroids.append(xy[random_index])
    centroids = numpy.array(centroids)
    return centroids


def moving_centroids(centroids):
    # ====== PUNKT 3 process of magnetizing
    stop = False
    while not stop:
        groups_of_centroid_and_points = [[], [], []]  # because we have 3 groups
        # ---- Making an array of which point is closer to which centroid
        for idx in range(len(xy)):
            # Eucledean distance between each point and centroid
            dist_min = numpy.sqrt(
                (xy[idx][0] - centroids[0][0]) ** 2 + (xy[idx][1] - centroids[0][1]) ** 2)  # TODO: move to func
            min_idx = 0
            for center_idx in range(len(centroids)):
                # distance between point and zero(random) centroid
                dist = numpy.sqrt(
                    (xy[idx][0] - centroids[center_idx][0]) ** 2 + (xy[idx][1] - centroids[center_idx][1]) ** 2)
                if dist < dist_min:
                    min_idx = center_idx
                    dist_min = dist
            groups_of_centroid_and_points[min_idx].append(xy[idx])  # min_idx <- index of centroid with minimal distance

        # Finding new "correct" position centroid (finding center of group of points)
        count = 0
        for center_idx in range(len(centroids)):
            new_x, new_y = 0, 0

            for avg_idx in range(len(groups_of_centroid_and_points[center_idx])):
                new_x += groups_of_centroid_and_points[center_idx][avg_idx][0]  # finding sum of Xs
                new_y += groups_of_centroid_and_points[center_idx][avg_idx][1]

            new_x /= len(groups_of_centroid_and_points[center_idx])  # to find average we have to divide sum by size
            new_y /= len(groups_of_centroid_and_points[center_idx])

            delta_x = abs(centroids[center_idx][0] - new_x)  # to check if centroid stopped moving
            delta_y = abs(centroids[center_idx][1] - new_y)

            if delta_x == 0 and delta_y == 0:
                count += 1  # one of centroid stopped moving

            centroids[center_idx][0] = new_x
            centroids[center_idx][1] = new_y

        if count == 3:  # all of centroids has stopped moving
            stop = True


def generate_normal_distribution():
    global group1, group2, group3, xy, x, y
    # generate 3 sets of normally distributed points around
    # ===== PUNKT #1 random points
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html
    # numpy.random.normal(loc=0.0, scale=1.0, size=None)
    group1 = numpy.random.normal(1, 0.2, (100, 2))
    group2 = numpy.random.normal(2, 0.5, (300, 2))
    group3 = numpy.random.normal(3, 0.3, (100, 2))
    print("group1 = ", group1)
    # slightly move sets 2 and 3 (for a prettier output)
    group2[:, 0] += 3
    group3[:, 0] -= 1.5
    xy = numpy.concatenate((group1, group2, group3))
    # plot colored points
    # print(xy)
    x = xy[:, 0]
    y = xy[:, 1]


generate_normal_distribution()


fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.ion()
plt.show()

