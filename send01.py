import os
import sys
import shutil
import subprocess
import split
import time
import zipfile
import getpass
#import datetime


def create_dir(username,reciever,password):
    os.system(r"core\\deleteall.bat")
    path = r"net use v: \\fileserver2.pdc.jiit\14103129 terabaap /USER:14103129"
    p = subprocess.Popen(path, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate('dir c:\\')
    print stdout
    path = r"v:\\abcd\\file_sending\\"+username+"_"+reciever
    if(not os.path.exists(path)):
        os.makedirs(path)
    path1 = path + "\\log_file"
    if(not os.path.exists(path1)):
        os.makedirs(path1)
    path2 = path + "\\data_dump"
    if(not os.path.exists(path2)):
        os.makedirs(path2)
    return [path1,path]
    #os.system(r"core\\deleteall.bat")

def create_zip(reciever):
    #create folder in local drive
    path = r"C:\\Users\\"+getpass.getuser()+"\\Documents\\"+reciever+"_data"
    if(not os.path.exists(path)):
        os.makedirs(path)
    path1 = path + "\\data_dump"
    if(not os.path.exists(path1)):
        os.makedirs(path1)
    
    o_file = raw_input("Enter path of folder")
    file_name = list(o_file.split("\\"))
    filename = file_name[-1]
    path = path + "\\" + filename
    shutil.make_archive(path,"zip",o_file)
    path = path+".zip"
    #split into files size <=90 mb
    parts = split.fsplit(path,path1)
    return [parts,filename,path]

def check_user(path,reciever):
    #watch = datetime.datetime.now()
    counter = 0
    status = False
    while(counter <= 60):
        counter += 1
        time.sleep(1)
        path1 = path + "\\" + reciever + ".txt"
        if(os.path.exists(path1)):
            status = True
            break
    return status

def join(fromdir, tofile):
    readsize = 1024
    output = open(tofile, 'wb')
    parts  = os.listdir(fromdir)
    parts.sort(  )
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj  = open(filepath, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )


def upload(username,reciever,parts):
    tpath = r"v:\\abcd\\file_sending\\"+username+"_"+reciever+"\\data_dump"
    upath = r"v:\\abcd\\file_sending\\"+username+"_"+reciever+"\\log_file\\upload.txt"
    rpath = r"v:\\abcd\\file_sending\\"+username+"_"+reciever+"\\log_file\\"+reciever+".txt"
    fpath = r"C:\\Users\\"+getpass.getuser()+"\\Documents\\"+reciever+"_data"+"\\data_dump"
    files = os.listdir(fpath)
    files.sort()
    uploaded = 0
    while(uploaded < parts):
        uploaded += 1
        print "uploading part ",uploaded
        temp_path = fpath + "\\" + files[uploaded-1]
        shutil.copy2(temp_path,tpath)
        
        fob = open(upath,"w")
        fob.write(str(uploaded))
        fob.close()
        sub_status = True
        print "Waiting for file to be downloded"
        while(sub_status):
            print "waiting for reciever to download"
            time.sleep(1)
            fobj = open(rpath)
            for line in fobj:
                n = line.rstrip()
                break
            fobj.close()
            if(int(n) == uploaded):
                sub_status = False


def decompress(final_path,file_name):
    zfile = zipfile.ZipFile(final_path)
    p = r"C:\\Users\\"+getpass.getuser()+"\\Downloads\\"+file_name
    zfile.extractall(p)
    time.sleep(1)

def download(username,password,sender):
    fpath =r"v:\\abcd\\file_sending\\"+sender+"_"+username+"\\data_dump"
    tpath =r"C:\\Users\\"+getpass.getuser()+"\\Downloads\\data_dump1"
    final_path = r"C:\\Users\\"+getpass.getuser()+"\\Downloads"
    upath =r"v:\\abcd\\file_sending\\"+sender+"_"+username+"\\log_file\\upload.txt"
    rpath =r"v:\\abcd\\file_sending\\"+sender+"_"+username+"\\log_file\\"+username+".txt"
    spath =r"v:\\abcd\\file_sending\\"+sender+"_"+username+"\\log_file\\"+sender+".txt"
    fobj1 = open(spath)
    for line in fobj1:
        n = line.rstrip()
        break
    fobj1.close()
    l_1 = list(n.split(" "))
    parts = l_1[1]
    file_name = l_1[0]
    final_path = final_path + "\\" + file_name + ".zip"
    print file_name,parts
    if(not os.path.exists(tpath)):
        os.makedirs(tpath)
    downloaded = 0
    while(True):
        if(downloaded == int(parts)):
            break
        while(not os.path.exists(upath)):
            pass
        time.sleep(0.2)
        fob = open(upath)
        for line in fob:
            n = line.rstrip()
            break
        fob.close()
        if(int(n) == downloaded+1):
            time.sleep(0.1)
            while(True):
                file_1 = os.listdir(fpath)
                if(len(file_1)!=0):
                    break
            #file_1 = os.listdir(fpath)
            fpath1 = fpath +"\\"+ file_1[0]
            print "Downloading part",downloaded+1
            shutil.copy2(fpath1,tpath)
            downloaded += 1
            print "downloaded"
            os.remove(fpath1)
            fob = open(rpath,"w")
            fob.write(str(downloaded))
            fob.close()
            print "updated"
            
        else:
            print "Waiting for new file to be uploaded"
    print "Joining parts"
    join(tpath,final_path)
    print "Done joining"
    shutil.rmtree(tpath)
    print "Decompressing File"
    decompress(final_path,file_name)
    return final_path
    print "Done dona done"
        
def recieve(username,password,sender):
    os.system(r"core\\deleteall.bat")
    path = r"net use v: \\fileserver2.pdc.jiit\14103129 terabaap /USER:14103129"
    p = subprocess.Popen(path, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate('dir c:\\')
    print stdout
    path = r"v:\\abcd\\file_sending\\"+sender+"_"+username+"\\log_file\\"+username+".txt"
    fob = open(path,"w")
    string = "0"
    fob.write(string)
    fob.close()
    path1 = r"v:\\abcd\\file_sending\\"+sender+"_"+username+"\\log_file\\"+sender+".txt"
    if(os.path.exists(path1)):
        print "Sender is ready"
        fp = download(username,password,sender)
    else:
        print "sender not found"
    return fp


def mainf(username,password):
    print "1 - SEND"
    print "2 - RECIEVE"
    print "3 - Go-Back"
    ans = int(raw_input("Enter Your Choice"))
    if(ans == 1):
        reciever = raw_input("Enter recievers enrolment number")
        local_db = r"C:\\Users\\"+getpass.getuser()+"\\Documents\\"+reciever+"_data"
        p1 = create_dir(username,reciever,password)
        path1 = p1[0]
        l = create_zip(reciever)
        path11 = path1 + "\\" + username + ".txt"
        fob = open(path11,"w")
        string = l[1] + " " + str(l[0])
        fob.write(string)
        fob.close()
        print "checking reciever"
        if(check_user(path1,reciever)):
            print "reciever found"
            print "Sending Files: "
            upload(username,reciever,l[0])
        else:
            print "reciever not found"
        time.sleep(1)
        shutil.rmtree(p1[1])
        shutil.rmtree(local_db)
        #wait until user gets logged in with same id
        #compress folder
        #split folder
        #send according to size
    if(ans==2):
        sender = raw_input("Enter senders enrollment number")
        f_p = recieve(username,password,sender)
        os.remove(f_p)
        #recieve pasword file
        #log in with senders id
        #decompress folder after transfer is complete
    if(ans==3):
        exit(0)

mainf("14103116","abcd")
os.system(r"core\\deleteall.bat")
