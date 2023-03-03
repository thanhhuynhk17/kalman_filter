import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
from constants import NROWS, NCOLS

def plot_radiomap(ax, nrows=NROWS,ncols=NCOLS, grid_state=0):
    # init layout
    radiomap = np.full((nrows, ncols), grid_state)
    # init heatmap
    sns.color_palette("flare", as_cmap=True)
    ax = sns.heatmap(radiomap, cmap="flare",
                    vmin=0, vmax=1,
                    linewidths=0.1,
                    # annot=True, fmt='.1f'
                    )
    return ax