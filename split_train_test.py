import os
import pathlib
import shutil
import numpy as np


source1 = "./"
dest11 = "./val"
for root, dirs, files in os.walk("."):
     for dir in dirs:
      files = os.listdir(dir)
      newdir = dest11 + '/' + dir 
      pathlib.Path(newdir).mkdir(parents=True, exist_ok=True) 
      for f in files:
        if np.random.rand(1) < 0.2:
         shutil.move(source1 + '/' + dir + '/'+ f, dest11 + '/' + dir + '/'+ f)