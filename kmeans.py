from matplotlib import pyplot as plt
import random

"""
Step0. Read data(X1, X2, X3, Xi)
Step1. Randomly pick K random points as cluster centers called centroids.
Step3. Assign each data to the clusters by its distance
Step4. Pick new centroids by the clusters
Step5. Repeat Step3 and Step4 til the world end
"""


number_of_data = 100
number_of_ans = 3
answer = [[3000, 2000], [8000, 5000], [4000, 7000]]
ans_x = []
ans_y = []

data_x = []
data_y = []

for i in answer:
    ans_x.append(i[0])
    ans_y.append(i[1])

for i in range(number_of_data):
    for j in range(number_of_ans):
        error_nx = random.randint(-2000, 2000)
        error_ny = random.randint(-2000, 2000)
        error_px = random.randint(-2000, 2000)
        error_py = random.randint(-2000, 2000)
        data_x.append(ans_x[j] + random.randint(-2000 +
                                                error_nx, 2000 + error_ny))
        data_y.append(ans_y[j] + random.randint(-2000 +
                                                error_px, 2000 + error_py))


plt.scatter(data_x, data_y, color="blue")
plt.scatter(ans_x, ans_y, color="red")
