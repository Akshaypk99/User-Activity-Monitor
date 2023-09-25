import os 
from os import stat, remove
import shutil
import pyAesCrypt
import tkinter as tk
from tkinter import filedialog
from tkinter import *


def readfile():
    global cache
    path = os.getcwd()
    cache = os.path.join(path,'cache')
    if not os.path.exists(cache):
        os.makedirs(cache)

    #---------------------selecting file-----------------------
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ((".aes files","*.aes"),("all files","*.*")))
    encFileSize = stat(filename).st_size
    #----------decrypttion------------------
    bufferSize = 64 * 1024
    password = "infolks_techies"
    with open(filename, "rb") as fIn:
        try:
            with open(os.path.join(cache,"dataout.txt"), "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
            print('Access Denied')

def decryption():

    global cache
    readfile()    
    with open(os.path.join(cache,"dataout.txt"),'r') as tfile:
        global data
        data = tfile.readlines()
    # view = threading.Thread(target=viewdata)
    # view.start()
    try:
        remove(os.path.join(cache,"dataout.txt"))
        shutil.rmtree(cache)
    except:
        pass
    viewdata()

def viewdata():
    global data
    root = tk.Tk()
    root.title('WTM || SUMMARY')
    root.geometry("600x500")
    root.resizable(False, False) 
    S = tk.Scrollbar(root)
    T = tk.Text(root, font=("times new roman",15,),)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.TOP, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    for i in data:
        T.insert(tk.END,str(i)) 

    tk.mainloop()
