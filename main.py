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

print(xy)
x = xy[:, 0]
y = xy[:, 1]
plt.scatter(x, y)


# plt.scatter(xy[:, 0], xy[:, 1], marker='o', s=500, linewidths=2, c='none')
# plt.scatter(xy[:, 0], xy[:, 1], marker='x', s=500, linewidths=2)

plt.show()

# ====== PUNKT 2 find centroids

#get 3 randoms

