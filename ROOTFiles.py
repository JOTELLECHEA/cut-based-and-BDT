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

num = []
mt = []
mt1 = 0
i = 0
for event in MyTree:

    num.append(event.njet[0])
    if event.nlep[0] == 1:
        mt1 = ROOT.TMath.Sqrt(2 * event.met[0] * event.leppT[0]/(10**6) * ( 1 - ROOT.TMath.Cos((event.lepphi[0] - event.met_phi[0]))))
    mt.append(mt1)
print 'njets',max(num)
print 'mT',max(mt), 'avg', np.mean(mt), 'min',min(mt)
# print mt1
for i in xrange(event.nlep[0]):
    print event.met[i]



    # jet1pT  = array( 'f', [ 0 ] )
    # jet1eta = array( 'f', [ 0 ] )
    # jet1phi = array( 'f', [ 0 ] )
    # jet1m   = array( 'f', [ 0 ] )
    # jet1c   = array( 'i', [ 0 ] )
    # jet1b   = array( 'i', [ 0 ] )
    # jet2pT  = array( 'f', [ 0 ] )
    # jet2eta = array( 'f', [ 0 ] )
    # jet2phi = array( 'f', [ 0 ] )
    # jet2m   = array( 'f', [ 0 ] )
    # jet2c   = array( 'i', [ 0 ] )
    # jet2b   = array( 'i', [ 0 ] )
    # jet3pT  = array( 'f', [ 0 ] )
    # jet3eta = array( 'f', [ 0 ] )
    # jet3phi = array( 'f', [ 0 ] )
    # jet3m   = array( 'f', [ 0 ] )
    # jet3c   = array( 'i', [ 0 ] )
    # jet3b   = array( 'i', [ 0 ] )
    # jet4pT  = array( 'f', [ 0 ] )
    # jet4eta = array( 'f', [ 0 ] )
    # jet4phi = array( 'f', [ 0 ] )
    # jet4m   = array( 'f', [ 0 ] )
    # jet4c   = array( 'i', [ 0 ] )
    # jet4b   = array( 'i', [ 0 ] )
    # jet5pT  = array( 'f', [ 0 ] )
    # jet5eta = array( 'f', [ 0 ] )
    # jet5phi = array( 'f', [ 0 ] )
    # jet5m   = array( 'f', [ 0 ] )
    # jet5c   = array( 'i', [ 0 ] )
    # jet5b   = array( 'i', [ 0 ] )
    # jet6pT  = array( 'f', [ 0 ] )
    # jet6eta = array( 'f', [ 0 ] )
    # jet6phi = array( 'f', [ 0 ] )
    # jet6m   = array( 'f', [ 0 ] )
    # jet6c   = array( 'i', [ 0 ] )
    # jet6b   = array( 'i', [ 0 ] )
    # jet7pT  = array( 'f', [ 0 ] )
    # jet7eta = array( 'f', [ 0 ] )
    # jet7phi = array( 'f', [ 0 ] )
    # jet7m   = array( 'f', [ 0 ] )
    # jet7c   = array( 'i', [ 0 ] )
    # jet7b   = array( 'i', [ 0 ] )
    # jet8pT  = array( 'f', [ 0 ] )
    # jet8eta = array( 'f', [ 0 ] )
    # jet8phi = array( 'f', [ 0 ] )
    # jet8m   = array( 'f', [ 0 ] )
    # jet8c   = array( 'i', [ 0 ] )
    # jet8b   = array( 'i', [ 0 ] )
    # jet9pT  = array( 'f', [ 0 ] )
    # jet9eta = array( 'f', [ 0 ] )
    # jet9phi = array( 'f', [ 0 ] )
    # jet9m   = array( 'f', [ 0 ] )
    # jet9c   = array( 'i', [ 0 ] )
    # jet9b   = array( 'i', [ 0 ] )
    # jet10pT  = array( 'f', [ 0 ] )
    # jet10eta = array( 'f', [ 0 ] )
    # jet10phi = array( 'f', [ 0 ] )
    # jet10m   = array( 'f', [ 0 ] )
    # jet10c   = array( 'i', [ 0 ] )