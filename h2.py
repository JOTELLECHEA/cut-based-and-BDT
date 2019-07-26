import ROOT
import array as arr
from tabulate import tabulate
#------------------------------ root file -------------------------------------#
g = ROOT.TFile('all_hist.root')
#---------------------------- load Histogram ----------------------------------#
Dict0 = {1:'ttHH' ,2:'ttH',3:'ttZ',4:'ttbb'}
Dict1 = {}
count = 1
for i in xrange(8):
     for j in xrange(1,5):
         # Dict1[i]={}
         histtoget=Dict0[j]+str(i)
         print histtoget
         Dict1[count]=g.Get(histtoget)
         count += 1
