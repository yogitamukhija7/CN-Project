import subprocess
import os
import getpass
def connection():
    path = r"core\\login.bat"
    p = subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
    stdout,stderr = p.communicate('dir c:\\')
    print stdout
def disconnect():
    path = r"core\\delete.bat"
    p = subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
    stdout,stderr = p.communicate('dir c:\\')

def create_file(enrl):
    path = r"v:\\login\\"+enrl+".txt"
    fobj = open(path,"w")
    fobj.close()
def delete_file(enrl):
    path = r"v:\\login\\"+enrl+".txt"
    os.remove(path)
def online_users():
    path=r"v:\\login"
    user_list = os.listdir(path)
    for user in user_list:
        print user[:-4]
def check_localdb():
    path = r"C:\\Users\\"+getpass.getuser()+"\\Documents\\yogitakijai"
    if (not os.path.exists(path)):
        os.makedirs(path)
    path = path + "\\urchats"
    if (not os.path.exists(path)):
        os.makedirs(path)
    chat_list = os.listdir(path)
    for user in chat_list:
        print user[:-4]
    
def menu():
    enrl = raw_input("Enter enrollmant number")
    enr2 = raw_input("Who do u want to chat with")
    
    if(not os.path.exists(r"v:\\login")):
        os.makedirs(r"v:\\login")
    create_file(enrl)
    online_users()
    check_localdb()
    delete_file(enrl)
    chat(enrl,enr2)
    check_newmsg(enrl)
    raw_input()

    
def check_newmsg(enr1):
    path=r"v:\\chat"
    unread_list=os.listdir(path)
    for users in unread_list:
        if enr1 in users:
            print users
            path=path+"\\"+users
            with open(path+"\\timeline.txt") as f:
                msg=f.readlines()
                print msg
    



def chat(enr1,enr2):
    path=r"v:\\chat"
    if(not os.path.exists(path)):
        os.makedirs(path)
    max_enr=max(enr1,enr2)
    min_enr=min(enr1,enr2)
    path = path+"\\"+min_enr+"_"+max_enr
    if(not os.path.exists(path)):
        os.makedirs(path)
        

   
    
    
    
    
connection()
menu()

disconnect()
        
