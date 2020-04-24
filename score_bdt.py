import ROOT
import argparse

parser = argparse.ArgumentParser(description= 'Variable plots with signal/background/bdt score and 2d plots.')
parser.add_argument("--branch", default='wrong', type=str, help= "Use '--branch=' followed by a branch_name")

args = parser.parse_args()
branch = str(args.branch)
print 'You selected option:', branch

def hplot(hist,color,style):
    hist.SetLineColor(color)
    hist.SetLineStyle(style)
    hist.SetStats(0)
    hist.Draw('HIST SAME')


sigfile = ROOT.TFile("new_signal_tthh.root","RO")
sigtree = sigfile.Get("OutputTree")

bgfileH = ROOT.TFile("new_background_ttH.root","RO")
bgtreeH = bgfileH.Get("OutputTree")

bgfileZ = ROOT.TFile("new_background_ttZ.root","RO")
bgtreeZ = bgfileZ.Get("OutputTree")

bgfileb = ROOT.TFile("new_background_ttbb.root","RO")
bgtreeb = bgfileb.Get("OutputTree")

bdtfile = ROOT.TFile("BDToutput_test_" + branch + ".root", "RO")
bdttree = bdtfile.Get(branch)
nbins = 30
# histograms to store our information
h01 = ROOT.TH1D('N Jets','N Jets;',30,0,30)#Signal
h02 = ROOT.TH1D('N2','N2;',30,0,30)#SIG w/BDT > threshold
h03 = ROOT.TH1D('N3','N3;',30,0,30)#BG
h04 = ROOT.TH1D('N4','N4;',30,0,30)#BG w/BDT > threshold
h11 = ROOT.TH1D('btag','btag;',9,0,9)#Signal
h12 = ROOT.TH1D('B2','B2;',9,0,9)#SIG w/BDT > threshold
h13 = ROOT.TH1D('B3','B3;',9,0,9)#BG
h14 = ROOT.TH1D('B4','B4;',9,0,9)#BG w/BDT > threshold
h21 = ROOT.TH1D('Srap','Srap;',60,0,10)#Signal
h22 = ROOT.TH1D('S2','S2;',60,0,10)#SIG w/BDT > threshold
h23 = ROOT.TH1D('S3','S3;',60,0,10)#BG
h24 = ROOT.TH1D('S4','S4;',60,0,10)#BG w/BDT > threshold
h41 = ROOT.TH1D('Cent','Cent;',10,0,1)#Signal
h42 = ROOT.TH1D('C2','C2;',10,0,1)#SIG w/BDT > threshold
h43 = ROOT.TH1D('C3','C3;',10,0,1)#BG
h44 = ROOT.TH1D('C4','C4;',10,0,1)#BG w/BDT > threshold
h51 = ROOT.TH1D('m_bb','m_bb;',10,0,250)#Signal
h52 = ROOT.TH1D('M2','M2;',10,0,250)#SIG w/BDT > threshold
h53 = ROOT.TH1D('M3','M3;',10,0,250)#BG
h54 = ROOT.TH1D('M4','M4;',10,0,250)#BG w/BDT > threshold
h61 = ROOT.TH1D('h_b','h_b;',10,0,1500)#Signal
h62 = ROOT.TH1D('HB2','HB2;',10,0,1500)#SIG w/BDT > threshold
h63 = ROOT.TH1D('HB3','HB3;',10,0,1500)#BG
h64 = ROOT.TH1D('HB4','HB4;',10,0,1500)#BG w/BDT > threshold
h71 = ROOT.TH1D('#DeltaR3','#DeltaR3;',100,-.5,9.5)
h72 = ROOT.TH1D('DR3_2','DR3_2;',100,-.5,9.5)
h73 = ROOT.TH1D('DR3_3','DR3_3;',100,-.5,9.5)
h74 = ROOT.TH1D('DR3_4','DR3_4;',100,-.5,9.5)
h81 = ROOT.TH1D('met1','met1;',100,0,300)
h82 = ROOT.TH1D('mt12','mt12;',100,0,300)
h83 = ROOT.TH1D('mt13','mt13;',100,0,300)
h84 = ROOT.TH1D('mt14','mt14;',100,0,300)
h91 = ROOT.TH1D('met2','met2;',100,0,300)
h92 = ROOT.TH1D('mt22','mt22;',100,0,300)
h93 = ROOT.TH1D('mt23','mt23;',100,0,300)
h94 = ROOT.TH1D('mt24','mt24;',100,0,300)
h31 = ROOT.TH2D('2D N Jets','2D N Jets;Amount of jets;bdt score',30,0,30,10,-1,1)
h32 = ROOT.TH2D('2D B Tags','2D B Tags;Amount of btag jets;bdt score', 9,0, 9,10,-1,1)
h33 = ROOT.TH2D('2D Srap','2D Srap;pseudorapidity;bdt score',60,0,10,10,-1,1)
h34 = ROOT.TH2D('2D Cent','2D Cent;Centrality;bdt score',10,0,1,10,-1,1)
h35 = ROOT.TH2D('2D m_bb','2D m_bb;Higgs boson candidate mass;bdt score',10,0,250,10,-1,1)
h36 = ROOT.TH2D('2D h_b','2D h_b;scalar sum of pT for b-tagged jets;bdt score',10,0,1500,10,-1,1)
h37 = ROOT.TH2D('2D DR3','2D DR3;Lowest #DeltaR;bdt score',100,-.5,9.5,10,-1,1)
h38 = ROOT.TH2D('2D met1','2D met1;Transverse mass (GeV);bdt score',100,0,300,10,-1,1)
h39 = ROOT.TH2D('2D met2','2D met2;Transverse mass (GeV)',100,0,300,10,-1,1)


c1 = ROOT.TCanvas('c1','Canvas 1',710,100,1000,500)
c1.Divide(3,2,0.01,0.01,0)
if branch == 'phase3':
    c2 = ROOT.TCanvas('c2','Canvas 2',710,100,1000,500)
    c2.Divide(3,2,0.01,0.01,0)
if branch == 'phase4':
    c2 = ROOT.TCanvas('c2','Canvas 2',710,100,1000,500)
    c2.Divide(3,2,0.01,0.01,0)
    c3 = ROOT.TCanvas('c3','Canvas 3',710,100,1000,500)
    c3.Divide(3,2,0.01,0.01,0)

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
chain.Add("new_background_ttH.root")
chain.Add("new_background_ttZ.root")


# this is the key line, where we associate the BDT output to the inputs.
chain.AddFriend(bdttree)

nsignalevents = sigtree.GetEntriesFast()
nevents = 0

bdt_threshold = -0.2

for event in chain:
    h31.Fill(event.njet[0],chain.y,event.mcweight[0])
    h32.Fill(event.btag,chain.y,event.mcweight[0])
    h33.Fill(event.srap,chain.y,event.mcweight[0])
    h34.Fill(event.cent,chain.y,event.mcweight[0])
    h35.Fill(event.m_bb,chain.y,event.mcweight[0])
    h36.Fill(event.h_b,chain.y,event.mcweight[0])
    h37.Fill(event.dr3,chain.y,event.mcweight[0]) 
    h38.Fill(event.mt1,chain.y,event.mcweight[0]) 
    h39.Fill(event.mt2,chain.y,event.mcweight[0]) 
    if nevents<nsignalevents:
        h01.Fill(event.njet[0],event.mcweight[0])# SIG ALL
        h11.Fill(event.btag,event.mcweight[0])# SIG ALL
        h21.Fill(event.srap,event.mcweight[0])# SIG ALL
        if branch == 'phase3':
            h41.Fill(event.cent,event.mcweight[0])# SIG ALL
            h51.Fill(event.m_bb,event.mcweight[0])# SIG ALL
            h61.Fill(event.h_b,event.mcweight[0])# SIG ALL
        elif branch == 'phase4':
            h41.Fill(event.cent,event.mcweight[0])# SIG ALL
            h51.Fill(event.m_bb,event.mcweight[0])# SIG ALL
            h61.Fill(event.h_b,event.mcweight[0])# SIG ALL
            h71.Fill(event.dr3,event.mcweight[0])# SIG ALL
            h81.Fill(event.mt1,event.mcweight[0])# SIG ALL
            h91.Fill(event.mt2,event.mcweight[0])# SIG ALL
        if chain.y > bdt_threshold:
            h02.Fill(event.njet[0],event.mcweight[0])# SIG ALL,BDT > 0.0
            h12.Fill(event.btag,event.mcweight[0])# SIG ALL,BDT > 0.0
            h22.Fill(event.srap,event.mcweight[0])# SIG ALL,BDT > 0.0          
            if branch == 'phase3':
                h42.Fill(event.cent,event.mcweight[0])# SIG ALL
                h52.Fill(event.m_bb,event.mcweight[0])# SIG ALL
                h62.Fill(event.h_b,event.mcweight[0])# SIG ALL
            elif branch == 'phase4':
                h42.Fill(event.cent,event.mcweight[0])# SIG ALL
                h52.Fill(event.m_bb,event.mcweight[0])# SIG ALL
                h62.Fill(event.h_b,event.mcweight[0])# SIG ALL
                h72.Fill(event.dr3,event.mcweight[0])# SIG ALL
                h82.Fill(event.mt1,event.mcweight[0])# SIG ALL
                h92.Fill(event.mt2,event.mcweight[0])# SIG ALL
    else:
        h03.Fill(event.njet[0],event.mcweight[0])# BG,ALL
        h13.Fill(event.btag,event.mcweight[0])# BG,ALL
        h23.Fill(event.srap,event.mcweight[0])# BG,ALL
        if branch == 'phase3':
            h43.Fill(event.cent,event.mcweight[0])# bg ALL
            h53.Fill(event.m_bb,event.mcweight[0])# bg ALL
            h63.Fill(event.h_b,event.mcweight[0])# bg ALL
        elif branch == 'phase4':
            h43.Fill(event.cent,event.mcweight[0])# bg ALL
            h53.Fill(event.m_bb,event.mcweight[0])# bg ALL
            h63.Fill(event.h_b,event.mcweight[0])# bg ALL
            h73.Fill(event.dr3,event.mcweight[0])# bg ALL
            h83.Fill(event.mt1,event.mcweight[0])# bg ALL
            h93.Fill(event.mt2,event.mcweight[0])# bg ALL
        if chain.y > bdt_threshold:
            h04.Fill(event.njet[0],event.mcweight[0])#BG,BDT > THRESHOLD
            h14.Fill(event.btag,event.mcweight[0])#BG,BDT > THRESHOLD
            h24.Fill(event.srap,event.mcweight[0])#BG,BDT > THRESHOLD
            if branch == 'phase3':
                h44.Fill(event.cent,event.mcweight[0])#BG,BDT > THRESHOLD
                h54.Fill(event.m_bb,event.mcweight[0])#BG,BDT > THRESHOLD
                h64.Fill(event.h_b,event.mcweight[0])#BG,BDT > THRESHOLD
            elif branch == 'phase4':
                h44.Fill(event.cent,event.mcweight[0])#BG,BDT > THRESHOLD
                h54.Fill(event.m_bb,event.mcweight[0])#BG,BDT > THRESHOLD
                h64.Fill(event.h_b,event.mcweight[0])#BG,BDT > THRESHOLD
                h74.Fill(event.dr3,event.mcweight[0])#BG,BDT > THRESHOLD
                h84.Fill(event.mt1,event.mcweight[0])#BG,BDT > THRESHOLD
                h94.Fill(event.mt2,event.mcweight[0])#BG,BDT > THRESHOLD
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
c1.cd(4)################################################
h31.SetStats(0)
h31.Draw('COLZ')
c1.cd(5).SetLogz()################################################
h32.SetStats(0)
h32.Draw('COLZ')
c1.cd(6).SetLogz()################################################
h33.SetStats(0)
h33.Draw('COLZ')
if branch == 'phase3':
    c2.cd(1).SetLogy()##################################### cent.
    h41.SetMaximum(10e6)
    hplot(h41,ROOT.kRed,1)
    hplot(h42,ROOT.kRed,2)
    hplot(h43,ROOT.kBlue,1)
    hplot(h44,ROOT.kBlue,2)
    leg.Draw()
    c2.cd(2).SetLogy()##################################### m_bb.
    h51.SetMaximum(2e6)
    hplot(h51,ROOT.kRed,1)
    hplot(h52,ROOT.kRed,2)
    hplot(h53,ROOT.kBlue,1)
    hplot(h54,ROOT.kBlue,2)
    leg.Draw()
    c2.cd(3).SetLogy()##################################### h_b.
    h61.SetMaximum(3.1e6)
    hplot(h61,ROOT.kRed,1)
    hplot(h62,ROOT.kRed,2)
    hplot(h63,ROOT.kBlue,1)
    hplot(h64,ROOT.kBlue,2)
    leg.Draw()
    c2.cd(4).SetLogz()########################### cent/bdt
    h34.SetStats(0)
    h34.Draw('COLZ')
    c2.cd(5).SetLogz()########################### m_bb/bdt
    h35.SetStats(0)
    h35.Draw('COLZ')
    c2.cd(6).SetLogz()########################### h_b/bdt
    h36.SetStats(0)
    h36.Draw('COLZ')
elif branch == 'phase4':
    c2.cd(1).SetLogy()##################################### cent.
    h41.SetMaximum(10e6)
    hplot(h41,ROOT.kRed,1)
    hplot(h42,ROOT.kRed,2)
    hplot(h43,ROOT.kBlue,1)
    hplot(h44,ROOT.kBlue,2)
    leg.Draw()
    c2.cd(2).SetLogy()##################################### m_bb.
    h51.SetMaximum(2e6)
    hplot(h51,ROOT.kRed,1)
    hplot(h52,ROOT.kRed,2)
    hplot(h53,ROOT.kBlue,1)
    hplot(h54,ROOT.kBlue,2)
    leg.Draw()
    c2.cd(3).SetLogy()##################################### h_b.
    h61.SetMaximum(3.1e6)
    hplot(h61,ROOT.kRed,1)
    hplot(h62,ROOT.kRed,2)
    hplot(h63,ROOT.kBlue,1)
    hplot(h64,ROOT.kBlue,2)
    leg.Draw()
    c2.cd(4).SetLogz()########################### cent/bdt
    h34.SetStats(0)
    h34.Draw('COLZ')
    c2.cd(5).SetLogz()########################### m_bb/bdt
    h35.SetStats(0)
    h35.Draw('COLZ')
    c2.cd(6).SetLogz()########################### h_b/bdt
    h36.SetStats(0)
    h36.Draw('COLZ')
 #################################phase4##################################   
    c3.cd(1).SetLogy()##################################### dr3.
    h71.SetMaximum(10e6)
    hplot(h71,ROOT.kRed,1)
    hplot(h72,ROOT.kRed,2)
    hplot(h73,ROOT.kBlue,1)
    hplot(h74,ROOT.kBlue,2)
    leg.Draw()
    c3.cd(2).SetLogy()##################################### mt1.
    h81.SetMaximum(2e6)
    hplot(h81,ROOT.kRed,1)
    hplot(h82,ROOT.kRed,2)
    hplot(h83,ROOT.kBlue,1)
    hplot(h84,ROOT.kBlue,2)
    leg.Draw()
    c3.cd(3).SetLogy()##################################### mt2.
    h91.SetMaximum(3.1e6)
    hplot(h91,ROOT.kRed,1)
    hplot(h92,ROOT.kRed,2)
    hplot(h93,ROOT.kBlue,1)
    hplot(h94,ROOT.kBlue,2)
    leg.Draw()
    c3.cd(4).SetLogz()########################### dr3/bdt
    h37.SetStats(0)
    h37.Draw('COLZ')
    c3.cd(5).SetLogz()########################### mt1/bdt
    h38.SetStats(0)
    h38.Draw('COLZ')
    c3.cd(6).SetLogz()########################### mt2/bdt
    h39.SetStats(0)
    h39.Draw('COLZ')