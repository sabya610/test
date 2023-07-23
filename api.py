from flask import Flask,request,jsonify
import os
import tarfile
import logging

app = Flask(__name__)

# Configure logging
#logging.basicConfig(level=logging.INFO)  # Set the desired log level
# Configure logging to write to a file
logging.basicConfig(filename='flask_app.log', level=logging.INFO)

# This endpoint will add two numbers

@app.route('/add',methods=['POST'])
def add_numbers():
   data=request.get_json()
   a=data.get('a',0) 
   b=data.get('b',0)
   result= a + b
   return jsonify({'result':result})

# This endpoint  will multiple two numbers

@app.route('/multiply',methods=['POST'])
def multiply_numbers():
   num1=int(request.args.get('num1',0))
   num2=int(request.args.get('num2',0))
   result = num1 * num2
   return jsonify({'result':result})

# Set the upload folder path
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# This endpoint will upload file and tar in uploads folder


@app.route('/upload',methods=['POST'])
def upload_files():
    if 'file' not in request.files:
       print(f"The request {request.files}")
       return jsonify({'message':f"file is not present {request.files}"}),400

    file=request.files['file']
    #print(f"The file entries {file}")
    
    if file.filename == '':
       return jsonify({'error':'No selected file'}),400
    

    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
    #file_tar=file.filename
    tar_path=UPLOAD_FOLDER
    create_tar(tar_path,file.filename)
    return jsonify({'message':'File uploaded and tar created successfully'})


# This function wirll create tar of  file in the  path 

def create_tar(source_path,output_tar_file):
    """
     acepts 2 paramters source path directory  and tar file name 
    """
    out=output_tar_file.split('.')[0]
    file_t=os.path.join(source_path,out)+".tar"
    with tarfile.open(file_t,'w') as tar:
       tar.add(source_path)


if __name__ == '__main__':
   UPLOAD_FOLDER = '/root/scripts_test/uploads'

   if not (os.path.exists(UPLOAD_FOLDER)):
      os.makedirs(UPLOAD_FOLDER)
   app.run(debug=True)
      
  
