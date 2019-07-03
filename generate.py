import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlib


def generateCurveBetweenPoints(a, b, width, dpi=.1):
    ny = int(width / dpi)
    nx = int((b[0] - a[0]) / dpi)
    data = np.random.randint(-ny, ny, nx)
    x, y = [], []
    for i in range(1, nx + 1):
        x.append(a[0] + i * dpi)
        y.append(a[1] + data[i-1] * dpi)
    return x, y


def generateNormalCurveBetweenPoints(a, b, width, dpi=.1):
    ny = int(width / dpi)
    nx = int((b[0] - a[0]) / dpi)
    mu, sigma = 0, 0.3 * ny # mean and standard deviation
    data = np.random.normal(mu, sigma, nx)
    x, y = [], []
    for i in range(1, nx + 1):
        x.append(a[0] + i * dpi)
        y.append(a[1] + (data[i-1] if abs(data[i-1]) < ny else ny) * dpi)
    return x, y


if __name__ == '__main__':
    for i in range(10):
        x, y = generateCurveBetweenPoints([0, 2], [10, 2], 2)
        plt.clf()
        plt.xlim([0,10])
        plt.ylim([0,4])
        plt.plot(0, 2, 'o')
        plt.plot(10, 2, 'o')
        plt.plot(x, y)
        plt.savefig("fig_{0}.png".format(i))
	
    for i in range(10):
        x, y = generateNormalCurveBetweenPoints([0, 2], [10, 2], 2)
        plt.clf()
        plt.xlim([0,10])
        plt.ylim([0,4])
        plt.plot(0, 2, 'o')
        plt.plot(10, 2, 'o')
        plt.plot(x, y)
        plt.savefig("fig-normal_{0}.png".format(i))	