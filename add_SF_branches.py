#!/usr/bin/env python2

'''
script to add sfs to ntuples
'''

import os, time, sys, argparse,math
import numpy as np
from array import array
import shutil

import ROOT
   
def augment_rootfile(filepath):
    
    shutil.copyfile(filepath,"new_"+filepath)

    # get tree to loop over
    treename = "OutputTree"
    t = ROOT.TFile("new_"+filepath, "UPDATE")
    tree = t.Get(treename)

    # define branches
    lep1pT  = array( 'f', [ 0 ] )
    lep1eta = array( 'f', [ 0 ] )
    lep1phi = array( 'f', [ 0 ] )
    lep1m   = array( 'f', [ 0 ] )
    lep2pT  = array( 'f', [ 0 ] )
    lep2eta = array( 'f', [ 0 ] )
    lep2phi = array( 'f', [ 0 ] )
    lep2m   = array( 'f', [ 0 ] )
    lep3pT  = array( 'f', [ 0 ] )
    lep3eta = array( 'f', [ 0 ] )
    lep3phi = array( 'f', [ 0 ] )
    lep3m   = array( 'f', [ 0 ] )
    mt1     = array( 'f', [ 0 ] )
    mt2     = array( 'f', [ 0 ] )
    mt3     = array( 'f', [ 0 ] )
    dr1     = array( 'f', [ 0 ] )
    dr2     = array( 'f', [ 0 ] )
    dr3     = array( 'f', [ 0 ] )



    br_lep1pT  = tree.Branch( 'lep1pT' , lep1pT , 'lep1pT/F'  )
    br_lep1eta = tree.Branch( 'lep1eta', lep1eta, 'lep1eta/F' )
    br_lep1phi = tree.Branch( 'lep1phi', lep1phi, 'lep1phi/F' )
    br_lep1m   = tree.Branch( 'lep1m'  , lep1m  , 'lep1m/F'   )
    br_lep2pT  = tree.Branch( 'lep2pT' , lep2pT , 'lep2pT/F'  )
    br_lep2eta = tree.Branch( 'lep2eta', lep2eta, 'lep2eta/F' )
    br_lep2phi = tree.Branch( 'lep2phi', lep2phi, 'lep2phi/F' )
    br_lep2m   = tree.Branch( 'lep2m'  , lep2m  , 'lep2m/F'   )
    br_lep3pT  = tree.Branch( 'lep3pT' , lep3pT , 'lep3pT/F'  )
    br_lep3eta = tree.Branch( 'lep3eta', lep3eta, 'lep3eta/F' )
    br_lep3phi = tree.Branch( 'lep3phi', lep3phi, 'lep3phi/F' )
    br_lep3m   = tree.Branch( 'lep3m'  , lep3m  , 'lep3m/F'   )
    br_mt1     = tree.Branch( 'mt1'    , mt1    , 'mt1/F'     )
    br_mt2     = tree.Branch( 'mt2'    , mt2    , 'mt2/F'     )
    br_mt3     = tree.Branch( 'mt3'    , mt3    , 'mt3/F'     )
    br_dr1     = tree.Branch( 'dr1'    , dr1    , 'dr1/F'     )
    br_dr2     = tree.Branch( 'dr2'    , dr2    , 'dr2/F'     )
    br_dr3     = tree.Branch( 'dr3'    , dr3    , 'dr3/F'     )

    # track the time
    start_time = time.clock()

######################################################################
    dR1 =[]
    dR2 =[]
    dR3 =[]
#######################################################################
    n_entries = tree.GetEntries()
    i = 1
    for event in tree:
        # show some progress
        if i % 1000 == 0: print("   processing entry {:8d}/{:d} [{:5.0f} evts/s]".format(i, n_entries, i/(time.clock()-start_time)))
        numlep = event.nlep[0]
        numjet = event.njet[0]
        if numlep >0:
            lep1m[0]   = 0.0
            lep1pT[0]  = event.leppT[0]
            lep1eta[0] = event.lepeta[0]
            lep1phi[0] = event.lepphi[0]
            mt1[0] = ROOT.TMath.Sqrt(2 * event.met[0] * event.leppT[0]/(10**6) * ( 1 - ROOT.TMath.Cos((event.lepphi[0] - event.met_phi[0]))))
            for x in xrange(numjet):
                dR1.append(np.sqrt((event.lepeta[0] - event.jeteta[x])**2 + (event.lepphi[0] - event.jetphi[x])**2))
            dr1[0] = min(dR1)
            if numlep > 1:
                lep2m[0]   = 0.0
                lep2pT[0]  = event.leppT[1]
                lep2eta[0] = event.lepeta[1]
                lep2phi[0] = event.lepphi[1]
                mt2[0] = ROOT.TMath.Sqrt(2 * event.met[0] * event.leppT[1]/(10**6) * ( 1 - ROOT.TMath.Cos((event.lepphi[1] - event.met_phi[0]))))
                for x in xrange(numjet):
                    dR2.append(np.sqrt((event.lepeta[1] - event.jeteta[x])**2 + (event.lepphi[1] - event.jetphi[x])**2))
                dr2[0] = min(dR2)
                if numlep > 2:
                    lep3m[0]   = 0.0
                    lep3pT[0]  = event.leppT[2]
                    lep3eta[0] = event.lepeta[2]
                    lep3phi[0] = event.lepphi[2]
                    mt3[0] = ROOT.TMath.Sqrt(2 * event.met[0] * event.leppT[2]/(10**6) * ( 1 - ROOT.TMath.Cos((event.lepphi[2] - event.met_phi[0]))))
                    for x in xrange(numjet):
                        dR3.append(np.sqrt((event.lepeta[2] - event.jeteta[x])**2 + (event.lepphi[2] - event.jetphi[x])**2))
                    dr3[0] = min(dR3)
                else:
                    lep3pT[0]  = -999
                    lep3eta[0] = -9
                    lep3phi[0] = -9
                    lep3m[0]   = -999
                    mt3[0]     = -999
                    dr3[0]     = -999
            else:
                lep2pT[0]  = -999
                lep2eta[0] = -9
                lep2phi[0] = -9
                lep2m[0]   = -999
                mt2[0]     = -999
                dr2[0]     = -999
                
        else:
            lep1pT[0]  = -999
            lep1eta[0] = -9
            lep1phi[0] = -9
            lep1m[0]   = -999
            mt1[0]     = -999
            dr1[0]     = -999




        # fill new branches
        br_lep1pT.Fill()
        br_lep1eta.Fill()
        br_lep1phi.Fill()
        br_lep1m.Fill()
        br_lep2pT.Fill()
        br_lep2eta.Fill()
        br_lep2phi.Fill()
        br_lep2m.Fill()
        br_lep3pT.Fill()
        br_lep3eta.Fill()
        br_lep3phi.Fill()
        br_lep3m.Fill()
        br_mt1.Fill()
        br_mt2.Fill()
        br_mt3.Fill()
        br_dr1.Fill()
        br_dr2.Fill()
        br_dr3.Fill() 
        i += 1

    # write augmented tree to original file
    tree.Write("", ROOT.TObject.kOverwrite)

    t.Close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='flatten/augment ntuples')
    parser.add_argument('--inputfile', help='input file to skim')
    args = parser.parse_args()

    augment_rootfile(args.inputfile)
