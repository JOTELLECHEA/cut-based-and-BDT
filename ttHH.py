#Program that outputs a histogram of the muon invariant mass
from ROOT import TCanvas,TH1F
import ROOT
#opens the root file
f = ROOT.TFile("tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root")
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
       lepvec[0].SetPtEtaPhiM(event.jetpT[0],event.jeteta[0],event.jetpphi[0],126)
       lepvec[1].SetPtEtaPhiM(event.jetpT[1],event.jeteta[1],event.jetpphi[1],126)
       h.Fill((lepvec[0]+lepvec[1]).M())


h.Draw()
