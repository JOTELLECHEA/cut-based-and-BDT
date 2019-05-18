# Written By : Jonathan O. Tellechea
# Research   : ttHH
# Description: Histogram of ttHH from pg.8 in http://cdsweb.cern.ch/record/2220969/files/ATL-PHYS-PUB-2016-023.pdf
#------------------------------------------------------------------------------#
import ROOT
import time
#------------------------------------------------------------------------------#
# Assign *.root file as f.
f = ROOT.TFile('tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root')
#------------------------------------------------------------------------------#
# Assign OutputTree as MyTree and get number of entries in tree.
MyTree = f.Get('OutputTree')
entries = MyTree.GetEntries()
#------------------------------------------------------------------------------#
# Create Canvas and empty Histograms hx.
c1 = ROOT.TCanvas('c1','bin Size',500,600,1000,800)
c1.Divide(2,2)
h1 = ROOT.TH1D('eta','eta;< #eta(b_{i},b_{j}) >;Events normalized to unit area / 0.2',20,0,4)
h2 = ROOT.TH1D('pt','pt;M_{bb} [GeV];Events normalized to unit area / 25GeV',250,0,250)
h3 = ROOT.TH1D('blah','blah;Centrality;Events normalised to unit area / 0.1',10,0,1)
h4 = ROOT.TH1D('blahh','blahh;H_{B} [GeV];Events normalised to unit area / 150GeV',1400,0,1400)

#------------------------------------------------------------------------------#
#Functions:average separation in pseudorapidity between two b-tagged jets
def etabi_j(x,y):
    distance = abs(x.Eta() - y.Eta())
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
        for j in xrange(len(jetvec)):
            if i == j: continue
            etasum += etabi_j(jetvec[i],jetvec[j])
    y = etasum/(2*numjet)
    h1.Fill(y)


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
c1.cd(1)
h1.Scale(2/(h1.Integral()))
h1.Draw('HIST')
c1.cd(2)
h2.Draw()
c1.cd(3)
h3.Draw()
c1.cd(4)
h4.Draw()
c1.Update()
