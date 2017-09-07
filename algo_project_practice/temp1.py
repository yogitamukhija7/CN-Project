import shutil
import getpass
import os
import subprocess



def loginfs(username,password):
    os.system(r"core\\deleteall.bat")
    path = r"core\\fslogin.bat"
    p = subprocess.Popen([path,password,username], stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate('dir c:\\')
    print stdout
