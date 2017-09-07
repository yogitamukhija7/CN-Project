import sqlite3
import subprocess
import os

#p=r"V:\algo"
#os.makedirs(p)
conn=sqlite3.connect('V:\algo\exam.db')
curs=conn.cursor()
def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')

def data_entry():
    curs.execute("INSERT INTO stuffToPlot VALUES(145,'2016-01-01','Python',5)")
    conn.commit()
    curs.close()
    conn.close()


create_table()
data_entry() 
    
