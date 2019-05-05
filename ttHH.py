# Written By : Jonathan O. Tellechea
# Research   : ttHH
# Description: Histogram of number of jets > 30GeV.
################################################################################
################################################################################
from ROOT import TCanvas,TH1F
import ROOT
################################################################################
# Assign *.root file as f.
f = ROOT.TFile("tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root")
################################################################################
# Assign OutputTree as MyTree and get number of entries in tree.
MyTree = f.Get("OutputTree")
entries = MyTree.GetEntries()
################################################################################
# Create empty Histogram h.x
h1 = ROOT.TH1D("njet","njet",10,0,20)
################################################################################
# Loop through the entries of MyTree. Fill histogram with transverse momentum.
################################################################################
for event in MyTree:
    num = event.njet[0]     # Store number of jets in each event as num.
    jetvec = {}             # Initialize empty jet vector.
    ngoodjets = 0           # Initialize variable for jets of interest.
    for i in xrange(num):
        jetvec[i] = ROOT.TLorentzVector()   # Cast vectors as Lorentz vectors.
        jetvec[i].SetPtEtaPhiM(event.jetpT[i],event.jeteta[i],event.jetphi[i],0)
        if jetvec[i].Pt() > 30000: # Only selecting jets > 30GeV.
            ngoodjets += 1
    # Fill Lorentz vector with pt , eta , and phi values.
    h1.Fill(ngoodjets)

h1.Draw()   # Draws Histogram.
