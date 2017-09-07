import sqlite3
import subprocess
import os
import shutil
import messagebot
import random
import temp1
def loginfs(username,password):
    os.system(r"C:\Users\dell\Desktop\project\batch_files\delete_connection.bat")
    path = r"C:\Users\dell\Desktop\project\batch_files\login.bat"
    p = subprocess.Popen(path, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate('dir c:\\')
    print stdout
def main_connection():
    print "hello"
    path = r"C:\Users\dell\Desktop\project\batch_files\login.bat"
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
    raw_input()

main_connection()
#raw_input()
#loginfs("a","b")
#raw_input()
temp1.loginfs("14103147","chien")
#raw_input()
conn=sqlite3.connect('V:\scheck.db')
print conn
curs=conn.cursor()

def downloading_options():
    curs.execute("SELECT filename FROM DATA")
    data=curs.fetchall()
    #conn.commit()
    print "Downlaoding Options"
    for row in data:
        print data
    choice=raw_input("ENter y to download")
    if choice=='y' or choice =='Y':
        src=r"v:\ab"
        dest=r"C:\\Users\Shubhi\Desktop\ff"
        shutil.copytree(src,dest)
    else:
        return

def chat(sender_username):
    sender_sm_pass=raw_input("Enter ur fileserver password")
    curs.execute("UPDATE USER set sm_pass=? where username=?",(sender_sm_pass,sender_username))
    receiver_username=raw_input("Enter the enrollment no of the person u want to chat with")
    curs.execute("SELECT online FROM USER WHERE username=?",(receiver_username,))
    data=curs.fetchall()
    #print data
    if data==1:
        print "User is online"
    else:
        print "User is not online"
    
    


def update_online_status(f,username):
    print "i m here"
    curs.execute("UPDATE User SET online =? where username=?",(f,username))
                 
def login():
    #main_connection()
    username=raw_input("Enter your username")
    password=raw_input("Enter your password")
        
    curs.execute("SELECT username,password FROM USER")
    data=curs.fetchall()
    f=0
    for row in data:
        if(row[0]==username and row[1]==password):
            print "Log in successful"
            f=1
            update_online_status(f,username)
            print "1. Downloading options"
            print "2. Chat"
            print "3.Exit"
           
            choice=int(raw_input("Enter choice"))
            if choice==1:
                       downloading_options()
            elif choice==2:
                       chat(username)
            elif choice==3:
                f=0
                update_online_status(f,username)

    if f==0:
        print "Wrong password"
        
    
        
        
        


    

def delete_connection():
    path = r"batch_files\\delete_connection.bat"
    p=subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
    stdout,stderr=p.communicate('dir c:\\')
    print stdout

def delete_connection1():
    path = r"net use * /delete /y"
    p=subprocess.Popen(path,stdout=subprocess.PIPE,shell=True)
    stdout,stderr=p.communicate('dir c:\\')
    print stdout
def copy_file(username,password):
    delete_connection()
    
    raw_input()
    delete_connection1()
    raw_input()
    #path = r"batch_files\\fileserver_connection.bat"
    path = r"C:\Users\Shubhi\Desktop\project\batch_files\fslogin.bat"
    p=subprocess.Popen([path,"chien","14103147"],stdout=subprocess.PIPE,shell=True)
    stdout,stderr=p.communicate('dir c:\\')
    print stdout
    raw_input()
    
    print "Opening File Server : "
    main_path = r"v:"
    depth=0
    main_list=[]
    main_list.append(main_path)
    status=1
    while status==1:
        for i in main_list:
            print i
        counter = 1
        l = os.listdir(main_path)
        for a in l:
                print counter,
                if(os.path.isdir(main_path + "\\" + a)):
                    print "+",
                print a
                counter+=1
        print counter , "Exit"
        ans=int(raw_input("Enter choice:"))
        if(ans==counter):
            status=0
        elif(ans==0):
            if(depth!=0):
                main_path=main_connectionn_list[depth-1]
                depth -=1
                main_list=main_list[:-1]
        
        else:
           
            main_path1= main_path + "\\" + l[ans-1]
            print main_path1
            if(os.path.isfile(main_path1)):
                print "Do you wish to download file: ? (y/n)"
                ans1=raw_input()
                if(ans1=='y'):
                    shutil.copy2(main_path1,r"C:\Users\Shubhi\Documents\sm")
                    print "Press any key to continue"
            else:
                depth+=1
                main_path=main_path1
                main_list.append(main_path)
                print "Press c to copy"
                ans2=raw_input()
                des = r"C:\\Users\\Shubhi\\Documents\\sm" + l[ans-1]
                if(ans2=='c'):
                    shutil.copytree(main_path,des)
                


def create_table():
    print "create table mei hai"
    curs.execute('CREATE TABLE IF NOT EXISTS User(name TEXT,username TEXT primary key,password TEXT,batch TEXT,branch TEXT,year int,mobileno string,email TEXT,gender TEXT,sec1 TEXT,sec2 REAL,online int,sm_pass TEXT)')


def insert_data_user(name,username,password,batch,branch,year,mobileno,email,gender,sec1,sec2):
    print "insert data mei hai"
    online=0
    sm_pass=""
                       
    try:
                       
        curs.execute("INSERT INTO User(name,username,password,batch,branch,year,mobileno,email,gender,sec1,sec2,online,sm_pass) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,username,password,batch,branch,year,mobileno,email,gender,sec1,sec2,online,sm_pass))
        print "Sign up succesful. Please login now."
        login()
    except:
        print "Error"                  
                 
            
def sign_up():
    
    create_table()
    name=raw_input("Enter your name")
    username=raw_input("ENter username")
    curs.execute("SELECT USERNAME FROM USER")
    user_exist=curs.fetchall()
    for row in user_exist:
         if username in row:
            print "You have already signed in."
            return
    
    password=raw_input("Enter your password")
    batch=raw_input("ENter batch")
    branch=raw_input("ENter branch")
    year=raw_input("ENter year")
    mobileno=raw_input("Enter mobile no")
    if mobileno== raw_input("Re-enter mobile no"):
        otp = random.randint(0,100)
        text = "OTP is: " + str(otp)
        messagebot.send_msg(mobileno,text)
        if(int(raw_input('Enter OTP:')) != otp):
            mobileno = 0
    gender=raw_input("Enter your gender")
    email=raw_input("ENter email")
    sec1=raw_input("Ur first mobile phone?")
    sec2=raw_input("ur first sem cgpa")
    insert_data_user(name,username,password,batch,branch,year,mobileno,email,gender,sec1,sec2)
    
    
    
    
    

def otp_check():
    otp=random.randint(0,100)
    text="OTP is: "+str(otp)
    messagebot.send_msg("8130878090",text)
    if(int(raw_input('Enter OTP: '))!=otp):
        return 0
    return 1

def change_pass():
    username=raw_input("Enter your username")
    old_password=raw_input("Enter old password")
    curs.execute("SELECT * FROM USER WHERE username = ? and password =?",(username,old_password))
    data=curs.fetchall()
    if (data):    
        new_password=raw_input("Enter new password")
        if(otp_check()):
            curs.execute("UPDATE USER SET password =? where username =? and password =?",(new_password,username,old_password))
            conn.commit()
            print "Password changed successfully."
        else:        
            print "Wrong OTP. Try Again"
            return
    else:
        print "Username or Password does not match. Try Again"
        return
def change_details():
    status=1
    while status == 1:
        print "1. Change Password"
        print "2. Change Mobile No"
        print "3. Change Email"
        print "4. Go Back"
        choice=int(raw_input("Enter your choice"))
        if choice == 1:
            change_pass()
        elif choice==2:
            new_mobileno=int(raw_input("Enter new Mobile No"))
        elif choice==3:
            new_email=raw_input("Enter new email")
        elif choice==4:
            status=0
            return

def send_students_msg():
    year=raw_input("Enter year")
    batch=raw_input("ENter batch")
    curs.execute("SELECT mobileno FROM USER WHERE year =? and batch =?",(year,batch))
    data=curs.fetchall()
    #msg=raw_input("ENter your message")
    for row in data:
        messagebot.send_msg(row,msg)

def get_students():
    year=raw_input("Enter year")
    branch=raw_input("Branch")
    batch=raw_input("batch")
    
    if batch=="ALL":
        curs.execute("SELECT username FROM USER where year =? and branch =?",(year,branch))
        data=curs.fetchall()
        conn.commit()
        print data
    else:
        curs.execute("SELECT username FROM USER WHERE year =? and branch =? and batch =?",(year,branch,batch))
        data=curs.fetchall()
        conn.commit()
        print data


    


status=1
while status==1:
    print"Menu"
    print "1. Login to Fileserver"
    print "2. Sign Up"
    print "3. Change Details"
    print "5. Exit"
    print "4. Copy material from fileserver"
    print "6. Send message"
    print "7. Get students"
    print "8. Chat"
    print " Enter ur choice"
    choice=int(raw_input())
    if choice==1:
      #  main_connection()
        login()
    if choice ==2:
        #main_connection()
        sign_up()
        
        
        
        
        
    if choice==3:
        change_details()
    if choice==5:
        status=0
        
    if choice==4:
        username=raw_input("Enter your username")
        password=raw_input("Enter your password")
        copy_file(username,password)
    if choice==6:
        send_students_msg()
    if choice==7:
        get_students()
    if choice==8:
        chat()
conn.commit()
curs.close()
conn.close()
delete_connection()

