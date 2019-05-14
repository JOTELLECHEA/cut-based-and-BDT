# Written By : Jonathan O. Tellechea
# Research   : ttHH
# Description: Histogram of leptons transverse momentum.
#------------------------------------------------------------------------------#
from ROOT import TCanvas,TH1F
import ROOT
import time
#------------------------------------------------------------------------------#
# Assign *.root file as f.
f = ROOT.TFile("tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root")
#------------------------------------------------------------------------------#
# Assign OutputTree as MyTree and get number of entries in tree.
MyTree = f.Get("OutputTree")
entries = MyTree.GetEntries()
#------------------------------------------------------------------------------#
# Create empty Histogram h.
h1 = ROOT.TH1D("pt","pt;leptons transverse momentum;Events/Bin",600,0,600)
h2 = ROOT.TH1D("eta","eta;eta seperation;Events/Bin",600,0,600)
#------------------------------------------------------------------------------#
#Functions:average separation in pseudorapidity between two b-tagged jets
def etabi_j(x,y):
    distance = abs(jetvec[x].Eta()-jetvec[y].Eta())
    return distance
#------------------------------------------------------------------------------#
# Loop through the entries of MyTree.
start_time = time.time()        # Timer starts.
elist = []                      # Initialize empty event list.
for event in MyTree:
    numlep = event.nlep[0]      # Store number of leptons in each event as num.
    numjet = event.njet[0]      # Store number of jets in each event as num.
    lepvec = {}                 # Initialize empty lepton vector.
    jetvec = {}                 # Initialize empty jet vector.
    goodleptons = 0             # Initialize counter for leptons.
    goodjets = 0                # Initialize counter for jets.
    btagjets = 0                # Initialize counter for b-tag jets.
    etasum   = 0                # Initialize sum for eta seperation.
#------------------------------Cuts Start--------------------------------------#
#Events must have exactly one electron or one muon (as detailed in 3.1.1).

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
#------------------------------------------------------------------------------#
# Events must have >= 7 jets with pT > 30 GeV and eta <= 4.0.
    y =0
    for i in xrange(numjet):
        jetvec[i] = ROOT.TLorentzVector()   # Cast vectors as Lorentz vectors.
        jetvec[i].SetPtEtaPhiM(event.jetpT[i],event.jeteta[i],event.jetphi[i],0)
        if jetvec[i].Pt() < 30000: continue # Only selecting jets > 30GeV.
        if abs(event.jeteta[i]) >= 4.0: continue
        # Only selecting jets with |eta| <= 4.0.
        goodjets += 1
        # Count of jets.
        if event.jetbhadron[i] != 1: continue
        btagjets += 1
        # Count of b-tag jets.
        
        for j in xrange(numjet):
            if i == j: continue
            etasum += etabi_j(i,j)
    y = etasum/(2*numjet)
    h2.Fill(y)

#------------------------------Cuts End----------------------------------------#
    if goodleptons == 1 and goodjets >= 7 and btagjets >= 5:
    # Passing lepton req. min of 7 jets with at least 5 b-tag jets.
        elist.append(event.evtno[0])
        # Fill histogram with event number.
#---------------------------Time tracking for loop_----------------------------#
end_time = time.time()                       # Timer stops.
loop_time = '%.3f'%( end_time - start_time)  # Total time.
print 'Loop Runtime:',loop_time,'seconds'
#------------------------------------------------------------------------------#
print(len(elist))
h2.Draw()
