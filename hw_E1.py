import matplotlib.pyplot as plt 
import numpy as np 
import random 
s = np.random.poisson(random.randint(1,50000), random.randint(1,50000)) 
count, bins, ignored = plt.hist(s, 14, density=True) 
plt.show()
