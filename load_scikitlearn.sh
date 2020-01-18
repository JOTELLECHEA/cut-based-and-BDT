#!/bin/bash

shopt -s expand_aliases

export ATLAS_LOCAL_ROOT_BASE="/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase"
alias setupATLAS="source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh"

setupATLAS

arch="x86_64-slc6-gcc49-opt"
LCG="85swan2"

source /export/home/mhance/students/jesse/lcgenv.sh

lsetup "lcgenv -p LCG_${LCG} ${arch} pyanalysis"

$ SHELL
