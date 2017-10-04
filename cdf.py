from statistics import mean, stdev
import matplotlib.pyplot as plt
from matplotlib.mlab import normpdf
import numpy as np
from collections import defaultdict

f = open("log.txt")
delays = [n for n in [float(l.strip().split()[1]) for l in f.readlines()] if n != -1]
delays.sort()

occurences = defaultdict(float)

for n in delays:
    occurences[n] += 1

for i in occurences.keys():
    occurences[i] = occurences[i] / len(delays)

values = np.cumsum(list(occurences.values()))

plt.hist(delays, bins=100, normed=True, cumulative=True, label='CDF DATA', histtype='step', alpha=0.55, color='purple') # bins and (lognormal / normal) datasets are pre-defined

plt.plot(list(occurences.keys()), values)

plt.show()