<img src="https://github.com/JOTELLECHEA/Exploring-ttHH-with-BDT/blob/master/Exploring_ttHH_with_BDT.png">

## Programs Descriptions
   1. lepvec_Pt.py
      -Cut base analysis.
   2. chisquare.py
      -Script that test gives all permutations of b tag jets for chisquare.
   3. MVA.py
      -Script that uses a MutiVariate Algorithm (MVA)/Boosted Decision Tree(BDT).
   5. RocCurve.py
      -Script that recreates ROC curve plots from the BDT.
   6. add_SF_branches.py
      - **SF Branch**: The script calculates and adds SF branches to your ROOT files. These SF branches contain correction factors used to mitigate systematic errors and enhance the precision of data analysis.
      
      - **Efficient Processing**: The script efficiently iterates through each event in the ROOT file, calculates SF values, and updates the corresponding branches. It also tracks the processing time and displays progress, ensuring a smooth augmentation process.


## Programs Parser Variables/ Outputs

- lepvec_Pt.py
  >`--x=i` where  i = 1-4: ttHH,ttbb,ttH,ttZ.
  
  >`--help` brings up help.
- chisquare.py
  >N/A
- MVA.py
  >`--branch=i` where i = phase1-4
  
  >Output file is `ROC_data_file.csv'.
- RocCurve.py
  >`--file=i` where  i = ROC_data_phase1-4.csv.

  >Output is tmp and can be save in format that is needed.
- add_SF_branches.py
  >`--file='****.root'`.
  
  >`--help` brings up help.
  
  >Creates new ROOT file as `new_****.root`.



  
