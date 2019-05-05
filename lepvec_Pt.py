# Written By : Jonathan O. Tellechea
# Research   : ttHH
# Description: Histogram of leptons transverse momentum.
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
# Create empty Histogram h.
h1 = ROOT.TH1D("pt","pt;leptons transverse momentum;Events/Bin",250,0,250)
################################################################################
# Loop through the entries of MyTree. Fill histogram with transverse momentum.
################################################################################
for event in MyTree:
    num = event.nlep[0]   # Store number of leptons in each event as num.
    lepvec = {}           # Initialize empty lepton vector.
    for i in xrange(num):
        lepvec[i] = ROOT.TLorentzVector() # Cast vectors as Lorentz vectors.
        lepvec[i].SetPtEtaPhiM(event.leppT[i],event.lepeta[i],event.lepphi[i],0)
        # Fill Lorentz vector with pt , eta , and phi values.
        h1.Fill(lepvec[i].Pt()/1000.)

h1.Draw()   # Draws Histogram.
h1.SaveAs("lepvec_Pt-Histogram.pdf") # Saves Histogram as *.pdf.
