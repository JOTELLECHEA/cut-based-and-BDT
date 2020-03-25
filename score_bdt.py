import ROOT

def hplot(hist,color,style):
    hist.SetLineColor(color)
    hist.SetLineStyle(style)
    hist.SetStats(0)
    hist.Draw('HIST SAME')


sigfile = ROOT.TFile("new_signal_tthh.root","RO")
sigtree = sigfile.Get("OutputTree")

bakfile = ROOT.TFile("new_background_ttbb.root","RO")
baktree = bakfile.Get("OutputTree")

bdtfile = ROOT.TFile("BDToutput_test_phase2.root", "RO")
bdttree = bdtfile.Get("phase2")
nbins = 30
# histograms to store our information
h01 = ROOT.TH1D('N Jets','N Jets;',30,0,30)#Signal
h02 = ROOT.TH1D('H2','H2;',30,0,30)#SIG w/BDT > 0.0
h03 = ROOT.TH1D('H3','H3;',30,0,30)#BG
h04 = ROOT.TH1D('H4','H4;',30,0,30)#BG w/BDT > 0.0
h11 = ROOT.TH1D('btag','btag;',9,0,9)#Signal
h12 = ROOT.TH1D('G2','G2;',9,0,9)#SIG w/BDT > 0.0
h13 = ROOT.TH1D('G3','G3;',9,0,9)#BG
h14 = ROOT.TH1D('G4','G4;',9,0,9)#BG w/BDT > 0.0
h21 = ROOT.TH1D('Srap','Srap;',60,0,10)#Signal
h22 = ROOT.TH1D('F2','F2;',60,0,10)#SIG w/BDT > 0.0
h23 = ROOT.TH1D('F3','F3;',60,0,10)#BG
h24 = ROOT.TH1D('F4','F4;',60,0,10)#BG w/BDT > 0.0
h31 = ROOT.TH2D('2D N Jets','2D N Jets;Amount of jets;bdt score',30,0,30,10,-1,1)
h32 = ROOT.TH2D('2D B Tags','2D B Tags;Amount of btag jets;bdt score', 9,0, 9,10,-1,1)
h33 = ROOT.TH2D('2D Srap','2D Srap;pseudorapidity;bdt score',60,0,10,10,-1,1)

c1 = ROOT.TCanvas('c1','Canvas 1',710,100,1000,500)
c1.Divide(3,2,0.01,0.01,0)
leg = ROOT.TLegend(0.69,0.69,0.89,0.89)
leg.SetLineColor(ROOT.kWhite)
leg.AddEntry(h01,'SIG,ALL')
leg.AddEntry(h02,'SIG,BDT')
leg.AddEntry(h03,'BG,ALL')
leg.AddEntry(h04,'BG,BDT')

# create a single chain that has trees in the same order as the training data
chain = ROOT.TChain("OutputTree")
chain.Add("new_signal_tthh.root")
chain.Add("new_background_ttbb.root")

# this is the key line, where we associate the BDT output to the inputs.
chain.AddFriend(bdttree)

nsignalevents = sigtree.GetEntriesFast()
nevents = 0
numbers = 0

bdt_threshold = 0.0
# print nsignalevents
for event in chain:
    # print numbers
    # if 1.5572 < event.srap < 1.5573:
    #     print 'here'
    # numbers += 1
    if nevents<nsignalevents:
        h01.Fill(event.njet[0],event.mcweight[0])# SIG ALL
        h31.Fill(event.njet[0],chain.y,event.mcweight[0])
        h11.Fill(event.btag,event.mcweight[0])# SIG ALL
        h32.Fill(event.btag,chain.y,event.mcweight[0])
        h21.Fill(event.srap,event.mcweight[0])# SIG ALL
        h33.Fill(event.srap,chain.y,event.mcweight[0])
        if chain.y > bdt_threshold:
            h02.Fill(event.njet[0],event.mcweight[0])# Sig,BDT > 0.0
            h12.Fill(event.btag,event.mcweight[0])# Sig,BDT > 0.0
            h22.Fill(event.srap,event.mcweight[0])# Sig,BDT > 0.0
    else:
        h03.Fill(event.njet[0],event.mcweight[0])# BG,ALL
        h13.Fill(event.btag,event.mcweight[0])# BG,ALL
        h23.Fill(event.srap,event.mcweight[0])# BG,ALL
        if chain.y > bdt_threshold:
            h04.Fill(event.njet[0],event.mcweight[0])#BG,BDT > 0.0
            h14.Fill(event.btag,event.mcweight[0])#BG,BDT > 0.0
            h24.Fill(event.srap,event.mcweight[0])#BG,BDT > 0.0
    nevents+=1


c1.cd(1).SetLogy()##################################### n-jets.
h01.SetMaximum(10e6)
hplot(h01,ROOT.kRed,1)
hplot(h02,ROOT.kRed,2)
hplot(h03,ROOT.kBlue,1)
hplot(h04,ROOT.kBlue,2)
leg.Draw()
c1.cd(2).SetLogy()##################################### b tag.
h11.SetMaximum(10e6)
hplot(h11,ROOT.kRed,1)
hplot(h12,ROOT.kRed,2)
hplot(h13,ROOT.kBlue,1)
hplot(h14,ROOT.kBlue,2)
leg.Draw()
c1.cd(3).SetLogy()##################################### Srap.
h21.SetMaximum(10e6)
hplot(h21,ROOT.kRed,1)
hplot(h22,ROOT.kRed,2)
hplot(h23,ROOT.kBlue,1)
hplot(h24,ROOT.kBlue,2)
leg.Draw()
c1.cd(4)
h31.SetLineColor(ROOT.kRed)
h31.SetLineStyle(1)
h31.SetStats(0)
h31.Draw('HIST')
c1.cd(5)
h32.SetLineColor(ROOT.kRed)
h32.SetLineStyle(1)
h32.SetStats(0)
h32.Draw('HIST')
c1.cd(6)
h33.SetLineColor(ROOT.kRed)
h33.SetLineStyle(1)
h33.SetStats(0)
h33.Draw('HIST')