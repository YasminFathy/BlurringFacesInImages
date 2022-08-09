'''
This file is to use deface lib to blurring faces in images
Yasmin Fathy; Fathy.Yasmin@gmail.com
'''


import sys
import subprocess
import pkg_resources
import os


try:
    # make sure to install required libs for deface
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

for img in os.listdir(imgs_path):
    try:
        if img.endswith(".png"):
            os.system('deface '+img)

    except Exception as e:
        print("Can't convert: ", ex.message)
