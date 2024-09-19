import numpy as np
import matplotlib.pyplot as plt

def plot_scatter(num_points=22):
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='green', alpha=0.7)
    plt.title('Диаграмма рассеяния случайных данных')
    plt.xlabel('Значения X')
    plt.ylabel('Значения Y')
    plt.grid(True)
    plt.show()

plot_scatter(22)
