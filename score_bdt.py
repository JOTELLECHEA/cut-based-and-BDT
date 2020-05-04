import ROOT
import argparse

parser = argparse.ArgumentParser(description= 'Variable plots with signal/background/bdt score and 2d plots.')
parser.add_argument("--branch", default='wrong', type=str, help= "Use '--branch=' followed by a branch_name")

args = parser.parse_args()
branch = str(args.branch)
print 'You selected option:', branch

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
Njet1 = ROOT.TH1D('N Jets','N Jets;',30,0,30)#Signal
Njet2 = ROOT.TH1D('N2','N2;',30,0,30)#SIG w/BDT > threshold
Njet3 = ROOT.TH1D('N3','N3;',30,0,30)#BG
Njet4 = ROOT.TH1D('N4','N4;',30,0,30)#BG w/BDT > threshold
btag1 = ROOT.TH1D('btag','btag;',9,0,9)#Signal
btag2 = ROOT.TH1D('B2','B2;',9,0,9)#SIG w/BDT > threshold
btag3 = ROOT.TH1D('B3','B3;',9,0,9)#BG
btag4 = ROOT.TH1D('B4','B4;',9,0,9)#BG w/BDT > threshold
Srap1 = ROOT.TH1D('Srap','Srap;',60,0,10)#Signal
Srap2 = ROOT.TH1D('S2','S2;',60,0,10)#SIG w/BDT > threshold
Srap3 = ROOT.TH1D('S3','S3;',60,0,10)#BG
Srap4 = ROOT.TH1D('S4','S4;',60,0,10)#BG w/BDT > threshold
Cent1 = ROOT.TH1D('Cent','Cent;',10,0,1)#Signal
Cent2 = ROOT.TH1D('C2','C2;',10,0,1)#SIG w/BDT > threshold
Cent3 = ROOT.TH1D('C3','C3;',10,0,1)#BG
Cent4 = ROOT.TH1D('C4','C4;',10,0,1)#BG w/BDT > threshold
M_bb1 = ROOT.TH1D('m_bb','m_bb;',10,0,250)#Signal
M_bb2 = ROOT.TH1D('M2','M2;',10,0,250)#SIG w/BDT > threshold
M_bb3 = ROOT.TH1D('M3','M3;',10,0,250)#BG
M_bb4 = ROOT.TH1D('M4','M4;',10,0,250)#BG w/BDT > threshold
h__b1 = ROOT.TH1D('h_b','h_b;',10,0,1500)#Signal
h__b2 = ROOT.TH1D('HB2','HB2;',10,0,1500)#SIG w/BDT > threshold
h__b3 = ROOT.TH1D('HB3','HB3;',10,0,1500)#BG
h__b4 = ROOT.TH1D('HB4','HB4;',10,0,1500)#BG w/BDT > threshold
dr_11 = ROOT.TH1D('#DeltaR1','#DeltaR1;',100,-.5,9.5)
dr_12 = ROOT.TH1D('DR1_2','DR1_2;',100,-.5,9.5)
dr_13 = ROOT.TH1D('DR1_3','DR1_3;',100,-.5,9.5)
dr_14 = ROOT.TH1D('DR1_4','DR1_4;',100,-.5,9.5)
dr_21 = ROOT.TH1D('#DeltaR2','#DeltaR2;',100,-.5,9.5)
dr_22 = ROOT.TH1D('DR2_2','DR2_2;',100,-.5,9.5)
dr_23 = ROOT.TH1D('DR2_3','DR2_3;',100,-.5,9.5)
dr_24 = ROOT.TH1D('DR2_4','DR2_4;',100,-.5,9.5)
dr_31 = ROOT.TH1D('#DeltaR3','#DeltaR3;',100,-.5,9.5)
dr_32 = ROOT.TH1D('DR3_2','DR3_2;',100,-.5,9.5)
dr_33 = ROOT.TH1D('DR3_3','DR3_3;',100,-.5,9.5)
dr_34 = ROOT.TH1D('DR3_4','DR3_4;',100,-.5,9.5)
met11 = ROOT.TH1D('met1','met1;',100,0,300)
met12 = ROOT.TH1D('mt12','mt12;',100,0,300)
met13 = ROOT.TH1D('mt13','mt13;',100,0,300)
met14 = ROOT.TH1D('mt14','mt14;',100,0,300)
met21 = ROOT.TH1D('met2','met2;',100,0,300)
met22 = ROOT.TH1D('mt22','mt22;',100,0,300)
met23 = ROOT.TH1D('mt23','mt23;',100,0,300)
met24 = ROOT.TH1D('mt24','mt24;',100,0,300)
met31 = ROOT.TH1D('met3','met3;',100,0,300)
met32 = ROOT.TH1D('mt32','mt32;',100,0,300)
met33 = ROOT.TH1D('mt33','mt33;',100,0,300)
met34 = ROOT.TH1D('mt34','mt34;',100,0,300)
Nlep1 = ROOT.TH1D('N Leps','N Leptons;',3,0,3)#Signal
Nlep2 = ROOT.TH1D('L2','l2;',3,0,3)#SIG w/BDT > threshold
Nlep3 = ROOT.TH1D('L3','l3;',3,0,3)#BG
Nlep4 = ROOT.TH1D('L4','l4;',3,0,3)#BG w/BDT > threshol
sig00 = ROOT.TH2D('2D N L','Signal;bdt score',3,0,3,10,-1,1)
bac00 = ROOT.TH2D('bac00','bac00;bdt score',3,0,3,10,-1,1)
sig01 = ROOT.TH2D('2D N Jets','Signal;bdt score',30,0,30,10,-1,1)
bac01 = ROOT.TH2D('bac01','background;bdt score',30,0,30,10,-1,1)
sig02 = ROOT.TH2D('2D B Tags','Signal;bdt score', 9,0, 9,10,-1,1)
bac02 = ROOT.TH2D('bac02','background;bdt score', 9,0, 9,10,-1,1)
sig03 = ROOT.TH2D('2D Srap','Signal;bdt score',60,0,10,10,-1,1)
bac03 = ROOT.TH2D('bac03','background;bdt score',60,0,10,10,-1,1)
sig04 = ROOT.TH2D('2D Cent','Signal;bdt score',10,0,1,10,-1,1)
bac04 = ROOT.TH2D('bac04','background;bdt score',10,0,1,10,-1,1)
sig05 = ROOT.TH2D('2D m_bb','Signal;bdt score',10,0,250,10,-1,1)
bac05 = ROOT.TH2D('bac05','background;bdt score',10,0,250,10,-1,1)
sig06 = ROOT.TH2D('2D h_b','Signal;bdt score',10,0,1500,10,-1,1)
bac06 = ROOT.TH2D('bac06','background;bdt score',10,0,1500,10,-1,1)
sig07 = ROOT.TH2D('2D DR3','Signal;bdt score',100,-.5,9.5,10,-1,1)
bac07 = ROOT.TH2D('bac07','background;bdt score',100,-.5,9.5,10,-1,1)
sig08 = ROOT.TH2D('2D met1','Signal;bdt score',100,0,300,10,-1,1)
bac08 = ROOT.TH2D('bac08','background;bdt score',100,0,300,10,-1,1)
sig09 = ROOT.TH2D('2D met2','Signal;bdt score',100,0,300,10,-1,1)
bac09 = ROOT.TH2D('bac09','background;bdt score',100,0,300,10,-1,1)
sig10 = ROOT.TH2D('2D met3','Signal;bdt score',100,0,300,10,-1,1)
bac10 = ROOT.TH2D('bac10','background;bdt score',100,0,300,10,-1,1)
sig11 = ROOT.TH2D('2D DR1','Signal;bdt score',100,-.5,9.5,10,-1,1)
bac11 = ROOT.TH2D('bac11','background;bdt score',100,-.5,9.5,10,-1,1)
sig12 = ROOT.TH2D('2D DR2','Signal;bdt score',100,-.5,9.5,10,-1,1)
bac12 = ROOT.TH2D('bac12','background;bdt score',100,-.5,9.5,10,-1,1)


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
    if nevents<nsignalevents:
        Njet1.Fill(event.njet[0],event.mcweight[0])# SIG ALL
        btag1.Fill(event.btag,event.mcweight[0])# SIG ALL
        Srap1.Fill(event.srap,event.mcweight[0])# SIG ALL
        Nlep1.Fill(event.nlep[0],event.mcweight[0])# SIG ALL
        sig01.Fill(event.njet[0],chain.y,event.mcweight[0])
        sig02.Fill(event.btag,chain.y,event.mcweight[0])
        sig03.Fill(event.srap,chain.y,event.mcweight[0])
        sig04.Fill(event.cent,chain.y,event.mcweight[0])
        sig05.Fill(event.m_bb,chain.y,event.mcweight[0])
        sig06.Fill(event.h_b,chain.y,event.mcweight[0])
        sig07.Fill(event.dr3,chain.y,event.mcweight[0]) 
        sig08.Fill(event.mt1,chain.y,event.mcweight[0]) 
        sig09.Fill(event.mt2,chain.y,event.mcweight[0])
        sig10.Fill(event.mt3,chain.y,event.mcweight[0])
        sig11.Fill(event.dr1,chain.y,event.mcweight[0]) 
        sig12.Fill(event.dr2,chain.y,event.mcweight[0])
        sig00.Fill(event.nlep[0],chain.y,event.mcweight[0])# SIG ALL 
        if branch == 'phase3':
            Cent1.Fill(event.cent,event.mcweight[0])# SIG ALL
            M_bb1.Fill(event.m_bb,event.mcweight[0])# SIG ALL
            h__b1.Fill(event.h_b,event.mcweight[0])# SIG ALL
        elif branch == 'phase4':
            Cent1.Fill(event.cent,event.mcweight[0])# SIG ALL
            M_bb1.Fill(event.m_bb,event.mcweight[0])# SIG ALL
            h__b1.Fill(event.h_b,event.mcweight[0])# SIG ALL
            dr_11.Fill(event.dr1,event.mcweight[0])# SIG ALL
            dr_21.Fill(event.dr2,event.mcweight[0])# SIG ALL
            dr_31.Fill(event.dr3,event.mcweight[0])# SIG ALL
            met11.Fill(event.mt1,event.mcweight[0])# SIG ALL
            met21.Fill(event.mt2,event.mcweight[0])# SIG ALL
            met31.Fill(event.mt3,event.mcweight[0])# SIG ALL
        if chain.y > bdt_threshold:
            Njet2.Fill(event.njet[0],event.mcweight[0])# SIG ALL,BDT > 0.0
            btag2.Fill(event.btag,event.mcweight[0])# SIG ALL,BDT > 0.0
            Srap2.Fill(event.srap,event.mcweight[0])# SIG ALL,BDT > 0.0
            Nlep2.Fill(event.nlep[0],event.mcweight[0])# SIG ALL          
            if branch == 'phase3':
                Cent2.Fill(event.cent,event.mcweight[0])# SIG ALL
                M_bb2.Fill(event.m_bb,event.mcweight[0])# SIG ALL
                h__b2.Fill(event.h_b,event.mcweight[0])# SIG ALL
            elif branch == 'phase4':
                Cent2.Fill(event.cent,event.mcweight[0])# SIG ALL
                M_bb2.Fill(event.m_bb,event.mcweight[0])# SIG ALL
                h__b2.Fill(event.h_b,event.mcweight[0])# SIG ALL
                dr_12.Fill(event.dr1,event.mcweight[0])# SIG ALL
                dr_22.Fill(event.dr2,event.mcweight[0])# SIG ALL
                dr_32.Fill(event.dr3,event.mcweight[0])# SIG ALL
                met12.Fill(event.mt1,event.mcweight[0])# SIG ALL
                met22.Fill(event.mt2,event.mcweight[0])# SIG ALL
                met32.Fill(event.mt3,event.mcweight[0])# SIG ALL
    else:
        Njet3.Fill(event.njet[0],event.mcweight[0])# BG,ALL
        btag3.Fill(event.btag,event.mcweight[0])# BG,ALL
        Srap3.Fill(event.srap,event.mcweight[0])# BG,ALL
        Nlep3.Fill(event.nlep[0],event.mcweight[0])#
        bac01.Fill(event.njet[0],chain.y,event.mcweight[0])
        bac02.Fill(event.btag,chain.y,event.mcweight[0])
        bac03.Fill(event.srap,chain.y,event.mcweight[0])
        bac04.Fill(event.cent,chain.y,event.mcweight[0])
        bac05.Fill(event.m_bb,chain.y,event.mcweight[0])
        bac06.Fill(event.h_b,chain.y,event.mcweight[0])
        bac07.Fill(event.dr3,chain.y,event.mcweight[0]) 
        bac08.Fill(event.mt1,chain.y,event.mcweight[0]) 
        bac09.Fill(event.mt2,chain.y,event.mcweight[0])
        bac10.Fill(event.mt3,chain.y,event.mcweight[0])
        bac11.Fill(event.dr1,chain.y,event.mcweight[0]) 
        bac12.Fill(event.dr2,chain.y,event.mcweight[0]) 
        bac00.Fill(event.nlep[0],chain.y,event.mcweight[0])
        if branch == 'phase3':
            Cent3.Fill(event.cent,event.mcweight[0])# bg ALL
            M_bb3.Fill(event.m_bb,event.mcweight[0])# bg ALL
            h__b3.Fill(event.h_b,event.mcweight[0])# bg ALL
        elif branch == 'phase4':
            Cent3.Fill(event.cent,event.mcweight[0])# bg ALL
            M_bb3.Fill(event.m_bb,event.mcweight[0])# bg ALL
            h__b3.Fill(event.h_b,event.mcweight[0])# bg ALL
            dr_13.Fill(event.dr1,event.mcweight[0])# bg ALL
            dr_23.Fill(event.dr2,event.mcweight[0])# bg ALL
            dr_33.Fill(event.dr3,event.mcweight[0])# bg ALL
            met13.Fill(event.mt1,event.mcweight[0])# bg ALL
            met23.Fill(event.mt2,event.mcweight[0])# bg ALL
            met33.Fill(event.mt3,event.mcweight[0])# bg ALL
        if chain.y > bdt_threshold:
            Njet4.Fill(event.njet[0],event.mcweight[0])#BG,BDT > THRESHOLD
            btag4.Fill(event.btag,event.mcweight[0])#BG,BDT > THRESHOLD
            Srap4.Fill(event.srap,event.mcweight[0])#BG,BDT > THRESHOLD
            Nlep4.Fill(event.nlep[0],event.mcweight[0])
            if branch == 'phase3':
                Cent4.Fill(event.cent,event.mcweight[0])#BG,BDT > THRESHOLD
                M_bb4.Fill(event.m_bb,event.mcweight[0])#BG,BDT > THRESHOLD
                h__b4.Fill(event.h_b,event.mcweight[0])#BG,BDT > THRESHOLD
            elif branch == 'phase4':
                Cent4.Fill(event.cent,event.mcweight[0])#BG,BDT > THRESHOLD
                M_bb4.Fill(event.m_bb,event.mcweight[0])#BG,BDT > THRESHOLD
                h__b4.Fill(event.h_b,event.mcweight[0])#BG,BDT > THRESHOLD
                dr_14.Fill(event.dr1,event.mcweight[0])#BG,BDT > THRESHOLD
                dr_24.Fill(event.dr2,event.mcweight[0])#BG,BDT > THRESHOLD
                dr_34.Fill(event.dr3,event.mcweight[0])#BG,BDT > THRESHOLD
                met14.Fill(event.mt1,event.mcweight[0])#BG,BDT > THRESHOLD
                met24.Fill(event.mt2,event.mcweight[0])#BG,BDT > THRESHOLD
                met34.Fill(event.mt3,event.mcweight[0])#BG,BDT > THRESHOLD
    nevents+=1

g = ROOT.TFile('bdt_hist'+branch+'.root','update')
##########################################################################
Njet1 = Njet1.Clone('Njet1')
Njet1.Write()
Njet2 = Njet2.Clone('Njet2')
Njet2.Write()
Njet3 = Njet3.Clone('Njet3')
Njet3.Write()
Njet4 = Njet4.Clone('Njet4')
Njet4.Write()
btag1 = btag1.Clone('btag1')
btag1.Write()
btag2 = btag2.Clone('btag2')
btag2.Write()
btag3 = btag3.Clone('btag3')
btag3.Write()
btag4 = btag4.Clone('btag4')
btag4.Write()
Srap1 = Srap1.Clone('Srap1')
Srap1.Write()
Srap2 = Srap2.Clone('Srap2')
Srap2.Write()
Srap3 = Srap3.Clone('Srap3')
Srap3.Write()
Srap4 = Srap4.Clone('Srap4')
Srap4.Write()
Cent1 = Cent1.Clone('Cent1')
Cent1.Write() 
Cent2 = Cent2.Clone('Cent2')
Cent2.Write()
Cent3 = Cent3.Clone('Cent3')
Cent3.Write() 
Cent4 = Cent4.Clone('Cent4')
Cent4.Write()
M_bb1 = M_bb1.Clone('M_bb1')
M_bb1.Write()
M_bb2 = M_bb2.Clone('M_bb2')
M_bb2.Write() 
M_bb3 = M_bb3.Clone('M_bb3')
M_bb3.Write() 
M_bb4 = M_bb4.Clone('M_bb4')
M_bb4.Write() 
h__b1 = h__b1.Clone('h__b1')
h__b1.Write()
h__b2 = h__b2.Clone('h__b2')
h__b2.Write()
h__b3 = h__b3.Clone('h__b3')
h__b3.Write()
h__b4 = h__b4.Clone('h__b4')
h__b4.Write()
dr_11 = dr_11.Clone('dr_11')
dr_11.Write()
dr_12 = dr_12.Clone('dr_12')
dr_12.Write()
dr_13 = dr_13.Clone('dr_13')
dr_13.Write()
dr_14 = dr_14.Clone('dr_14')
dr_14.Write()
dr_21 = dr_21.Clone('dr_21')
dr_21.Write()
dr_22 = dr_22.Clone('dr_22')
dr_22.Write()
dr_23 = dr_23.Clone('dr_23')
dr_23.Write()
dr_24 = dr_24.Clone('dr_24')
dr_24.Write()
dr_31 = dr_31.Clone('dr_31')
dr_31.Write()
dr_32 = dr_32.Clone('dr_32')
dr_32.Write()
dr_33 = dr_33.Clone('dr_33')
dr_33.Write()
dr_34 = dr_34.Clone('dr_34')
dr_34.Write()
met11 = met11.Clone('met11')
met11.Write()
met12 = met12.Clone('met12')
met12.Write()
met13 = met13.Clone('met13')
met13.Write()
met14 = met14.Clone('met14')
met14.Write()
met21 = met21.Clone('met21')
met21.Write()
met22 = met22.Clone('met22')
met22.Write()
met23 = met23.Clone('met23')
met23.Write()
met24 = met24.Clone('met24')
met24.Write()
met31 = met31.Clone('met31')
met31.Write()
met32 = met32.Clone('met32')
met32.Write()
met33 = met33.Clone('met33')
met33.Write()
met34 = met34.Clone('met34')
met34.Write()
Nlep1 = Nlep1.Clone('Nlep1')
Nlep1.Write()
Nlep2 = Nlep2.Clone('Nlep2')
Nlep2.Write()
Nlep3 = Nlep3.Clone('Nlep3')
Nlep3.Write()
Nlep4 = Nlep4.Clone('Nlep4')
Nlep4.Write()
sig00 = sig00.Clone('sig00')
sig00.Write() 
bac00 = bac00.Clone('bac00')
bac00.Write()
sig01 = sig01.Clone('sig01')
sig01.Write()
bac01 = bac01.Clone('bac01')
bac01.Write()
sig02 = sig02.Clone('sig02')
sig02.Write()
bac02 = bac02.Clone('bac02')
bac02.Write()
sig03 = sig03.Clone('sig03')
sig03.Write()
bac03 = bac03.Clone('bac03')
bac03.Write()
sig04 = sig04.Clone('sig04')
sig04.Write()
bac04 = bac04.Clone('bac04')
bac04.Write()
sig05 = sig05.Clone('sig05')
sig05.Write()
bac05 = bac05.Clone('bac05')
bac05.Write()
sig06 = sig06.Clone('sig06')
sig06.Write()
bac06 = bac06.Clone('bac06')
bac06.Write()
sig07 = sig07.Clone('sig07')
sig07.Write()
bac07 = bac07.Clone('bac07')
bac07.Write()
sig08 = sig08.Clone('sig08')
sig08.Write()
bac08 = bac08.Clone('bac08')
bac08.Write()
sig09 = sig09.Clone('sig09')
sig09.Write() 
bac09 = bac09.Clone('bac09')
bac09.Write()
sig10 = sig10.Clone('sig10')
sig10.Write()
bac10 = bac10.Clone('bac10')
bac10.Write()
sig11 = sig11.Clone('sig11')
sig11.Write()
bac11 = bac11.Clone('bac11')
bac11.Write()
sig12 = sig12.Clone('sig12')
sig12.Write()
bac12 = bac12.Clone('bac12')
bac12.Write()
print('Done')