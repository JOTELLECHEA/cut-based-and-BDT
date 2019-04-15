#Program that outputs a histogram of the muon invariant mass
from ROOT import TCanvas,TH1F
import ROOT
#opens the root file
f = ROOT.TFile("delphes.Bj-4p-0-500_100TEV.NoPileUp.root")
#loads TTree into the memory
MyTree = f.Get("OutputTree")
#create a empty histogram
h = ROOT.TH1D("mass","mass;#mu^{+}#mu^{-} Invariant Mass[GeV];Events/Bin",200,0,200)
#loop through the entries of the leaf and fill the histogram with data
#then draw histogram
#declared variable of number of events from pTLep
entries = MyTree.GetEntries()
#declare variables
#int flavLep
for event in MyTree:
   lepvec = {}
   lepvec[0] = ROOT.TLorentzVector()
   lepvec[1] = ROOT.TLorentzVector()
   lepvec[2] = ROOT.TLorentzVector()
   if event.flavLep[0]*event.flavLep[1]== -4:
       lepvec[0].SetPtEtaPhiM(event.pTLep[0],event.etaLep[0],event.phiLep[0],0.105)
       lepvec[1].SetPtEtaPhiM(event.pTLep[1],event.etaLep[1],event.phiLep[1],0.105)
       h.Fill((lepvec[0]+lepvec[1]).M())


h.Draw()
