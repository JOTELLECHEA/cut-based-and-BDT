import ROOT,numpy as np
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))

while True:
    try:
        x =  int(input('\n Which sample would you like to use: '))
        a = 'tthh_ntuple.343469.MadGraphPythia8EvtGen_A14NNPDF23_tthh_bbbb.root'
        b = 'tthh_ntuple.410246.Sherpa_NNPDF30NNLO_ttbb.root'
        c = 'tthh_ntuple.344436.Sherpa_NNPDF30NNLO_ttH_Htobb.root'
        d = 'tthh_ntuple.410247.Sherpa_NNPDF30NNLO_ttZ_Ztobb.root'
        print '\n'
        if x == 1:
            print 'You selected option:\n\n', a
            f = ROOT.TFile(a)
            break
        elif x == 2:
            print 'You selected option:\n\n', b
            f = ROOT.TFile(b)
            break
        elif x == 3:
            print 'You selected option:\n\n', c
            f = ROOT.TFile(c)
            break
        elif x == 4:
            print 'You selected option:\n\n', d
            f = ROOT.TFile(d)
            break
        elif x == 5:
            system('clear')
            sys.exit('Bye')
        else :
            sleep(1)
            system('clear')
            menu()
            prRed('****************** Invalid option, Enter 1-5 **************\n')
    except NameError:
        sleep(1)
        system('clear')
        menu()
        prRed('*******************Invalid option, Enter 1-5**************\n')
#------------------------------------------------------------------------------#
# Assign OutputTree as MyTree and get number of entries in tree.
MyTree = f.Get('OutputTree')

lepvec = {}
num = []
mt = []
mt1 = 0
lepvec2 = {}
i = 0
for event in MyTree:
    numlep = event.nlep[0]
    for i in xrange(numlep): 
        lepvec[i] = ROOT.TLorentzVector()
        lepvec2[i] = ROOT.TLorentzVector()
        lepvec[i].SetPtEtaPhiM(event.leppT[i],event.lepeta[i],event.lepphi[i],0)
        lepvec2[i].SetPtEtaPhiM(event.leppT[i]-3,event.lepeta[i]-3,event.lepphi[i]-3,0)
        if numlep > 0:
            print lepvec[0].Phi()
            print lepvec[0].DeltaPhi(lepvec2[0])
            print lepvec[0].Phi() - lepvec2[0].Phi()
#     num.append(event.njet[0])
#     if event.nlep[0] == 1:
#         mt1 = ROOT.TMath.Sqrt(2 * event.met[0] * event.leppT[0]/(10**6) * ( 1 - ROOT.TMath.Cos((event.lepphi[0] - event.met_phi[0]))))
#     mt.append(mt1)
# print 'njets',max(num)
# print 'mT',max(mt), 'avg', np.mean(mt), 'min',min(mt)
# # print mt1

