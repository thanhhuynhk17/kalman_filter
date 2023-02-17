import pandas as pd
import numpy as np
# plot section
from itertools import count
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from constant import FNAME, BEACON, TIME_OUT

def animate(i):
    data = pd.read_csv(FNAME,header=None)

    xs = list(range(len(data)))
    ys = data[0].values
    ys_filtered = data[1].astype(int).values
    plt.cla()
    plt.title(BEACON)
    plt.grid()
    plt.plot(xs, ys, label='Raw RSSI')
    plt.plot(xs, ys_filtered, label='Filtered')
    plt.legend()

def main():
    try:
        ani = animation.FuncAnimation(plt.gcf(), animate)
        plt.show()
    except KeyboardInterrupt:
        print('save & close figure')
        plt.savefig(f'img/Figure_{BEACON}.png')
        plt.close()

if __name__ == "__main__":
    main()