import os
import shutil
path="C:/Users/LENOVO/OneDrive/Desktop/WhiteHatJr.Project/newPythonFolder/"
list_File = os.listdir(path)
for file in list_File:
    name, ext= os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
        