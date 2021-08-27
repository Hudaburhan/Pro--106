import os
import shutil
source="C:/Users/LENOVO/OneDrive/Desktop/WhiteHatJr.Project/newPythonFolder/py"
destination="C:/Users/LENOVO/OneDrive/Desktop/WhiteHatJr.Project/"
list_File = os.listdir(source)
for file in list_File:
    print(file)
    shutil.copy((source+'/'+file), destination)