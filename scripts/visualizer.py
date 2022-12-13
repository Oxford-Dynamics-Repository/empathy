import matplotlib.pyplot as plt
import numpy as np
import time
#Adding text inside a rectangular box by using the keyword 'bbox'
class PrintOutputs:
    def __init__(self):
        x = np.arange(-10, 10, 0.01)
        y = x**2
        self.fig, self.ax = plt.subplots()
        self.ax.axis('off')
        self.ax.plot(x, y, c = 'w')
        plt.show(block=False)
        self.user_loco = 110
        self.avis_loco = 100
    # PRINT AVIS
    def print_avis(self, text_file):
        avis = open(text_file).readlines()
        self.avis_count = len(avis)
        self.ax.text(-14, self.avis_loco, f'Avis: {avis[self.avis_count-1]}', fontsize = 20,
                bbox = dict(facecolor = 'turquoise', alpha = 0.5, boxstyle="round,pad=0.1"))
        # plt.plot(x, y, c = 'w')
        print(f'avis_loco: {self.avis_loco}')
        self.avis_loco -= 20
        plt.draw()
    # Print User
    def print_user(self, text_file):
        user = open(text_file).readlines()
        self.user_count = len(user)
        plt.text(-14, self.user_loco, f'User: {user[self.user_count-1]}', fontsize = 20,
                bbox = dict(facecolor = 'white', alpha = 0.5, boxstyle="round,pad=0.1"))
        print(f'user_loco: {self.user_loco}')
        self.user_loco -= 20
        # plt.plot(x, y, c = 'w')
        plt.draw()
