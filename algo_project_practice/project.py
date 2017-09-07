import sqlite3
import subprocess
import os


path = r"batch_files\\login.bat"
p=subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
stdout,stderr=p.communicate('dir c:\\')
print stdout
    
def login(username,password):
    conn=sqlite3.connect('V:\ex.db')
    curs=conn.cursor()
    def create_table():
        curs.execute('CREATE TABLE IF NOT EXISTS User1(username TEXT primary key,password TEXT)')

    def data_entry():
        curs.execute("INSERT INTO User1(username,password) VALUES(?,?)",(username,password))
        conn.commit()
        curs.close()
        conn.close()


    create_table()
    data_entry() 

    

status=1
while status==1:
    print"Menu"
    print "1. Login to Fileserver"
    print "2. Change Password"
    print "3. Exit"
    print " Enter ur choice"
    choice=int(raw_input())
    if choice==1:
        username=raw_input("Enter your username")
        password=raw_input("Enter your password")
        login(username,password)
    if choice==2:
        new_password=raw_input("Enter new password")
        #change_pass(new_password)
    if choice==3:
        status=0
