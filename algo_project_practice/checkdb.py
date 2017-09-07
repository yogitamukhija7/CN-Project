import sqlite3
import subprocess
import os

#p=r"V:\algo"
#os.makedirs(p)
conn=sqlite3.connect('check.db')
curs=conn.cursor()
def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS USER(username int, password TEXT)')

def data_entry():
    curs.execute("INSERT INTO USER VALUES('14103147','motog3')")
    curs.execute("INSERT INTO USER VALUES('14103151','rockon')")
    conn.commit()
   
def update():
    user="14103147"
    old_password="motog3"
    curs.execute("SELECT * FROM USER WHERE username =? and password=?",(user,old_password))
    details=curs.fetchall()
    if(details):
                 print"user exists"
                
    conn.commit()

def update_like():
    a="g3"
    curs.execute("SELECT * FROM USER WHERE password like ?",('%'+a+'%',))
    data=curs.fetchall()
    print data
    conn.commit()

def update1():
    ss="were"
    username="14103147"
    password="motog3"
    curs.execute("UPDATE USER SET password =? where username =? and password =?",(ss,username,password))
    conn.commit()
create_table()
#data_entry()
update1()
#update_like()
#data_entry() 
curs.close()
conn.close()
 
