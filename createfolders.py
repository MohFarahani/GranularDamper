import os
import shutil
import subprocess
import re
amp=[0.010,0.020,0.030,0.040,0.050]

for i in range(0,len(amp)):
    dir_name = "amplitude= "+str(amp[i])
    if not os.path.exists(dir_name):
           os.mkdir(dir_name)
    os.chdir(dir_name)
    if not os.path.exists("post"):
           os.mkdir("post")
    os.chdir("..")

for i in range(0,len(amp)):
    dir_name = "amplitude= "+str(amp[i])
    shutil.copy("in.damper",dir_name)
    shutil.copy("test_vtk.py",dir_name)
    shutil.copy("test_plotview.py",dir_name)

sourceCommand1 = "fix move all move/mesh mesh cad wiggle amplitude 0.0 0.01 0.0 period 0.1"
sourceCommand2 = "mesh/surface file box/"
replaceCommand2 = "mesh/surface file ../box/" 

for i in range(0,len(amp)):
    dir_name = "amplitude= "+str(amp[i])
    os.chdir(dir_name)
    replaceCommand1 = "fix move all move/mesh mesh cad wiggle amplitude 0.0 "+ str(amp[i]) +" 0.0 period 0.1"
    file = open("in.damper",'r')
    file_string = file.read()
    file.close()
    
    file_string = (re.sub(sourceCommand1, replaceCommand1, file_string))
    file_string = (re.sub(sourceCommand2, replaceCommand2, file_string))

    file = open("in.damper",'w')
    file.write(file_string)
    file.close()

    os.chdir('..')

for i in range(0,len(amp)):
    dir_name = "amplitude= "+str(amp[i])
    os.chdir(dir_name)
    mpicmd = 'mpirun -n 7 liggghts < in.damper' 
    subprocess.call(mpicmd,shell=True)    
    os.chdir('..')


