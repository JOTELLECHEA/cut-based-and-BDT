#!/usr/bin/env python2

'''
script to add sfs to ntuples
'''

import os, time, sys, argparse, numpy, math
from array import array

import ROOT
   
def augment_rootfile(filepath):
    
    # get tree to loop over
    treename = "OutputTree"
    t = ROOT.TFile(filepath, "UPDATE")
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

    # track the time
    start_time = time.clock()

    n_entries = tree.GetEntries()
    i = 1
    for entry in tree:
        # show some progress
        if i % 1000 == 0: print("   processing event {:8d}/{:d} [{:5.0f} evts/s]".format(i, n_entries, i/(time.clock()-start_time)))
        num = entry.nlep[0]
        if num >0:
            lep1m[0]   = 0.0
            lep1pT[0]  = entry.leppT[0]
            lep1eta[0] = entry.lepeta[0]
            lep1phi[0] = entry.lepphi[0]
            if num > 1:
                lep2m[0]   = 0.0
                lep2pT[0]  = entry.leppT[1]
                lep2eta[0] = entry.lepeta[1]
                lep2phi[0] = entry.lepphi[1]
                if num > 2:
                    lep3m[0]   = 0.0
                    lep3pT[0]  = entry.leppT[2]
                    lep3eta[0] = entry.lepeta[2]
                    lep3phi[0] = entry.lepphi[2]
                else:
                    lep3pT[0]  = -999
                    lep3eta[0] = -9
                    lep3phi[0] = -9
                    lep3m[0]   = -999
            else:
                lep2pT[0]  = -999
                lep2eta[0] = -9
                lep2phi[0] = -9
                lep2m[0]   = -999
        else:
            lep1pT[0]  = -999
            lep1eta[0] = -9
            lep1phi[0] = -9
            lep1m[0]   = -999




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
        i += 1

    # write augmented tree to original file
    tree.Write("", ROOT.TObject.kOverwrite)

    t.Close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='flatten/augment ntuples')
    parser.add_argument('--inputfile', help='input file to skim')
    args = parser.parse_args()

    augment_rootfile(args.inputfile)
