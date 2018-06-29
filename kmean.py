import csv
from matplotlib import pyplot as plt
import random

data_x = []
data_y = []

with open('output.csv', newline='') as csvfile:

    rows = csv.reader(csvfile)
    i = 0
    for row in rows:
        if (i < 0):
            for s in row:
                data_y.append(s)
        for s in row:
            data_x.append(s)
        i += 1


plt.scatter(data_x, data_y, color="blue", s=3)
