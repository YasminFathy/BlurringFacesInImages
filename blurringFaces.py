'''
This file is to use deface lib to blurring faces in images
Yasmin Fathy; Fathy.Yasmin@gmail.com
'''


import sys
import subprocess
import pkg_resources
import os


try:
    required_libs = {'imageio', 'ffmpeg', 'deface'}
    installed_libs = {pkg.key for pkg in pkg_resources.working_set}
    missing_libs = required_libs - installed_libs

except Exception as ex:
    print("Error install required lib!", ex.message)

if missing_libs:
    # run pip in python3 as a subprocess
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install', *missing_libs])

# loop for folder contains imgs to be blurred and store output imgs at same dir with same name including _anonymized
imgs_path= "BlurringFaces/imgs"
ext = ".jpeg"
# ext = ".png"
threshold = "0.2"  # Default: 0.2
imgs = [os.path.abspath(os.path.join(imgs_path,i)) for i in os.listdir(imgs_path)]
for img in imgs:
    print(img)
    try:
        if img.endswith(ext) and 'anonymized' not in img:
            os.system('deface ' +img +' --thresh '+ threshold)

    except Exception as ex:
        print("Can't convert: ", ex.message)
