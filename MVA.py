#!/cvmfs/sft.cern.ch/lcg/releases/LCG_94/Python/2.7.15/x86_64-slc6-gcc62-opt/bin/python
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
name = 'data_ROC_Curve.csv'
tree = 'OutputTree'

branch_names = """njet""".split(",")
# branch_names = """njet,met,met_phi,nlep,lep1pT,lep1eta,lep1phi,lep1m,lep2pT,lep2eta,lep2phi,lep2m,lep3pT,lep3eta,lep3phi""".split(",")
# branch_names = """njet,met,met_phi,nlep,lep1pT,lep1eta,lep1phi,lep1m,lep2pT,lep2eta,lep2phi,lep2m,lep3pT,lep3eta,lep3phi,lep3m,mt1,mt2,mt3""".split(",")
branch_names = [c.strip() for c in branch_names]
branch_names = (b.replace(" ", "_") for b in branch_names)
branch_names = list(b.replace("-", "_") for b in branch_names)

signal = root2array('new_signal.root',tree, branch_names, include_weight=True)
signal = rec2array(signal)

background = root2array('new_background.root', tree, branch_names, include_weight=True)
background = rec2array(background)

X = np.concatenate((signal, background)) 
y = np.concatenate((np.ones(signal.shape[0]), np.zeros(background.shape[0])))
X_dev,X_eval, y_dev,y_eval = train_test_split(X, y, test_size = 0.10, random_state=42)
X_train,X_test, y_train,y_test, = train_test_split(X_dev, y_dev, test_size = 0.10,random_state=42)             


dt = DecisionTreeClassifier(max_depth=3, min_samples_split=2, splitter='best')
bdt = AdaBoostClassifier(dt, algorithm ='SAMME', n_estimators=1000, learning_rate=1.0)
bdt.fit(X_train, y_train)
y_predicted = bdt.predict(X_test)
print classification_report(y_test, y_predicted,target_names=["background", "signal"])
print "Area under ROC curve: %.4f"%(roc_auc_score(y_test,bdt.decision_function(X_test)))

# ROC Curve
decisions = bdt.decision_function(X_test)
fpr, tpr, thresholds = roc_curve(y_test, decisions)
roc_auc = auc(fpr, tpr)
plt.subplot(211)
plt.plot(fpr, tpr, lw=1, label='ROC (area = %0.2f)'%(roc_auc))
plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.grid()

#BDT Distribution
def compare_train_test(clf, X_train, y_train, X_test, y_test, bins=30):
    decisions = []
    for X,y in ((X_train, y_train), (X_test, y_test)):
        d1 = clf.decision_function(X[y>0.5]).ravel()
        d2 = clf.decision_function(X[y<0.5]).ravel()
        decisions += [d1, d2]
    print decisions[0]   
    low = min(np.min(d) for d in decisions)
    high = max(np.max(d) for d in decisions)
    low_high = (low,high)
    
    plt.subplot(212)
    plt.hist(decisions[0],color='r', alpha=0.5, range=low_high, bins=bins,histtype='stepfilled', normed=True,label='S (train)')
    plt.hist(decisions[1],color='b', alpha=0.5, range=low_high, bins=bins,histtype='stepfilled', normed=True,label='B (train)')

    hist, bins = np.histogram(decisions[2],bins=bins, range=low_high, normed=True)
    scale = len(decisions[2]) / sum(hist)
    err = np.sqrt(hist * scale) / scale
    
    width = (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.errorbar(center, hist, yerr=err, fmt='o', c='r', label='S (test)')
    hist1 = hist
    bins1 = bins
    scale1 = scale
    err1 = err
    
    hist, bins = np.histogram(decisions[3],bins=bins, range=low_high, normed=True)
    scale = len(decisions[2]) / sum(hist)
    err = np.sqrt(hist * scale) / scale

    plt.errorbar(center, hist, yerr=err, fmt='o', c='b', label='B (test)')
    
################################################################################################
    r1  = ['center',center]
    r2  = ['hist',hist]
    r3  = ['bins1',bins1]
    r4  = ['bins',bins]
    r5  = ['scale1',scale1]
    r6  = ['scale',scale]
    r7  = ['err',err]
    r8  = ['fpr',fpr]
    r9  = ['tpr',tpr]
    r10 = ['thresholds',thresholds]

    with open('data_ROC_Curve.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(r1)
        writer.writerow(r2)
        writer.writerow(r3)
        writer.writerow(r4)
        writer.writerow(r5)
        writer.writerow(r6)
        writer.writerow(r7)
        writer.writerow(r8)
        writer.writerow(r9)
        writer.writerow(r10)

    csvFile.close()
################################################################################################


    plt.xlabel("BDT output")
    plt.ylabel("Arbitrary units")
    plt.legend(loc='upper left')
    plt.yscale('log')
    plt.show()
    
compare_train_test(bdt, X_train, y_train, X_test, y_test)

# BDT to TTree
from root_numpy import array2root
y_predicted = bdt.decision_function(X)
y_predicted.dtype = [('y', np.float64)]
array2root(y_predicted, "BDToutput_test.root", "BDToutput_test")

plt.show()




