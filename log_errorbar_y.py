import numpy as np
import matplotlib.pyplot as plt

def log_errorbar_y(ax, x, y, yerr, **kwargs):
    '''
    Plot errorbars but for log scale, where errors need to be transfromed:
    You are plotting x vs y, and in a cartesian coordinates plot you would use +-dy for error bars.
    But d(log(y)) != log(dy), which is what you usually get when plotting an errorbar in log scale.
    The correct way would be:
    d(log(y)) = 1 / ln(10) * dy / y
    '''
    dy = np.array(yerr)
    dy = 1 / np.log(10) * np.multiply(dy, 1/y)

    '''
    However, matplotlib will plot
    log(y +- yerr), but I want it to plot log(y) +- dy,
    so we give it
    yerr_pos = y*10^dy - y -> log(y + yerr_pos) = log(y*10^dy) = log(y) + dy
    and
    yerr_neg = y - y/10^dy -> log(y - yerr_neg) = log(y/10^dy) = log(y) - dy
    '''
        
    yerr = np.zeros([2,len(y)])
    yerr[0] = np.multiply( y, 1 - 1/(10**dy) )
    yerr[1] = np.multiply( y, 10**dy - 1 )

    ax.errorbar(x, y, yerr = yerr, **kwargs)
    ax.set_xscale('log')
    ax.set_yscale('log')

