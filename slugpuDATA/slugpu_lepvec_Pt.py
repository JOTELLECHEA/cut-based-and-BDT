# Written By : Jonathan O. Tellechea
# Adviser    : Mike Hance, Phd
# Research   : ttHH
# Description: Histogram of ttHH from pg.8 in http://cdsweb.cern.ch/record/2220969/files/ATL-PHYS-PUB-2016-023.pdf
#------------------------------------------------------------------------------#
import ROOT,sys
import numpy as np
import random,os
from os import system
from time import sleep
import time
from tabulate import tabulate
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
#------------------------------------------------------------------------------#

import argparse

parser = argparse.ArgumentParser(description= 'Cut base analysis for ttHH and background')
parser.add_argument("--x", default=5, type=int, help= "Use '--x=' followed by a number from here:  1:ttHH 2:ttbb 3:ttH 4:ttZ ")

args = parser.parse_args()
x = int(args.x)
a = 'new_TTHH.root'
b = 'new_TTBB.root'
c = 'new_TTH.root'
d = 'new_TTZ.root'

while True:
    try:
        if x == 1:
            print 'You selected option:', 'ttHH'
            f = ROOT.TFile(a)
            break
        elif x == 2:
            print 'You selected option:', 'ttbb'
            f = ROOT.TFile(b)
            break
        elif x == 3:
            print 'You selected option:', 'ttH'
            f = ROOT.TFile(c)
            break
        elif x == 4:
            print 'You selected option:', 'ttZ'
            f = ROOT.TFile(d)
            break
        elif x == 5:
            system('clear')
            sys.exit('Need to pass a variable, use --help for options')
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
h0  = ROOT.TH1D('counter','counter',7,0,7)
h1  = ROOT.TH1D('#eta','#eta;< #eta(b_{i},b_{j}) >;Events normalized to unit area / 0.2',20,0,4)
h2  = ROOT.TH1D('M_{bb}','M_{bb};M_{bb} [GeV];Events normalized to unit area / 25GeV',10,0,250)
h3  = ROOT.TH1D('Centrality','Centrality;Centrality;Events normalised to unit area / 0.1',10,0,1)
h4  = ROOT.TH1D('H_{B}','H_{B};H_{B} [GeV];Events normalised to unit area / 150GeV',10,0,1500)
h5  = ROOT.TH1D('jet','jet;Jet muliplicity;Events normalised to unit area',13,0,13)
h6  = ROOT.TH1D('btag','btag;N b-tagged jets;Events normalised to unit area',10,-.5,9.5)
h7  = ROOT.TH1D('met','met;Transverse mass (GeV);Events',100,0,300)
h8  = ROOT.TH1D('pT of top 2 btag','pT of top 2 btag;invariant mass of two highest btag pT (GeV);Events',100,0,525)
h9  = ROOT.TH1D('#DeltaR','#DeltaR;#DeltaR ;Events',100,-.5,9.5)
h10 = ROOT.TH1D('Lowest #DeltaR','Lowest #DeltaR;h10;Events',100,-.5,9.5)
h11 = ROOT.TH1D('remaining pT','remaining pT;remaining pT;Events',100,0,250)
h12 = ROOT.TH1D('h12','h12;lowest btagjet pT;Events',100,0,180)
h13 = ROOT.TH1D('h13','h13;2nd lowest btagjet pT;Events',100,0,180)
h14 = ROOT.TH1D('h14','h14;Lowest pT of charm jet;Events',100,0,1000)
h15 = ROOT.TH1D('h15','h15;2nd Lowest pT of charm jet;Events',100,0,1000)
h16 = ROOT.TH1D('h16','h16;Chisquare;Events',1000000,0,1.0e+13)
h17 = ROOT.TH1D('h17','h17;btag pt;Events',100,0,1.0e+7)
# #------------------------------------------------------------------------------#
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
    w      = event.mcweight[0]  # Histogram weights.
    numlep = event.nlep[0]      # Store number of leptons in each event as num.
    numjet = event.njet[0]      # Store number of jets in each event as num.
    lepvec      = {}            # Initialize empty lepton vector.
    jetvec      = {}            # Initialize empty jet vector.
    neutrino    = {}
    tracker_btj = []            # Initialize empty tracking btagjets.
    tracker_non = []            # Initialize empty tracking lightjets.
    jetprime    = []            # Initialize empty tracking ctagjets.
    btjmaxPt    = 0.            # Initialize empty b-tag vecto for max .Pt().
    btjmaxM     = 0.            # Initialize empty b-tag vecto for max .M().
    vec_sum_Pt  = 0.            # Initialize empty b-tag vector for summing Pt().
    vec_sum_M   = 0.            # Initialize empty b-tag vector for summing M().
    goodleptons = 0             # Initialize counter for leptons.
    goodjets    = 0             # Initialize counter for jets.
    btagjets    = 0             # Initialize counter for b-tag jets.
    ntagjets    = 0             # Initialize counter for non b-tag jets.
    etasum      = 0.            # Initialize sum for eta seperation.
    etasum_N    = 0.            # Initialize sum for eta separation average.
    cen_sum_Pt  = 0.            # Initialize sum of Pt for all jets.
    cen_sum_E   = 0.            # Initialize sum of E for all jets.
    HB_sum_Pt   = 0.            # Initialize sum of Pt for all b-tag jets.
    rand        = 0.            # Initialize random variable with value (0,1).
    onelep      = False
    mt          = 0.
    pT1         = 0.
    pT2         = 0.
    pTmax       = 0.
    cone_l_Pt   = 0.
    cone_j_Pt   = 0.
    m1          = 0.
    m2          = 0.
    mv          = 0.
    chi         = 0.
    l1          = []
    l2          = []
    l3          = []
    dR          = []
    chisq       = []
    # h0.Fill(0,w)
    h0.Fill(0)
#------------------------------Cuts Start--------------------------------------#
# Events must have exactly one electron or one muon (as detailed in 3.1.1).
    neutrino[0] = ROOT.TLorentzVector()
    neutrino[0].SetPtEtaPhiM(event.met[0],0,event.met_phi[0],0)
    for i in xrange(numlep):
        rand = random.random()
        lepvec[i] = ROOT.TLorentzVector() # Cast vectors as Lorentz vectors.
        lepvec[i].SetPtEtaPhiM(event.leppT[i],event.lepeta[i],event.lepphi[i],0)
        mt = ROOT.TMath.Sqrt(2 * event.met[0] * lepvec[i].Pt()/(10**6) * ( 1 - ROOT.TMath.Cos((lepvec[i].DeltaPhi(neutrino[0])))))
        h7.Fill(mt,w)
        if event.lepflav[i] == 11 and abs(event.lepeta[i]) < 2.5 and (22000 < event.leppT[i] < 35000) and rand <= .95:
            goodleptons += 1
        elif event.lepflav[i] == 11 and abs(event.lepeta[i]) < 2.5 and event.leppT[i] > 35000 and rand <= 1.00:
            goodleptons += 1
        elif event.lepflav[i] == 11 and (2.5 < abs(event.lepeta[i]) < 4.9) and event.leppT[i] > 35000 and rand <= 0.90:
            goodleptons += 1
        elif event.lepflav[i] == 13 and abs(event.lepeta[i]) < 2.4 and event.leppT[i] > 20000 and rand <= 0.96:
            goodleptons +=1
        if event.leppT[i] <= 25000: continue
        # Only selecting leptons > 25GeV.
        if abs(event.lepflav[i]) == 11 and abs(event.lepeta[i]) <= 4.0:
            onelep = True
        # Only selecting electrons with |eta| <= 4.0.
        elif abs(event.lepflav[i]) == 13 and abs(event.lepeta[i]) <= 2.5:
        # Only selecting muons with |eta| <= 2.5.
            onelep = True
    if onelep == False: continue #Trigger cut#
    # h0.Fill(1,w)
    h0.Fill(1)
    h5.Fill(numjet,w)
# Events must have >= 7 jets with pT > 30 GeV and eta <= 4.0.
    for i in xrange(numjet):
        jetprime.append(i) 
        jetvec[i] = ROOT.TLorentzVector()    # Cast vectors as Lorentz vectors.
        jetvec[i].SetPtEtaPhiM(event.jetpT[i],event.jeteta[i],event.jetphi[i],0)
        if jetvec[i].Pt() <= 30000: continue  # Only selecting jets > 30GeV.
        if abs(event.jeteta[i]) > 4.0: continue
        # Only selecting jets with |eta| <= 4.0.
        goodjets += 1                                           # Count of jets.
        rand = 0.0
        rand = random.random()
        if event.jetbhadron[i] == 1 and rand <= 0.7:
            tracker_btj.append(i)              # B-tag jets into a list.
        elif event.jetchadron[i] == 1 and rand <= 0.2:
            tracker_btj.append(i)
        elif rand <= 0.002:
            tracker_btj.append(i)
        else:
            tracker_non.append(i)
    btagjets = len(tracker_btj)
    ntagjets = len(tracker_non)
    for i in xrange(btagjets):
        jetprime.remove(tracker_btj[i])
    for i in xrange(ntagjets):
        jetprime.remove(tracker_non[i])
    ctagjets = len(jetprime)
    if not goodleptons == 1:continue
    # h0.Fill(2,w)
    h0.Fill(2)
    if not goodjets  >= 7 :continue
    h0.Fill(3)
    # h0.Fill(3,w)
    h6.Fill(btagjets,w)
    # if 5 <= btagjets < 6:
    if not btagjets >= 5: continue
    h0.Fill(4)
    # h0.Fill(4,w)
    # if not btagjets >= 6:continue
    for i in xrange(btagjets):
        h17.Fill(jetvec[tracker_btj[i]].Pt())
        l1.append(jetvec[tracker_btj[i]].Pt())
        l2.append(jetvec[tracker_btj[i]].Pt())
    m1 = l2.index(l1.pop(l1.index(max(l1))))
    m2 = l2.index(max(l1))
    h8.Fill((jetvec[tracker_btj[m1]]+jetvec[tracker_btj[m2]]).M()/1000,w)
    h12.Fill(l2.pop(l2.index(min(l2)))/1000,w)
    h13.Fill(min(l2)/1000,w)
    for i in xrange(ctagjets):
        l3.append(jetvec[jetprime[i]].Pt())
    if ctagjets > 0:
        h14.Fill(l3.pop(l3.index(min(l3)))/1000,w)
    if len(l3) > 0:
        h15.Fill(min(l3)/1000,w)
    for i in xrange(len(l1)):
        h11.Fill(l1[i]/1000,w)
    for i in xrange(btagjets):
        HB_sum_Pt += jetvec[tracker_btj[i]].Pt()
        # scalar sum of pT for b-tagged jets, HB.
        for j in xrange(btagjets):
            if i == j: continue
            etasum += etabi_j(i,j)           # Finding separation between all b_jets.
            vec_sum_Pt = vectorsum(i,j,'Pt') # Sum of btagjets Pt.
            vec_sum_M  = vectorsum(i,j,'M')  # Sum of btagjets M.
            if vec_sum_Pt < btjmaxPt:continue
            # Finds max Pt and M for two btagjets.
            btjmaxPt = vec_sum_Pt
            btjmaxM  = vec_sum_M
    h2.Fill(btjmaxM/1000,w)                    # Fill h2 histogram with M_bb.
    if btagjets > 1:
        etasum_N = etasum/(btagjets**2 - btagjets)  # Getting distance avg.
    h1.Fill(etasum_N,w)                        # Fill h1 w/ btagjets speration avg.
    h4.Fill(HB_sum_Pt/1000,w)                  # Fill h4 w/ scalar sum of pT.
    if not etasum_N < 1.25: continue
    # h0.Fill(5,w)
    h0.Fill(5)
    if btagjets >= 6:
        # h0.Fill(6,w)
        h0.Fill(6)
#------------------------------------------------------------------------------#
    for i in xrange(numjet):
        cen_sum_E  += jetvec[i].E()          # Scalar sum of E.
        cen_sum_Pt += jetvec[i].Pt()         # Scalar sum of Pt.
        for j in xrange(numlep):
            dR.append(lepvec[j].DeltaR(jetvec[i]))
            h9.Fill(lepvec[j].DeltaR(jetvec[i]),w)
            h10.Fill(min(dR),w)
    if cen_sum_E != 0:
        h3.Fill(cen_sum_Pt/cen_sum_E,w)      # Fill h3 w/ scalar sum of Pt/E.
    if btagjets >= 6:        
        for i in xrange(0,6):
            for j in xrange(1,6):
                for k in xrange(2,6):
                    for l in xrange(3,6):
                        if i == j == k == l :continue
                        if i > j > k > l :continue
                        if j > k > l :continue
                        if k > l :continue
                        if i > j :continue
                        if j > k  :continue
                        if i == j == k :continue
                        if i == j :continue
                        if i == k :continue
                        if i == l :continue
                        if j == k == l:continue
                        if j == k :continue
                        if j == l :continue
                        if k == l :continue
                        chisq.append((vectorsum(i,j,'M') - 120000)**2 + (vectorsum(k,l,'M') - 120000)**2)
    if len(chisq) > 0:
        chi = min(chisq)
        h16.Fill(chi/1000,w)
#------------Histograms Display-------------------------------#
g = ROOT.TFile('mark1.root','update')
if int(x) == 1:
    ttHH0 = h0.Clone('ttHH0')
    # ttHH0.Scale(990/(930000/0.609))
    ttHH0.Write()
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
    ttHH7 = h7.Clone('ttHH7')
    ttHH7.Write()
    ttHH8 = h8.Clone('ttHH8')
    ttHH8.Write()
    ttHH9 = h9.Clone('ttHH9')
    ttHH9.Write()
    ttHH10 = h10.Clone('ttHH10')
    ttHH10.Write()
    ttHH11 = h11.Clone('ttHH11')
    ttHH11.Write()
    ttHH12 = h12.Clone('ttHH12')
    ttHH12.Write()
    ttHH13 = h13.Clone('ttHH13')
    ttHH13.Write()
    ttHH14 = h14.Clone('ttHH14')
    ttHH14.Write()
    ttHH15 = h15.Clone('ttHH15')
    ttHH15.Write()
    ttHH16 = h16.Clone('ttHH16')
    ttHH16.Write()
    ttHH17 = h17.Clone('ttHH17')
    ttHH17.Write()
elif int(x) == 2:
    ttbb0 = h0.Clone('ttbb0')
    # ttbb0.Scale((3332932/5900000.)*5850000/ttbb0.GetBinContent(1))
    # ttbb0.Scale(5850000/5900000.)
    ttbb0.Write()
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
    ttbb7 = h7.Clone('ttbb7')
    ttbb7.Write()
    ttbb8 = h8.Clone('ttbb8')
    ttbb8.Write()
    ttbb9 = h9.Clone('ttbb9')
    ttbb9.Write()
    ttbb10 = h10.Clone('ttbb10')
    ttbb10.Write()
    ttbb11 = h11.Clone('ttbb11')
    ttbb11.Write()
    ttbb12 = h12.Clone('ttbb12')
    ttbb12.Write()
    ttbb13 = h13.Clone('ttbb13')
    ttbb13.Write()
    ttbb14 = h14.Clone('ttbb14')
    ttbb14.Write()
    ttbb15 = h15.Clone('ttbb15')
    ttbb15.Write()
    ttbb16 = h16.Clone('ttbb16')
    ttbb16.Write()
    ttbb17 = h17.Clone('ttbb17')
    ttbb17.Write()
elif int(x) == 3:
    ttH0 = h0.Clone('ttH0')
    # ttH0.Scale((320752/610000.)*612000/ttH0.GetBinContent(1))
    # ttH0.Scale(612000/610000.)
    ttH0.Write()
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
    ttH7 = h7.Clone('ttH7')
    ttH7.Write()
    ttH8 = h8.Clone('ttH8')
    ttH8.Write()
    ttH9 = h9.Clone('ttH9')
    ttH9.Write()
    ttH10 = h10.Clone('ttH10')
    ttH10.Write()
    ttH11 = h11.Clone('ttH11')
    ttH11.Write()
    ttH12 = h12.Clone('ttH12')
    ttH12.Write()
    ttH13 = h13.Clone('ttH13')
    ttH13.Write()
    ttH14 = h14.Clone('ttH14')
    ttH14.Write()
    ttH15 = h15.Clone('ttH15')
    ttH15.Write()
    ttH16 = h16.Clone('ttH16')
    ttH16.Write()
    ttH17 = h17.Clone('ttH17')
    ttH17.Write()
elif int(x) == 4:
    ttZ0 = h0.Clone('ttZ0')
    # ttZ0.Scale((158645/270000.)*269000/ttZ0.GetBinContent(1))
    # ttZ0.Scale((269000/270000.))
    ttZ0.Write()
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
    ttZ7 = h7.Clone('ttZ7')
    ttZ7.Write()
    ttZ8 = h8.Clone('ttZ8')
    ttZ8.Write()
    ttZ9 = h9.Clone('ttZ9')
    ttZ9.Write()
    ttZ10 = h10.Clone('ttZ10')
    ttZ10.Write()
    ttZ11 = h11.Clone('ttZ11')
    ttZ11.Write()
    ttZ12 = h12.Clone('ttZ12')
    ttZ12.Write()
    ttZ13 = h13.Clone('ttZ13')
    ttZ13.Write()
    ttZ14 = h14.Clone('ttZ14')
    ttZ14.Write()
    ttZ15 = h15.Clone('ttZ15')
    ttZ15.Write()
    ttZ16 = h16.Clone('ttZ16')
    ttZ16.Write()
    ttZ17 = h17.Clone('ttZ17')
    ttZ17.Write()
prRed('****************** Finished **************\n')
print 'Finished @:', time.asctime()
