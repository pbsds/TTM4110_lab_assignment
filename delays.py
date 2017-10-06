import matplotlib.pyplot as plt
from matplotlib.mlab import normpdf
import numpy as np
from collections import defaultdict

mu = [0.588, 23.064, 35.534, 0.348, 0.585, 11.835]
stdev = [0.276, 12.908, 20.117, 0.138, 0.275, 6.466]

#plt.xscale('log')
plt.ylabel('Delay (s)')
plt.xlabel('Smart meters')

plt.plot([1000,2000,4000], mu[0:3], 'ro-', label='Number of servers: 2')
plt.plot([1000,2000,4000], mu[3:6], 'bo-', label='Number of servers: 4')

plt.legend()

plt.show()