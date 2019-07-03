# Written By : Jonathan O. Tellechea
# Adviser    : Mike Hance, Phd
# Research   : ttHH
# Description: Histogram of ttHH from pg.8 in http://cdsweb.cern.ch/record/2220969/files/ATL-PHYS-PUB-2016-023.pdf
#------------------------------------------------------------------------------#
import ROOT,sys
import numpy as np
from os import system
from time import sleep
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
#------------------------------------------------------------------------------#
def menu():
    print '               __________________________________________'
    print '              |                                          |'
    print '              |Welcome to the ttHH Histogram Script 2019 |'
    print '              |__________________________________________| \n\n'
    print '_______________________________\n'
    print '# [1] -',u'tt\u0304HH (HH -> 'u'bb\u0304',u'bb\u0304)    #'
    print '# [2] -',u'tt\u0304bb\u0304 + jets           #'
    print '# [3] -',u'tt\u0304H (H -> 'u'bb\u0304) + jets  #'
    print '# [4] -',u'tt\u0304Z (Z -> 'u'bb\u0304) + jets  #'
    print '# [5] - Quit                  #'
    print '_______________________________\n'
menu()
while True:
    try:
        x =  int(input('Which sample would you like to use: '))
        a = 'tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root'
        b = 'tthh_ntuple.410246.Sherpa_NNPDF30NNLO_ttbb.root'
        c = 'tthh_ntuple.344436.Sherpa_NNPDF30NNLO_ttH_Htobb.root'
        d = 'tthh_ntuple.410247.Sherpa_NNPDF30NNLO_ttZ_Ztobb.root'
        print '\n'
        if x == 1:
            print 'You selected option:\n\n', a
            f = ROOT.TFile(a)
            sleep(3)
            system('clear')
            break
        elif x == 2:
            print 'You selected option:\n\n', b
            f = ROOT.TFile(b)
            sleep(3)
            system('clear')
            break
        elif x == 3:
            print 'You selected option:\n\n', c
            f = ROOT.TFile(c)
            sleep(3)
            system('clear')
            break
        elif x == 4:
            print 'You selected option:\n\n', d
            f = ROOT.TFile(d)
            sleep(3)
            system('clear')
            break
        elif x == 5:
            system('clear')
            sys.exit('Bye')
        else :
            sleep(1)
            system('clear')
            menu()
            prRed('****************** Invalid option, Enter 1-5 **************\n')
    except NameError:
        sleep(1)
        system('clear')
        menu()
        prRed('*******************Invalid option, Enter 1-5**************\n')
#------------------------------------------------------------------------------#
# Assign OutputTree as MyTree and get number of entries in tree.
MyTree = f.Get('OutputTree')
entries = MyTree.GetEntries()
#------------------------------------------------------------------------------#
# Create Canvas and empty Histograms hx.
h1 = ROOT.TH1D('#eta','#eta;< #eta(b_{i},b_{j}) >;Events normalized to unit area / 0.2',20,0,4)
h2 = ROOT.TH1D('M_{bb}','M_{bb};M_{bb} [GeV];Events normalized to unit area / 25GeV',10,0,250)
h3 = ROOT.TH1D('Centrality','Centrality;Centrality;Events normalised to unit area / 0.1',10,0,1)
h4 = ROOT.TH1D('H_{B}','H_{B};H_{B} [GeV];Events normalised to unit area / 150GeV',10,0,1500)
h5 = ROOT.TH1D('jet','jet;H_{B} [GeV];Events normalised to unit area / 150GeV',13,0,13)
h6 = ROOT.TH1D('btag','btag;sfsfjknkjls',7,0,7)
h0 = ROOT.TH1D('counter','counter;sfsfs',7,0,7)
#------------------------------------------------------------------------------#
# Functions:
# Average separation in pseudorapidity between two b-tagged jets.
def etabi_j(x,y):
    distance = abs(jetvec[tracker_btj[x]].Eta() - jetvec[tracker_btj[y]].Eta())
    return distance
# Vector Pt or M Sum between two b-tagged jets.
def vectorsum(x,y,c):
    if c == 'Pt':
        sum = (jetvec[tracker_btj[x]] + jetvec[tracker_btj[y]]).Pt()
    elif c == 'M':
        sum = (jetvec[tracker_btj[x]] + jetvec[tracker_btj[y]]).M()

    return sum
#------------------------------------------------------------------------------#
# Loop through the entries of MyTree.
for event in MyTree:
    # Variables.
    numlep = event.nlep[0]      # Store number of leptons in each event as num.
    numjet = event.njet[0]      # Store number of jets in each event as num.
    lepvec      = {}            # Initialize empty lepton vector.
    jetvec      = {}            # Initialize empty jet vector.
    tracker_btj = []            # Initialize empty tracking btagjets.
    btjmaxPt    = 0             # Initialize empty b-tag vecto for max .Pt().
    btjmaxM     = 0             # Initialize empty b-tag vecto for max .M().
    vec_sum_Pt  = 0             # Initialize empty b-tag vector for summing Pt().
    vec_sum_M   = 0             # Initialize empty b-tag vector for summing M().
    goodleptons = 0             # Initialize counter for leptons.
    goodjets    = 0             # Initialize counter for jets.
    btagjets    = 0             # Initialize counter for b-tag jets.
    etasum      = 0             # Initialize sum for eta seperation.
    etasum_N    = 0             # Initialize sum for eta separation average.
    cen_sum_Pt  = 0             # Initialize sum of Pt for all jets.
    cen_sum_E   = 0             # Initialize sum of E for all jets.
    HB_sum_Pt   = 0             # Initialize sum of Pt for all b-tag jets.
    h0.Fill(1,1)
#------------------------------Cuts Start--------------------------------------#
# Events must have exactly one electron or one muon (as detailed in 3.1.1).
    for i in xrange(numlep):
        lepvec[i] = ROOT.TLorentzVector() # Cast vectors as Lorentz vectors.
        lepvec[i].SetPtEtaPhiM(event.leppT[i],event.lepeta[i],event.lepphi[i],0)
        if lepvec[i].Pt() < 25000: continue
        # Only selecting leptons > 25GeV.
        if event.lepflav[i] == 11 and abs(event.lepeta[i]) >= 4.0: continue
        # Only selecting electrons with |eta| <= 4.0.
        if event.lepflav[i] == 13 and abs(event.lepeta[i]) >= 2.5: continue
        # Only selecting muons with |eta| <= 2.5.
        goodleptons += 1
    h0.Fill(2,1)
# Events must have >= 7 jets with pT > 30 GeV and eta <= 4.0.
    for i in xrange(numjet):
        jetvec[i] = ROOT.TLorentzVector()    # Cast vectors as Lorentz vectors.
        jetvec[i].SetPtEtaPhiM(event.jetpT[i],event.jeteta[i],event.jetphi[i],0)
        if jetvec[i].Pt() < 30000: continue  # Only selecting jets > 30GeV.
        if abs(event.jeteta[i]) >= 4.0: continue
        # Only selecting jets with |eta| <= 4.0.
        goodjets += 1                        # Count of jets.
        if event.jetbhadron[i] != 1: continue
        tracker_btj.append(i)                # B-tag jets into a list.
    btagjets = len(tracker_btj)              # Count of b-tagged jets.
    h0.Fill(3,1)
    if not (goodleptons == 1 and goodjets >= 7 and btagjets >= 5):continue
    # Passing lepton req. min of 7 jets with at least 5 b-tag jets.
    h0.Fill(4,1)
    h5.Fill(goodjets)
#---------------------------------Cuts-End-------------------------------------#
    for i in xrange(btagjets):
        HB_sum_Pt += jetvec[tracker_btj[i]].Pt()
        # scalar sum of pT for b-tagged jets, HB.
        for j in xrange(btagjets):
            if i == j: continue
            etasum += etabi_j(i,j)      # Finding separation between all b_jets.
            vec_sum_Pt = vectorsum(i,j,'Pt') # Sum of btagjets Pt.
            vec_sum_M  = vectorsum(i,j,'M')  # Sum of btagjets M.
            if vec_sum_Pt < btjmaxPt:continue
            # Finds max Pt and M for two btagjets.
            btjmaxPt = vec_sum_Pt
            btjmaxM  = vec_sum_M
    h2.Fill(btjmaxM/1000)                    # Fill h2 histogram with M_bb.
    if btagjets != 0:
        etasum_N = etasum/(2*btagjets)       # Getting distance avg.
    h1.Fill(etasum_N)                        # Fill h1 w/ btagjets speration avg.
    h4.Fill(HB_sum_Pt/1000)                  # Fill h4 w/ scalar sum of pT.
    if etasum_N < 1.25 :
        h0.Fill(5,1)
        if btagjets >= 6:
            h0.Fill(6,1)

#------------------------------------------------------------------------------#
    for i in xrange(numjet):
        cen_sum_E  += jetvec[i].E()          # Scalar sum of E.
        cen_sum_Pt += jetvec[i].Pt()         # Scalar sum of Pt.
    if cen_sum_E != 0:
        h3.Fill(cen_sum_Pt/cen_sum_E)        # Fill h3 w/ scalar sum of Pt/E.
    h6.Fill(1)
#-----------------------------Histograms Display-------------------------------#
g = ROOT.TFile('all_hist.root','update')
if int(x) == 1:
    ttHH1 = h1.Clone('ttHH1')
    ttHH1.Write()
    ttHH2 = h2.Clone('ttHH2')
    ttHH2.Write()
    ttHH3 = h3.Clone('ttHH3')
    ttHH3.Write()
    ttHH4 = h4.Clone('ttHH4')
    ttHH4.Write()
    ttHH5 = h5.Clone('ttHH5')
    ttHH5.Write()
    ttHH6 = h6.Clone('ttHH6')
    ttHH6.Write()
    ttHH0 = h0.Clone('ttHH0')
    ttHH0.Write()
elif int(x) == 2:
    ttbb1 = h1.Clone('ttbb1')
    ttbb1.Write()
    ttbb2 = h2.Clone('ttbb2')
    ttbb2.Write()
    ttbb3 = h3.Clone('ttbb3')
    ttbb3.Write()
    ttbb4 = h4.Clone('ttbb4')
    ttbb4.Write()
    ttbb5 = h5.Clone('ttbb5')
    ttbb5.Write()
    ttbb6 = h6.Clone('ttbb6')
    ttbb6.Write()
    ttbb0 = h0.Clone('ttbb0')
    ttbb0.Write()
elif int(x) == 3:
    ttH1 = h1.Clone('ttH1')
    ttH1.Write()
    ttH2 = h2.Clone('ttH2')
    ttH2.Write()
    ttH3 = h3.Clone('ttH3')
    ttH3.Write()
    ttH4 = h4.Clone('ttH4')
    ttH4.Write()
    ttH5 = h5.Clone('ttH5')
    ttH5.Write()
    ttH6 = h6.Clone('ttH6')
    ttH6.Write()
    ttH0 = h0.Clone('ttH0')
    ttH0.Write()
elif int(x) == 4:
    ttZ1 = h1.Clone('ttZ1')
    ttZ1.Write()
    ttZ2 = h2.Clone('ttZ2')
    ttZ2.Write()
    ttZ3 = h3.Clone('ttZ3')
    ttZ3.Write()
    ttZ4 = h4.Clone('ttZ4')
    ttZ4.Write()
    ttZ5 = h5.Clone('ttZ5')
    ttZ5.Write()
    ttZ6 = h6.Clone('ttZ6')
    ttZ6.Write()
    ttZ0 = h0.Clone('ttZ0')
    ttZ0.Write()
print 'done'
