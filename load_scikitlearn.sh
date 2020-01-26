#!/bin/bash

setupATLAS

arch="x86_64-slc6-gcc49-opt"
LCG="85swan2"

source /export/home/mhance/students/jesse/lcgenv.sh

lsetup "lcgenv -p LCG_${LCG} ${arch} pyanalysis"

