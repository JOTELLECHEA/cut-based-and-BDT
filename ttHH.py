#Program that outputs a histogram of the muon invariant mass
from ROOT import TCanvas,TH1F
import ROOT
#opens the root file
f = ROOT.TFile("tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root")
#loads TTree into the memory
MyTree = f.Get("OutputTree")
#create a empty histogram
h = ROOT.TH1D("mass","mass;#mu^{+}#mu^{-} Invariant Mass[GeV];Events/Bin",250,0,250)
#loop through the entries of the leaf and fill the histogram with data
#then draw histogram
#declared variable of number of events from pTLep
entries = MyTree.GetEntries()
#declare variables
#int flavLep
for event in MyTree:
    num = event.njet
    lepvec = {}
    for i in num:
        lepvec[i] = ROOT.TLorentzVector()
        if event.nlep == 1 :
           lepvec[i].SetPtEtaPhiE(event.jetpT[i],event.jeteta[i],event.jetphi[i],126)
           h.Fill((lepvec[0]+lepvec[1]).E())





h.Draw()
