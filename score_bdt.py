import ROOT

sigfile = ROOT.TFile("new_signal_tthh.root","RO")
sigtree = sigfile.Get("OutputTree")

bakfile = ROOT.TFile("new_background_ttbb.root","RO")
baktree = bakfile.Get("OutputTree")

bdtfile = ROOT.TFile("BDToutput_test_phase2.root", "RO")
bdttree = bdtfile.Get("phase2")
nbins = 30
# histograms to store our information
h1 = ROOT.TH1F("Signal","",nbins,0,13)
h2 = ROOT.TH1F("BG","",nbins,0,13)
c1 = ROOT.TCanvas('c1','Canvas 1',710,100,1000,500)
c1.Divide(2,1,0.01,0.01,0)
leg = ROOT.TLegend(0.69,0.69,0.89,0.89)
leg.SetLineColor(ROOT.kWhite)
leg.AddEntry(h1,'Signal')
leg.AddEntry(h2,'Background')

# create a single chain that has trees in the same order as the training data
chain = ROOT.TChain("OutputTree")
chain.Add("new_signal_tthh.root")
chain.Add("new_background_ttbb.root")

# this is the key line, where we associate the BDT output to the inputs.
chain.AddFriend(bdttree)

nsignalevents = sigtree.GetEntriesFast()
nevents = 0

bdt_threshold = 0.1
for event in chain:
     # access the BDT score like this
     if chain.y > bdt_threshold:
         # keep track of how many events we've processed, so we know whether this is a signal or background event
         if nevents < nsignalevents:
             h1.Fill(event.njet[0],event.mcweight[0])
         # else:
             h2.Fill(event.njet[0],event.mcweight[0])
     nevents+=1


c1.cd(1)##################################### Seperation between two b-tag jets.
h1.SetLineColor(ROOT.kRed)
h1.SetStats(0)
h1.Scale(1/(h1.Integral()))
h1.Draw('HIST SAME')
h2.SetLineColor(ROOT.kBlue)
h2.SetStats(0)
h2.Scale(1/(h2.Integral()))
h2.Draw('HIST SAME')
leg.Draw()