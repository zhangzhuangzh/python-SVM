import numpy as np
from sklearn import svm

f = open("E:\code\python\C1_TRAINING_SET.txt")
line = f.readline()
i = 0
X = [[0.0]*12]*307
Y = [0.0]*307

while line:
    # print(line)
    # print (line)
    a = line.split()
    a = np.array(a)
    a = a.astype(np.float)
    # print (len(a))

    for j in range(0, 12):
        X[i][j] = a[j]

    Y[i] = a[12]
    # print (a[12])
    # print (Y[i])
    i = i+1
    # break
    line = f.readline()
f.close()
print (i)
X.pop(0)
Y.pop(0)
print (X)
print (Y)
# X = [[0, 0], [2, 2]]
# y = [0.5, 2.5]
clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)
clf.fit(X, Y)
print ("result=")
print (clf.predict([[0.00000000, 1.00000000, 0.86206230, 0.88485846, 0.07665082, 1.00000000, 0.54064998,
                    0.00000000, 0.00000000, 0.00000000, 0.58191725, 0.00624169],
                   [0.00000000, 1.00000000, 0.86206230, 0.88485846, 0.07665082, 1.00000000, 0.54064998,
                    0.00000000, 0.00000000, 0.00000000, 0.58191725, 0.00624169]]))
