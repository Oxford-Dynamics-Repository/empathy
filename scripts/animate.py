# Lucy Jackson (lucy@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This scripts visualizes the speech of the user and the AI with wave patterns.

import pyshine as ps
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

def animate(ax, audio):
    ax.clear()
    y = audio.get()
    
    for i in range(5):
        generate_graph_set(ax, y[i][0], y[i][1], random.randint(0,5)/10)
    
    ax.set_ylim( ymin=-0.2, ymax=0.2)	 
    ax.axis('off')

def generate_graph_set(ax, j, k, l):
    x = np.arange(0, 4 * np.pi, 0.1) # start, stop, step
    
    y_1 = np.sin(x) * k * np.sin(j * x)
    y_2 = y_1 * 0.9
    y_3 = y_1 * 0.8
    y_4 = y_1 * 0.7
    y_5 = y_1 * 0.6
    y_6 = y_1 * 0.5
    y_7 = y_1 * 0.4
    y_8 = y_1 * 0.3
    y_9 = y_1 * 0.2
    
    ax.plot(x + 0.1 * l, y_1, 'c', alpha = 0.9)
    ax.plot(x + 0.3 * l, y_2, 'c', alpha = 0.7)
    ax.plot(x + 0.5 * l, y_3, 'c', alpha = 0.6)
    ax.plot(x + 0.7 * l, y_4, 'c', alpha = 0.5)
    ax.plot(x + 0.9 * l, y_5, 'c', alpha = 0.4)
    ax.plot(x + 1.0 * l, y_6, 'c', alpha = 0.3)
    ax.plot(x + 1.1 * l, y_7, 'c', alpha = 0.2)
    ax.plot(x + 1.2 * l, y_8, 'c', alpha = 0.1)
    ax.plot(x + 1.3 * l, y_9, 'c', alpha = 0.05)


def main():
    audio,context = ps.audioCapture(mode='send')

    fig, ax = plt.subplots(figsize=(8,2))
    generate_graph_set(ax, 1, 0.5, 0.3)
    ax.axis('off')
    animation = FuncAnimation(fig, animate(ax, audio), frames=200, interval=10, repeat=False)
    plt.show()


if __name__ == '__main__':
    main()