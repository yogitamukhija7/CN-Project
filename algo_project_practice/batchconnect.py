import subprocess
import os

path = r"batch_files\\command.bat"
p=subprocess.Popen([path,"14103151","uranidiot"],stdout=subprocess.PIPE,shell=True)
stdout,stderr=p.communicate('dir c:\\')
print stdout

