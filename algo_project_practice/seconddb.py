import sqlite3
import datetime
import random
conn=sqlite3.connect('example.db')
curs=conn.cursor()
def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')

def data_entry():
    username=raw_input("Username")
    a=1
    b=2
    c='2014-2-3'
    curs.execute("INSERT INTO stuffToPlot(unix,datestamp,keyword,value) VALUES(?,?,?,?)",(a,c,username,b))
    conn.commit()
    curs.close()
    conn.close()


create_table()
data_entry() 
    
