import os
import shutil

def directory_organize(d_path):
   f_list = os.listdir(d_path)
   print(f"{f_list} is the files")
   for i in f_list:
      if os.path.isfile(os.path.join(d_path,i)):
         f_ext = i.split(".")[1] 
         print("The file extention {} and file name {} ".format(f_ext,f_list))
         n_path=os.path.join(d_path,f_ext)
         print(f"the {n_path} is the new path")
         if not os.path.exists(n_path):
            n_dir=os.makedirs(os.path.join(d_path,f_ext))
            # pass
         s_path=os.path.join(d_path,i) 
         print(f"The new {n_path} directory newly created nd file is {s_path}")
         d_path=os.path.join(d_path,n_path)
         print(f"the dest path is {d_path}")
         #shutil.move(s_path,d_path)	




dir_path="/root/testdir"
directory_organize(dir_path)
