from sklearn import tree
import numpy as np

import sys

import matplotlib.pylab as plt

infilename0 = sys.argv[1]
infilename1 = sys.argv[2]
infilename2 = sys.argv[3]

infile0 = open(infilename0,'r')
infile1 = open(infilename1,'r')
infile2 = open(infilename2,'r')

Xtrain = np.array([])
Ytrain = np.array([])

Xtest = np.array([])

nlines = 0
for line in infile0:
    Xtrain = np.append(Xtrain,np.array(line.split()).astype('float'))
    Ytrain = np.append(Ytrain,0)
    nlines += 1

for line in infile1:
    Xtrain = np.append(Xtrain,np.array(line.split()).astype('float'))
    Ytrain = np.append(Ytrain,1)
    nlines += 1

Xtrain = Xtrain.reshape(nlines,5)
print Xtrain

nlines = 0
for line in infile2:
    Xtest = np.append(Xtest,np.array(line.split()).astype('float'))
    nlines += 1

Xtest = Xtest.reshape(nlines,5)


# Make it so we can plot these variables
newXtrain = Xtrain.swapaxes(0,1)
newXest = Xtrain.swapaxes(0,1)

print newXtrain

clf = tree.DecisionTreeClassifier()
clf = clf.fit(Xtrain, Ytrain)

predictions = clf.predict(Xtest)
print predictions

plt.figure()
plt.plot(newXtrain[0][Ytrain==0],newXtrain[1][Ytrain==0],'o')
plt.plot(newXtrain[0][Ytrain==1],newXtrain[1][Ytrain==1],'o')
plt.xlim(0,1)
plt.ylim(0,1)

plt.figure()
plt.plot(newXtrain[0][Ytrain==0],newXtrain[2][Ytrain==0],'o')
plt.plot(newXtrain[0][Ytrain==1],newXtrain[2][Ytrain==1],'o')
plt.xlim(0,1)
plt.ylim(0,1)

plt.figure()
plt.plot(newXtrain[3][Ytrain==0],newXtrain[4][Ytrain==0],'o')
plt.plot(newXtrain[3][Ytrain==1],newXtrain[4][Ytrain==1],'o')
plt.xlim(0,1)
plt.ylim(0,1)


plt.show()
