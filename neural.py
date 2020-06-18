# Written By : Jonathan O. Tellechea
# Adviser    : Mike Hance, Phd
# Research   : Using a neural network to maximize the significance of tttHH production.
# Reference  :http://cdsweb.cern.ch/record/2220969/files/ATL-PHYS-PUB-2016-023.pdf
from ROOT import*
from root_numpy import array2root,root2array,rec2array
import csv,sys
import argparse
import pandas as pd
import numpy as np
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# file= 'ROC_data'
tree = 'OutputTree'

parser = argparse.ArgumentParser(description= 'BDT for ttHH and background')
parser.add_argument("--branch", default='wrong', type=str, help= "Use '--branch=' followed by a branch_name")

args = parser.parse_args()
branch = str(args.branch)

bn_phase1   = """njet""".split(",")
bn_phase2   = """njet,btag,srap""".split(",")
bn_phase3   = """njet,btag,srap,cent,m_bb,h_b""".split(",")
bn_phase4   = """njet,btag,srap,cent,m_bb,h_b,mt1,mt2,mt3,dr1,dr2,dr3""".split(",")
bn_phase5   = """njet,btag,srap,cent,m_bb,h_b,mt1,mt2,mt3,dr1,dr2,dr3,chi""".split(",")

while True:
    try:
        if branch == 'phase1':
            print 'You selected option:', branch
            branch_names = bn_phase1
            # name = file + '_' + branch + '.csv'
            break
        elif branch == 'phase2':
            print 'You selected option:', branch
            branch_names = bn_phase2
            # name = file + '_' + branch + '.csv'
            break
        elif branch == 'phase3':
            print 'You selected option:', branch
            branch_names = bn_phase3
            # name = file + '_' + branch + '.csv'
            break
        elif branch == 'phase4':
            print 'You selected option:', branch
            branch_names = bn_phase4
            # name = file + '_' + branch  + '.csv'
            break
        elif branch == 'phase5':
            print 'You selected option:', branch
            branch_names = bn_phase5
            # name = file + '_' + branch + '.csv'
            break
        elif branch == 'wrong':
            sys.exit('Need to pass a variable, use --h for options')
    except NameError:
        system('clear')
        prRed('*******************Invalid option **************\n')
        break


branch_names = [c.strip() for c in branch_names]
branch_names = (b.replace(" ", "_") for b in branch_names)
branch_names = list(b.replace("-", "_") for b in branch_names)

signal = root2array('new_signal_tthh.root',tree, branch_names, include_weight=True)
signal = rec2array(signal)

bg_ttbb   = root2array('new_background_ttbb.root', tree, branch_names, include_weight=True)
bg_ttZ    = root2array('new_background_ttZ.root' , tree, branch_names, include_weight=True)
bg_ttH    = root2array('new_background_ttH.root' , tree, branch_names, include_weight=True)
background    = np.concatenate((bg_ttbb,bg_ttH,bg_ttZ))
background    = rec2array(background)

X = np.concatenate((signal, background)) 
y = np.concatenate((np.ones(signal.shape[0]), np.zeros(background.shape[0])))
X_dev,X_eval, y_dev,y_eval = train_test_split(X, y, test_size = 0.10, random_state=42)
X_train,X_test, y_train,y_test, = train_test_split(X_dev, y_dev, test_size = 0.5,random_state=42)  
# mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
# mlp.fit(X_train, y_train.values.ravel())
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train)

predictions = mlp.predict(X_test)


print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))