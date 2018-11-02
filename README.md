# util
Utility scripts for working with datasets:

split_train_test.py: small script to split a multinomial directory dataset into train and val. Full recursion is provided. Set the desired split ratio directly within the script (change 0.2 to whatever is desired). Place script into dir with subdirectories, and run:  python3 split_train_test.py

Starting dir structure should be as follows:

dataset
 --subdir1
 --subdir2
 split_train_test.py
 
 
 Script will create
  dataset
   --subdir1
   --subdir2
   --....
   --val
    ---subdir1
    ---subdir2
  split_train_test.py
