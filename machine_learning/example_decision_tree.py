from sklearn import tree
import numpy as np

import matplotlib.pylab as plt

X = np.array([[1, 1, 2], [1, 2, 1], [2, 1, 2], [2, 2, 1], [6,6, 5], [6,7, 5], [7,6, 6], [7,7, 6]])
Y = np.array([1, 1, 1, 1, 2, 2, 2, 2])

npts = len(X)
nvars = len(X[0])

# Make it so we can plot these variables
newX = X.swapaxes(0,1)

print newX

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print clf.predict([[5,5,5],[1,2,1]])

plt.figure()
plt.plot(newX[0],newX[1],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(newX[0],newX[2],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.figure()
plt.plot(newX[1],newX[2],'o')
plt.xlim(0,8)
plt.ylim(0,8)

plt.show()
