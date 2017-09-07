import subprocess
import os
path=r"net use v: \\fileserver2.pdc.jiit\14103151 uranidiot /USER:14103151"
p=subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
stdout,stderr=p.communicate('dir c:\\')
print stdout

