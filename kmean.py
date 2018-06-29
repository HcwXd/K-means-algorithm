import csv
from matplotlib import pyplot as plt
import random

"""
Step0. Read data(X1, X2, X3, Xi)
Step1. Randomly pick K random points as cluster centers called centroids.
Step2. Assign each data to the clusters by its distance
Step3. Pick new centroids by the clusters
Step4. Repeat Step3 and Step4 til the world end
"""


def geo_distance(ax, ay, bx, by):
    return((ax-bx)**2+(ay-by)**2)**(1/2)


data_x = []
data_y = []

# Step0. Read data(X1, X2, X3, Xi)

with open('data.csv', newline='') as csvfile:

    rows = csv.reader(csvfile)
    i = 0
    for row in rows:
        if (i > 0):
            for s in row:
                data_y.append(float(s))
            break
        for s in row:
            data_x.append(float(s))
        i += 1

# plt.scatter(data_x, data_y, color="blue", s=3)

number_of_ans = 3
centeroid_x = []
centeroid_y = []
cluster_group_x = []
cluster_group_y = []

# Step1. Randomly pick K random points as cluster centers called centroids.

for i in range(number_of_ans):
    centeroid_x.append(random.randint(min(data_x), max(data_x)))
    centeroid_y.append(random.randint(min(data_y), max(data_y)))

""" Display
plt.scatter(data_x, data_y, color="blue", s=3)
plt.scatter(centeroid_x, centeroid_y, color="red")
"""

# Step2. Assign each data to the clusters by its distance
for i in range(number_of_ans):
    cluster_group_x.append([])
    cluster_group_y.append([])

for index in range(len(data_x)):
    x = data_x[index]
    y = data_y[index]
    distance = []
    for s in range(number_of_ans):
        distance.append(geo_distance(
            x, y, centeroid_x[s], centeroid_y[s]))
    min_distance = min(distance)
    min_index = distance.index(min_distance)
    cluster_group_x[min_index].append(x)
    cluster_group_y[min_index].append(y)

""" Display
plt.scatter(cluster_group_x[0], cluster_group_y[0], color="blue", s=3)
plt.scatter(cluster_group_x[1], cluster_group_y[1], color="yellow", s=3)
plt.scatter(cluster_group_x[2], cluster_group_y[2], color="green", s=3)
plt.scatter(centeroid_x, centeroid_y, color="black")
"""
