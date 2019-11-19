
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

# fpr   = df['fpr']
# tpr   = df['tpr']
fpr = [0.00000000e+00,3.70096225e-05,7.03182828e-04,2.66469282e-03, 7.84603997e-03,2.23908216e-02,2.27239082e-02,5.66617321e-02, 1.27757217e-01,2.50185048e-01,4.37971873e-01,6.57549963e-01,8.44041451e-01,9.51443375e-01,9.90932642e-01,1.00000000e+00]
tpr = [0.,0.,0.00393258,0.01516854,0.04269663,0.11067416,0.11123596,0.21910112,0.39606742,0.61067416,0.81067416,0.93764045,0.98764045,0.99775281,1.,1.]
roc_auc = auc(fpr, tpr)
# slope,intercept,r_value,p_value,std_err = linregress(fpr,tpr)# method 1 
p2 = np.polyfit(fpr,tpr,5)
# c = df['var'][0]
# c = c.strip('[]')
# c = [c.replace(" ", ",")]
# c = c.replace("'", "")
# c = list(c.strip() for x in c)
# center = c.replace(" ", ",")
# center1 = center.strip("'")

# # plt.subplot(211)
# plt.plot(fpr, tpr, 'ro', label='ROC (area = %0.2f)'%(roc_auc))
# plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
# plt.xlim([-0.05, 1.05])
# plt.ylim([-0.05, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic')
# plt.legend(loc="lower right")
# plt.grid()
# plt.show()

x = np.linspace(-.0001,1,1000)
# plt.figure()
plt.title('Receiver operating characteristic')
plt.plot(fpr, tpr, 'ro', label='ROC (area = %0.2f)'%(roc_auc))
plt.plot(x,np.polyval(p2,x), label='fit')
plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid()
plt.legend(loc="lower right")
#plt.savefig('battery.png', format='png', dpi=300)
plt.show()