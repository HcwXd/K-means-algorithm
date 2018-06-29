import csv
from matplotlib import pyplot as plt
import random

"""
Step0. Read data(X1, X2, X3, Xi)
Step1. Randomly pick K random points as cluster centers called centroids.
Step3. Assign each data to the clusters by its distance
Step4. Pick new centroids by the clusters
Step5. Repeat Step3 and Step4 til the world end
"""

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

# Step1. Randomly pick K random points as cluster centers called centroids.

for i in range(number_of_ans):
    centeroid_x.append(min(data_x) - max(data_x))
    centeroid_y.append(min(data_y) - max(data_y))
