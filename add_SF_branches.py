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

    br_lep1pT  = tree.Branch( 'lep1pT' , lep1pT , 'lep1pT/F'  )
    br_lep1eta = tree.Branch( 'lep1eta', lep1eta, 'lep1eta/F' )
    br_lep1phi = tree.Branch( 'lep1phi', lep1phi, 'lep1phi/F' )
    br_lep1m   = tree.Branch( 'lep1m'  , lep1phi, 'lep1m/F'   )

    # track the time
    start_time = time.clock()

    n_entries = tree.GetEntries()
    i = 1
    for entry in tree:
        # show some progress
        if i % 1000 ==0: print("   processing event {:8d}/{:d} [{:5.0f} evts/s]".format(i, n_entries, i/(time.clock()-start_time)))

        if len(entry.leppT)<1:
            lep1pT[0]  =-999
            lep1eta[0] =-999
            lep1phi[0] =-999
            lep1m[0]   =-999
        else:
            lep1pT[0]  =entry.leppT[0]
            lep1eta[0] =entry.lepeta[0]
            lep1phi[0] =entry.lepphi[0]
            lep1m[0]   =0


        # fill new branches
        br_lep1pT.Fill()
        br_lep1eta.Fill()
        br_lep1phi.Fill()
        br_lep1m.Fill()
        i += 1

    # write augmented tree to original file
    tree.Write("", ROOT.TObject.kOverwrite)

    t.Close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='flatten/augment ntuples')
    parser.add_argument('--inputfile', help='input file to skim')
    args = parser.parse_args()

    augment_rootfile(args.inputfile)
