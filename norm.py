# importing pyplot as plt histogram
import matplotlib.pyplot as plt
 
# position
pos = 100
# scale
scale = 5
 
# size
size = 100000
 
# creating a normal distribution data
values = np.random.normal(pos, scale, size)
 
# plotting histograph
plt.hist(values, 100)
 
# showing the graph
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
  
# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-20, 20, 0.01)
  
# Calculating mean and standard deviation
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)
  
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()