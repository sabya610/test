import os
import tarfile
output_tar_file="organize.py"
source_path="/root/scripts_test/uploads"

def create_tar(source_path,output_tar_file):
    """
     acepts 2 paramters source path directory  and tar file name
    """
    out=output_tar_file.split('.')[0]
    file_t=os.path.join(source_path,out)+".tar"
    with tarfile.open(file_t,'w') as tar:
       tar.add(source_path)

create_tar(source_path,output_tar_file)
