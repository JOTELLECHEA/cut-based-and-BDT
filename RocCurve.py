import sklearn 

if sklearn.__version__ == '0.20.4':
    from sklearn.model_selection import train_test_split
else :
    from sklearn.cross_validation import train_test_split
    
import matplotlib.mlab as mlab
import csv
import argparse
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from ROOT import*
from numpy import array
from root_numpy import root2array, rec2array
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, auc
from sklearn.preprocessing import StandardScaler
################################################################################
from scipy.interpolate import *
from scipy.stats import *
#################################################################################
parser = argparse.ArgumentParser(description= 'ROC curve plot from BDT')
parser.add_argument("--file", type=str, help= "Use '--file=' followed by a *.csv file")
args = parser.parse_args()
file = str(args.file)
df = pd.read_csv(file)
##################################################################################
def data(x):
	return np.array([float(i) for i in df['var'][x][1:-1].split()])

d0  = data(0)
d1  = data(1)
d2  = data(2)
d3  = data(3)
fpr = data(4)
tpr = data(5)
low_high = data(6)
# low_high = np.array([float(i) for i in str(df['var'][6])[1:-1].split(",")])

bins =30

roc_auc = auc(fpr, tpr)
plt.subplot(211)
r = 0.00606061
g = 0.0000677966
b = 0.00147541
m = 0.0001111
t = 0.0000764706 
x = np.linspace(0,1,1000)
plt.title('Receiver operating characteristic')
plt.plot(fpr, tpr, lw=1, label='ROC (area = %0.6f)'%(roc_auc))
#plt.plot((b,b),(0,1),'b--', label='ttH')
#plt.plot((m,m),(0,1),'m--', label='ttZ')
# plt.plot((g,g),(0,1),'g--', label='ttbb')
plt.plot((t,t),(0,1),'k--', label='total')
plt.plot(x,r + 0*x,linestyle='--',color='r', label='ttHH')
# plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid()
plt.legend(loc="lower right")
#plt.savefig('battery.png', format='png', dpi=300)
plt.subplot(212)
plt.hist(d0,color='r', alpha=0.5, range=low_high, bins=bins,histtype='stepfilled', density=True,label='S (train)')
plt.hist(d1,color='b', alpha=0.5, range=low_high, bins=bins,histtype='stepfilled', density=True,label='B (train)')

hist, bins = np.histogram(d2,bins=bins, range=low_high, density=True)
scale = len(d2) / sum(hist)
err = np.sqrt(hist * scale) / scale
width = (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.errorbar(center, hist, yerr=err, fmt='o', c='r', label='S (test)')

hist, bins = np.histogram(d3,bins=bins, range=low_high, density=True)
scale = len(d2) / sum(hist)
err = np.sqrt(hist * scale) / scale
plt.errorbar(center, hist, yerr=err, fmt='o', c='b', label='B (test)')
plt.xlabel("BDT output")
plt.ylabel("Arbitrary units")
plt.legend(loc='upper left')
plt.yscale('log')
plt.show()
