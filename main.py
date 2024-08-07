import tkinter
import os
import time

root = tkinter.Tk(screenName="soundboard")

#Before any of you try to "optimize" this code dont forget to update the total hours you wasted
# Total hours wasted: 1 

programrootfoldername = "programoftesting"
prompt = "This app wasnt found in your computer would you like to install"
prompt2 = "This app was found in your computer would you like to Repair or Uninstall"
prompt3 = "Hello would you like to scan your pc for this app?"
firsttext = tkinter.Label(root, text=prompt3)
firsttext.pack()
yes = "Yes"
no = "No"
programcontent = "yourptogramsstuffhere"
installprompt = "İnstall"

def scan():
    os.chdir("C:/Program Files")
    stuff = os.listdir("./")
    if programrootfoldername in stuff:
        firsttext.config(text=prompt2)
        choice1.config(text="Repair", command=repair)
        choice2.config(text="Uninstall",command=uninstall)
    else:
        firsttext.config(text=prompt)
        choice2.config(command = notoinstall)
        choice1.config(command=install, text=installprompt)
def install():
    os.makedirs(f"./{programrootfoldername}")
    os.chdir(f"./{programrootfoldername}")
    with open("main.py","w") as file:
        starttime = time.time()
        firsttext.config(text=f"currently installing time:{starttime}")
        file.write(programcontent)
        stoptime = time.time()
        firsttext.config(text=f"writing complete total time spent:{stoptime}")
    with open("main.py", "r") as file:
        starttime = time.time()
        content = file.read()
        if programcontent == content:
            stoptime = time.time()
            firsttext.config(text=f"file integrity verified please dont close this window total time spent:{stoptime}")
            choice2.destroy()
            choice1.destroy()
            time.sleep(1)
            exit(1)
        else:
            stoptime = time.time()
            firsttext.config(text=f"the contents of the file was not the same written on it please check your antivirus or any other app that might affect the install total time spent:{stoptime}")
            choice2.destroy()
            choice1.destroy()
            exit(1)
def noscan():
    firsttext.config(text="cant continue if you dont let us scan", padx=30, pady=30)
    choice1.destroy()
    choice2.destroy()
    firsttext.update_idletasks()
    time.sleep(2)
    exit(1)
def notoinstall():
    choice1.destroy()
    choice2.destroy()
    firsttext.config(text="there isnt anything we can do if you want to repair but you cant get past here run this again and select install")
    firsttext.update_idletasks()
    time.sleep(5)
    exit(1)
def uniinstall():
    os.chdir(f"C:/Program Files/{programrootfoldername}")
    dirs = os.listdir("./")
    for hir in dirs:
        os.remove(f"./{hir}")
    with open("main.py","w") as file:
        starttime = time.time()
        firsttext.config(text=f"currently installing time:{starttime}")
        file.write(programcontent)
        stoptime = time.time()
        firsttext.config(text=f"writing complete total time spent:{stoptime}")
    with open("main.py", "r") as file:
        starttime = time.time()
        content = file.read()
        if programcontent == content:
            stoptime = time.time()
            firsttext.config(text=f"file integrity verified please dont close this window total time spent:{stoptime}")
            choice2.destroy()
            choice1.destroy()
            time.sleep(1)
            exit(1)
        else:
            stoptime = time.time()
            firsttext.config(text=f"the contents of the file was not the same written on it please check your antivirus or any other app that might affect the install total time spent:{stoptime}")
            choice2.destroy()
            choice1.destroy()
            exit(1)
def abort():
    choice1.destroy()
    choice2.destroy()
    firsttext.config(text="Abroting...")
    exit(1)
def uninstall():
    os.chdir(f"C:/Program Files/{programrootfoldername}")
    starttime = time.time()
    firsttext.config(text=f"uninstalling time:{starttime}")
    dirs = os.listdir("./")
    for hir in dirs:
        os.remove(f"./{hir}")
    os.chdir("C:/Program Files")
    os.rmdir(f"./{programrootfoldername}")
    stoptime = time.time()
    firsttext.config(text=f"task completed total time spent{stoptime}")
    exit(1)
def repair():
    os.chdir(f"C:/Program Files/{programrootfoldername}")
    firsttext.config(text="Please note that any informaiton in this aplications directory will be removed with no way of getting back please backup anything needed do you still want to contunuie")
    choice2.config(command=abort,text=no)
    choice1.config(command=uniinstall, text=yes)
choice1 = tkinter.Button(root, text=yes,command=scan)
choice2 = tkinter.Button(root,text=no,command=noscan)
choice1.pack();choice2.pack()
root.mainloop()