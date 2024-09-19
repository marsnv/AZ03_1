import numpy as np
import matplotlib.pyplot as plt
def plot_histogram(mean=0, std_dev=1, num_samples=1000):
    data = np.random.normal(mean, std_dev, num_samples)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, color='blue', alpha=0.7)
    plt.title('Гистограмма нормального распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

mean = 0
std_dev = 1
num_samples = 1000

plot_histogram(mean, std_dev, num_samples)