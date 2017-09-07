import sqlite3
import subprocess
import os
import shutil

def main_connection():
    print "hello"
    path = r"C:\Users\Shubhi\Desktop\project\batch_files\login.bat"
    p = subprocess.Popen(path, stdout=subprocess.PIPE, shell=True)
    stdout,stderr=p.communicate('dir c:\\')
    print stdout
    if "The command completed successfully." not in stdout:
        path1 = r"net use v: \\fileserver2.pdc.jiit\14103147 chien /USER:14103147"
        p = subprocess.Popen(path, stdout=subprocess.PIPE, shell=True)
        stdout,stderr=p.communicate('dir c:\\')
        print stdout
        if "The command completed successfully." not in stdout:
            os.system(path)
        
    #os.system(path)
main_connection()
conn=sqlite3.connect('V:\example12.db')
print conn
curs=conn.cursor()

def create_table():
    curs.execute("CREATE TABLE IF NOT EXISTS DATA(filename TEXT,owner int,fileid INTEGER primary key AUTOINCREMENT ,extension TEXT)")
    #conn.commit()


#path=r"C:\Users\Shubhi\Desktop\ab"
#mainpath=r"v:\\"+username
#shutil.copytree(path,mainpath)
#print "Uploaded to sm succesfully"
#create_table()
#insert_table("addicted","username")
    
def after_login():
    username="14103147"
    curs.execute("SELECT * FROM DATA")
    data=curs.fetchall()
    print "Downloading options"
    for row in data:
        print data

def insert_table(filename,owner,extension):
    a=1
    try:
        curs.execute("INSERT INTO DATA(filename,owner,extension) VALUES(?,?,?)",(filename,owner,extension))
    except:
        print "Error"

def login(username,password):
    #main_connection()
    curs.execute("SELECT username,password FROM USER")
    data=curs.fetchall()
    f=0
    for row in data:
        if(row[0]==username and row[1]==password):
            print "Log in successful"
            f=1
            create_table()
            insert_table("addicted","14103151","mp3")
            after_login()
            

    if f==0:
        print "Wrong password"

print "1. LOgin"
status=1
while status:
    login("14103147","motog3")
    status=0

conn.commit()
curs.close()
conn.close()
