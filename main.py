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

x2 = numpy.random.normal(1, 0.2, (100, 2))
y2 = numpy.random.normal(3, 0.3, (100, 2))
plt.scatter(x2, y2)
plt.show()

