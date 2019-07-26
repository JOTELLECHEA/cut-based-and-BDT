import ROOT
import array as arr
from tabulate import tabulate
#------------------------------ root file -------------------------------------#
g = ROOT.TFile('all_hist.root')
#---------------------------- load Histogram ----------------------------------#
Dict0 = {1:'ttHH' ,2:'ttH',3:'ttZ',4:'ttbb'}
Dict1 = {}
for i in xrange(7):
    for j in xrange(1,4):
        Dict1[i] = Dict0[j] + str(i) + ' = g.Get(' + Dict0[j] + str(i) + ')'
        print Dict1[i]
