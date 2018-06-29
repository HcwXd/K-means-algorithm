from matplotlib import pyplot as plt
import random

"""
Step0. Read data(X1, X2, X3, Xi)
Step1. Randomly pick K random points as cluster centers called centroids.
Step3. Assign each data to the clusters by its distance
Step4. Pick new centroids by the clusters
Step5. Repeat Step3 and Step4 til the world end
"""


def data_generation():
    number_of_data = 1000
    number_of_ans = 3
    answer = [[30000, 20000], [80000, 50000], [40000, 70000]]
    ans_x = []
    ans_y = []

    data_x = []
    data_y = []

    for i in answer:
        ans_x.append(i[0])
        ans_y.append(i[1])

    for i in range(int(number_of_data/2)):
        for j in range(number_of_ans):
            error_nx = random.randint(-10000, 10000)
            error_ny = random.randint(-10000, 10000)
            error_px = random.randint(-10000, 10000)
            error_py = random.randint(-10000, 10000)
            data_x.append(ans_x[j] + random.randint(-20000 +
                                                    error_nx, 20000 + error_ny))
            data_y.append(ans_y[j] + random.randint(-20000 +
                                                    error_px, 20000 + error_py))
    for i in range(int(number_of_data/(5/2))):
        for j in range(number_of_ans):
            error_nx = random.randint(-10000, 10000)
            error_ny = random.randint(-10000, 10000)
            error_px = random.randint(-10000, 10000)
            error_py = random.randint(-10000, 10000)
            data_x.append(ans_x[j] + random.randint(-10000 +
                                                    error_nx, 10000 + error_ny))
            data_y.append(ans_y[j] + random.randint(-10000 +
                                                    error_px, 10000 + error_py))
    for i in range(int(number_of_data/(5/2))):
        for j in range(number_of_ans):
            error_nx = random.randint(-10000, 10000)
            error_ny = random.randint(-10000, 10000)
            error_px = random.randint(-10000, 10000)
            error_py = random.randint(-10000, 10000)
            data_x.append(ans_x[j] + random.randint(-20000 +
                                                    error_nx, 20000 + error_ny))
            data_y.append(ans_y[j] + random.randint(-20000 +
                                                    error_px, 20000 + error_py))
    for i in range(int(number_of_data/(5/1))):
        for j in range(number_of_ans):
            error_nx = random.randint(-20000, 20000)
            error_ny = random.randint(-20000, 20000)
            error_px = random.randint(-20000, 20000)
            error_py = random.randint(-20000, 20000)
            data_x.append(ans_x[j] + random.randint(-20000 +
                                                    error_nx, 20000 + error_ny))
            data_y.append(ans_y[j] + random.randint(-20000 +
                                                    error_px, 20000 + error_py))

    plt.scatter(data_x, data_y, color="blue", s=3)
    plt.scatter(ans_x, ans_y, color="red")
    return data_x, data_y


data_x, data_y = data_generation()
