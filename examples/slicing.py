import numpy as np

x = np.random.random(100000)

y = x[x>0.2]

print len(x)
print len(y)


