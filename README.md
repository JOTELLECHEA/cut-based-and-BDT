# ttHH-Research
1. Programs Descriptions
   - lepvec_Pt.py
     >Cut base analysis.
   - chisquare.py
     >Script that test gives all permutations of b tag jets for chisquare.
   - MVA.py
     >Script that uses a MutiVariate Algorithm (MVA)/Boosted Decision Tree(BDT).
   - ROC.py
     >Script that recreates ROC curve plots from the BDT.
   - add_SF_branches.py
     >Script that makes a new ROOT file; is used to flatten vectors.
2. Programs Parser Variables/ Outputs
   - lepvec_Pt.py
     >`--x=i` where  i = 1-4: ttHH,ttbb,ttH,ttZ.
     
     >`--help` brings up help.
   - chisquare.py
     >N/A
   - MVA.py
     >`--branch=i` where i = njets,lep,...
     
     >Output file is `data_ROC_Curve.csv`.
   - ROC.py
     >Output is tmp and can be save in format that is needed.
   - add_SF_branches.py
     >`--inputfile='****.root'`.
     
     >`--help` brings up help.
     
     >Creates new ROOT file as `new_****.root`.
  
