
import matplotlib.mlab as mlab
import csv
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from ROOT import*
from root_numpy import root2array, rec2array
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, auc
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV,train_test_split
#########
from scipy.interpolate import *
from scipy.stats import *
#########
file = 'data_ROC_Curve.csv'
df = pd.read_csv(file)
def data(x):
	return np.array([float(i) for i in df['var'][x][1:-1].split()])

h1  = data(0)
b1  = data(1)
s1  = data(2)
h2  = data(3)
b2  = data(4)
s2  = data(5)
fpr = data(6)
tpr = data(7)

roc_auc = auc(fpr, tpr)
p2 = np.polyfit(fpr,tpr,5)
plt.subplot(211)
x = np.linspace(-.0001,1,1000)
plt.title('Receiver operating characteristic')
plt.plot(fpr, tpr, 'ro', label='ROC (area = %0.2f)'%(roc_auc))
plt.plot(x,np.polyval(p2,x), label='fit')
plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid()
plt.legend(loc="lower right")
#plt.savefig('battery.png', format='png', dpi=300)
plt.subplot(212)
# plt.hist(h1,color='r', alpha=0.5,  bins=b1,histtype='stepfilled', normed=True,label='S (train)')
# plt.hist(h2,color='b', alpha=0.5,  bins=b2,histtype='stepfilled', normed=True,label='B (train)')

err1 = np.sqrt(h1 * s1) / s1

width = (b1[1] - b1[0])
center = (b1[:-1] + b1[1:]) / 2
plt.errorbar(center, h1, yerr=err1, fmt='o', c='r', label='S (test)')


s2 = len(h2) / sum(h2)
err = np.sqrt(h2 * s2) / s2

plt.errorbar(center, h2, yerr=err, fmt='o', c='b', label='B (test)')
plt.xlabel("BDT output")
plt.ylabel("Arbitrary units")
plt.legend(loc='upper left')
# plt.yscale('log')
plt.show()