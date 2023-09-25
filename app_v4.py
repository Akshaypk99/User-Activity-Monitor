import os
import shutil
import time
# from PIL import Image,ImageTk
from datetime import date, datetime, timedelta
from threading import Thread
from tkinter import *
from tkinter import messagebox

import pyAesCrypt
from idle_time import IdleMonitor

import decrypt

ifid = ""
stoped_at = ''
started_at = ''
counter = 66600
running = False
ttl_string = ""
ttl_work = ""
idle_count = 66600
        
        
def L_UI():
    global app
    app = Tk()
    app.title('INFOLKS | WTM')
    # app.iconbitmap(os.path.join(os.getcwd(),'app.ico'))
    app.protocol('WM_DELETE_WINDOW', on_close)

    # ########### MENUBAR ########### #
    menubar = Menu(app)
    app.config(menu=menubar)
    file_menu = Menu(menubar, tearoff="off")
    menubar.add_cascade(label="File", menu=file_menu)
    # add a menu item to the menu
    file_menu.add_command(label='Open', command=decrypt.decryption)
    file_menu.add_separator()

    file_menu.add_command(label='About', command=viewAbout)

    # to popup app window onthe middle of the screen:
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2)-(500/2)
    y = (screen_height/2)-(350/2)
    app.geometry(f"500x350+{int(x)}+{int(y)}")
    app.resizable(False, False)

    LoginPage()

    app.mainloop()


# ======== ABOUT ==========
def viewAbout():
    root = Tk()
    root.title('WTM || About')
    # to popup app window onthe middle
    # root.iconbitmap(os.path.join(os.getcwd(),'app.ico'))
    # f the screen:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2)-(300/2)
    y = (screen_height/2)-(180/2)
    root.geometry(f"300x180+{int(x)}+{int(y)}")
    root.resizable(False, False)
    # ===== LABELS =====
    text = Label(root, text='Version 2.0.1', fg="#2e4d9f", font=("Helvetica", 13))
    text.place(x=15, y=15)
    cpyrght = Label(root, text='Copyright © WebFolks', font=("Helvetica", 8,))
    cpyrght.place(x=15, y=42)
    vrsn = Label(root, text='Version    : 2.0.1', font=("Helvetica", 8,))
    vrsn.place(x=15, y=92)
    pythn = Label(root, text='Python      : 3.9.13', font=("Helvetica", 8,))
    pythn.place(x=15, y=108)
    bld = Label(root, text='Built with Python Tkinter', font=("Helvetica", 8,))
    bld.place(x=15, y=135)
    mainloop()


# ----------Login Page-----------------------------------------------
def LoginPage():
    global ifid, started_at, stoped_at, counter, running
    # for form validation::

    def myfunction(*args):
        global username, ifid
        x = nameVar.get()
        y = idVar.get()
        y = y.replace(" ", "")
        if y and y.isnumeric():
            sbmt.config(state='normal',)
            username = x
            ifid = y

        else:
            sbmt.config(state='disabled')

    # ----BgImage----
    # bg = ImageTk.PhotoImage(file="images/form_bg.jpg")
    bg = Label(bg='#1d3159').place(x=0, y=0, relwidth=1, relheight=1)

    # ---Left image------
    # left = ImageTk.PhotoImage(file="images/logo_2.png")
    left_frame = Frame(bg='white')
    left_frame.place(x=40, y=90, width=120, height=170)
    left = Label(left_frame, text='INFOLKS', font=(
        'Montserrat', 17, 'bold'), bg="white", fg="#2e4d9f")
    left.place(x=8, y=30,)
    title = Label(left_frame, text='Work Time\n Monitor',
                  font=('Montserrat', 10, 'bold'), bg="white")
    title.place(x=22, y=90)

    # ----Form Frame-----
    frame1 = Frame(bg='#060c5c')
    frame1.place(x=160, y=90, width=299, height=170)
    # formTitle = Label(frame1, text="REGISTER HERE", font=("times new roman",20,"bold"), bg="#1c4a94",fg="white")
    # formTitle.place(x=100, y=70)

    nameVar = StringVar()
    idVar = StringVar()
    # Name
    # username = Label(frame1, text="Name", font=("times new roman",14,"bold"), bg="#060c5c",fg="white").place(x=10, y=30)
    # txt_username = Entry(frame1, textvariable=nameVar, font=("times new roman",14), bg="lightgrey")
    # txt_username.place(x=70, y=32)
    # IFID
    ifid_in = Label(frame1, text="IFID", font=(
        "times new roman", 13, "bold"), bg="#060c5c", fg="white").place(x=10, y=56)
    txt_ifid = Entry(frame1, textvariable=idVar, font=(
        "times new roman", 14), bg="lightgrey")
    txt_ifid.place(x=70, y=57)

    # submit button
    # btnImg = ImageTk.PhotoImage(file="images/submit_button.png")
    sbmt = Button(frame1, fg="white", bg="#060930", text="SUBMIT", font=(
        'Montserrat', 12, 'bold'), bd=1, cursor="hand2", state='disabled', command=lambda: [TimerPage()])
    sbmt.place(x=70, y=120, width=100)
    nameVar.trace("w", myfunction)
    idVar.trace("w", myfunction)


# -------------Timer Page----------------------------------------------
def TimerPage():
    global IF_ID, ID_LABEL, start_time, total_Label, start_label, start, stop
    global label, total_time , idle_LBL
    # ----BgImage----
    # bg = ImageTk.PhotoImage(file="images/form_bg.jpg")
    # bg = Label( image=bg).place(x=0, y=0, relwidth=1 ,relheight=1)
    frame1 = Frame(bg='#060c5c')
    frame1.place(x=0, y=0,  relwidth=1, relheight=1)
    # ======== BACK BUTTON =========
    # back = Button(frame1,text='BACK', font=('Calibri', 5,'bold',),fg='white',bg='black', command=lambda: controller.show_frame(LoginPage))
    # back.place(x=10, y=10,width=20,height=10)

    # ======== TIMER=======

    label = Label(frame1, text=datetime.fromtimestamp(counter).strftime(
        "%H:%M:%S"), fg='#060c5c', bg="white", font=("times new roman", 70, "bold"))
    label.place(x=25, y=30, width=450, height=100)
    wrk_LBL =  Label(frame1, text='Working Time',bg="white", fg='#060c5c', font=("Calibri", 8,'bold'))
    wrk_LBL.place(x=215 ,y=30)

    # ========  START BUTTON ========
    start = Button(frame1, text='START', font=('Calibri', 15, 'bold',),
                   fg='white', bg='#060930', command=lambda: [Start()])
    start.place(x=25, y=132, width=225, height=50)
    # ======== STOP BUTTON ========
    stop = Button(frame1, text='STOP & SAVE', font=('Calibri', 15, 'bold'), fg='white', bg='#060930', state='disabled',
                  command=lambda: [Stop(), summaryPage()])
    stop.place(x=251, y=132, width=225, height=50)

    # ------------ OTHER DISPLAY --------------
    displayframe = Frame(frame1, bg='#060c5c')
    displayframe.place(x=25, y=220, width=450, height=130)
    # ======= IFID =======
    IF_ID = Label(displayframe, text="", font=(
        "times new roman", 10, "bold"), bg="#060c5c", fg="#060c5c")
    IF_ID.place(x=0, y=10, width=66, height=25)
    ID_LABEL = Label(displayframe, text=ifid,  font=(
        "times new roman", 13, "bold"), bg="#060c5c", fg="#060c5c")
    ID_LABEL.place(x=0, y=38, width=66, height=35)
    
    # ====== STARTED AT =======
    start_label = Label(displayframe, text='', fg='#060c5c',
                        bg="#060c5c", font=("times new roman", 10, "bold"))
    start_label.place(x=70, y=10, width=184, height=25)
    start_time = Label(displayframe, text='', fg='#060c5c',
                       bg="#060c5c", font=("times new roman", 13, "bold"))
    start_time.place(x=70, y=38, width=184, height=35)

    # ====== TOTAL TIME =======
    total_Label = Label(displayframe, text='', fg='#060c5c',
                        bg="#060c5c", font=("times new roman", 10, "bold"))
    total_Label.place(x=258, y=10, width=195, height=25)
    total_time = Label(displayframe, text='', fg='#060c5c',
                       bg="#060c5c", font=("times new roman", 13, "bold"))
    total_time.place(x=258, y=38, width=195, height=35)

    idle_LBL = Label(displayframe, text='', fg='red',
                       bg="#060c5c", font=("Calibri", 10, "bold"))
    idle_LBL.place(x=297, y=75, width=195, height=35)


# start time
def Start():
    global running, ifid, started_at, started_at_date
    global IF_ID, ID_LABEL, start_time, total_Label, start_label, start, stop, label
    running = True
    started_at = datetime.now().strftime("%H:%M:%S")
    started_at_date = datetime.now()
    IF_ID.config(text='IFID', bg="white")
    ID_LABEL.config(text=ifid, bg="white")
    start_time.config(text=started_at, bg="white")
    start_label.config(text='STARTED AT', bg="white")
    total_Label.config(text='TOTAL TIME', bg="white")

    start['state'] = 'disabled'
    stop['state'] = 'normal'

    # start idleThread when Start Button Press
    Process = Thread(target=IdleTimeThread, daemon=True)
    Process.start()

    # start total time Thread
    total_start = Thread(target=TotalTimer, daemon=True)
    total_start.start()

    # ---- Start saving File -------
    saveProcess = Thread(target=autoSave, daemon=True)
    saveProcess.start()


def TotalTimer():
    global  started_at_date, running, ttl_string ,ttl_work,idle_count ,idle_time_str, label
    global idle_LBL
    while running:
        total_t = datetime.now() - started_at_date
        
        ttl_string = str(total_t).split('.')[0]
        total_time.config(text=ttl_string, bg='white')
        
        idle_time_str = datetime.fromtimestamp(idle_count).strftime("%H:%M:%S")
        
        FMT = '%H:%M:%S'
        ttl_work = datetime.strptime(ttl_string, FMT) - datetime.strptime(idle_time_str, FMT)
        
        if len( str(ttl_work).split(":")[0] )==1:
            ttl_work = "0"+str(ttl_work)
        label['text'] = ttl_work
        # if idle_time_str!="00:00:00":
        idle_LBL['text'] =f"IDLE TIME : {str(idle_time_str)}" 
        
        # print(ttl_string,idle_time_str , ttl_work)

        time.sleep(1)


# Stop time
def Stop():
    global running, username, ifid, stoped_at, stoped_at_date
    stoped_at_date = datetime.now()
    stoped_at = datetime.now().strftime("%H:%M:%S")

    start['state'] = 'normal'
    stop['state'] = 'disabled'
    running = False
    ifid = ifid

    SaveUserInfo(auto=False)



# timer resets when idle time >10
def IdleTimeThread():
    monitor = IdleMonitor.get_monitor()
    global running  ,idle_count
    # Choose the idletime here;
    maxIdletime = 10
    while running:
        if int(monitor.get_idle_time()) == maxIdletime:
            idle_count +=maxIdletime
            print(int(monitor.get_idle_time()))
            
            time.sleep(1)
        elif int(monitor.get_idle_time()) > maxIdletime:
            idle_count+=1
            print(int(monitor.get_idle_time()))
            
            time.sleep(1)

# Auto Save
def autoSave():
    while running:
        time.sleep(20)
        if running:
            SaveUserInfo(auto=True)


# to save Time Data into Text file ----------------------------------
def SaveUserInfo(auto=False):
    global  username, ifid, started_at, stoped_at, ttl_string ,idle_time_str,ttl_work

    idinfo = ifid
    current_date = date.today().strftime('%d-%m-%Y')
    MainFolder = os.path.join(os.getcwd(), 'Time_Details')
    if not os.path.exists(MainFolder):
        os.makedirs(MainFolder)

    folderName = str(current_date)
    txtfile = "IF"+str(idinfo)+"__"+str(current_date)+".txt"
    txtData = ["---------- "+str(current_date)+" ----------\n"]
    txtData.append("IFID         : "+str(ifid)+"\n")
    txtData.append("======== SESSION 1 ========\n")
    txtData.append("STARTED  AT  : "+str(started_at)+"\n")
    txtData.append("STOPPED  AT  : "+str(stoped_at)+"\n")
    txtData.append("TOTAL  TIME  : "+str(ttl_string)+"\n")
    ttl_idltime =  idle_time_str
    txtData.append("IDLE  TIME   : "+str(ttl_idltime)+"\n")
    txtData.append("TOTAL WORK TIME: "+str(ttl_work)+"\n\n")

    Timedir = os.path.join(MainFolder, folderName)
    if not os.path.exists(Timedir):
        os.makedirs(Timedir)

    # ------ WRITE TO TXT --------
    fout_aes = os.path.join(Timedir, txtfile.replace(".txt", ".aes"))

    # ---------- encryption --------------------
    bufferSize = 64 * 1024
    password = "infolks_techies"

    # ------ WRITE TO TEMP FILE (AUTO SAVE)--------
    backup_folder = os.path.join(Timedir, 'backup')
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    tname = "IF"+str(idinfo)+" ("+str(started_at.replace(':', '.'))+")"
    fout_aes_temp = os.path.join(backup_folder, tname+".aes")
    if auto:
        stptime = datetime.now().strftime("%H:%M:%S")
        print('auto saving....')
        fout_txt_temp = os.path.join(backup_folder, tname+'.txt')
        txtData[4] = "STOPPED  AT  : "+str(stptime)+"\n"
        with open(fout_txt_temp, 'w') as tf:
            tf.writelines(txtData)

        with open(fout_txt_temp, 'rb') as finp:
            with open(fout_aes_temp, "wb") as fOut:
                pyAesCrypt.encryptStream(finp, fOut, password, bufferSize)

        os.remove(fout_txt_temp)
    else:
        if os.path.exists(fout_aes_temp):
            # ++++++++ REPLACE AUTOSAVED DATA ++++++++
            stptime = datetime.now().strftime("%H:%M:%S")
            print('updating....auto saved data....')
            fout_txt_temp = os.path.join(backup_folder, tname+'.txt')
            txtData[4] = "STOPPED  AT  : "+str(stptime)+"\n"
            with open(fout_txt_temp, 'w') as tf:
                tf.writelines(txtData)

            with open(fout_txt_temp, 'rb') as finp:
                with open(fout_aes_temp, "wb") as fOut:
                    pyAesCrypt.encryptStream(finp, fOut, password, bufferSize)

            os.remove(fout_txt_temp)

        # ========== IF NOT EXISTS ===========
        if not os.path.exists(fout_aes):
            print('saving Data....')
            # -------------- ENCRYPT --------------
            fout_txt = os.path.join(Timedir, txtfile)

            with open(fout_txt, 'w') as tf:
                tf.writelines(txtData)

            with open(fout_txt, 'rb') as finp:
                with open(fout_aes, "wb") as fOut:
                    pyAesCrypt.encryptStream(finp, fOut, password, bufferSize)

            os.remove(fout_txt)
        # ========== IF ALREADY EXISTS ===========
        else:
            print('saving Existing Data....')

            # -------- temp Folder ---------
            cache_dir = os.path.join(os.getcwd(), 'cache')
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
            encFileSize = os.stat(fout_aes).st_size
            with open(fout_aes, "rb") as fIn:
                with open(os.path.join(cache_dir, "dataout.txt"), "wb") as fOut:
                    # decrypt file stream
                    pyAesCrypt.decryptStream(
                        fIn, fOut, password, bufferSize, encFileSize)
                # read decrypted ::
                with open(os.path.join(cache_dir, "dataout.txt"), "r") as tf:
                    existData = tf.readlines()
                    existData_ss = existData[2:]
                    check_ssion = []
                    for i in existData_ss:
                        if i != "\n" and len(i) < 50:
                            check_ssion.append(i)
                    n = 6
                    sessions = [
                        check_ssion[i * n:(i + 1) * n] for i in range((len(check_ssion) + n - 1) // n)]
                    # print(sessions)
                    session_length = len(sessions)
                    ssn_txt = "======== SESSION " + \
                        str(session_length+1)+" ========\n"
                    to_add = txtData[2:]
                    to_add[0] = ssn_txt

                    # ------ REMOVE LAST LINE ------
                    if session_length > 1:
                        existData.pop()

                    existData.extend(to_add)
                    existData_sss = existData[2:]
                    check_updated_ssion = []
                    for i in existData_sss:
                        if i != "\n" and len(i) < 50:
                            check_updated_ssion.append(i)

                    n = 6
                    updated_sessions = [
                        check_updated_ssion[i * n:(i + 1) * n] for i in range((len(check_updated_ssion) + n - 1) // n)]
                    print(updated_sessions)
                    # ----- add Time details -----

                    def to_td(h):
                        ho, mi, se = h.split(':')
                        return timedelta(hours=int(ho), minutes=int(mi), seconds=int(se))
                    ttl_list = []
                    idle_list = []
                    wrk_list = []
                    for ssn in updated_sessions:
                        print(ssn)
                        totl = ssn[3].replace("\n", "").split(": ")[-1]
                        ttl_list.append(totl)
                        idl = ssn[4].replace("\n", "").split(": ")[-1]
                        idle_list.append(idl)
                        wrk = ssn[5].replace("\n", "").split(": ")[-1]
                        wrk_list.append(wrk)

                    sum_ttl = str(sum(map(to_td, ttl_list), timedelta()))
                    sum_idle = str(sum(map(to_td, idle_list), timedelta()))
                    sum_wrk = str(sum(map(to_td, wrk_list), timedelta()))
                    print(sum_ttl, sum_idle, sum_wrk)
                    total__TXT = f"Total Time: {str(sum_ttl)}   IdleTime: {str(sum_idle)}  Work Time: {str(sum_wrk)}"
                    existData.append(total__TXT)

                # Write NEW DATA :::
                fout_txt = os.path.join(cache_dir, txtfile)

                with open(fout_txt, 'w') as tf:
                    tf.writelines(existData)

                with open(fout_txt, 'rb') as finp:
                    with open(fout_aes, "wb") as fOut:
                        pyAesCrypt.encryptStream(
                            finp, fOut, password, bufferSize)

                shutil.rmtree(cache_dir)


def Restart():
    LoginPage()
    global ifid, started_at, stoped_at, ttl_string, counter, running,idle_time_str,ttl_work,idle_count ,IF_ID
    ifid = ""
    started_at = ""
    ttl_string = ""
    idle_time_str = ""
    ttl_work = ""
    counter = 66600
    idle_count = 66600
    running = False
    IF_ID.config(text='')
    stop['state'] = 'disabled'
    start['state'] = 'normal'
    label['text'] = datetime.fromtimestamp(counter).strftime("%H:%M:%S")


# ------------------------------- SUMMARY PAGE -------------------------------
def summaryPage():
    global ifid, started_at, ttl_string, stoped_at,ttl_work,idle_time_str
    # print(ifid)
    frame1 = Frame(bg='#060c5c')
    frame1.place(x=0, y=0,  relwidth=1, relheight=1)
    summary_LBL = Label(frame1, text="SUMMARY", fg='#060c5c',
                        bg="white", font=("times new roman", 20, "bold"))
    summary_LBL.place(x=25, y=15, width=451, height=35)

    # ========  VIEW BUTTON  ========
    current_date = date.today().strftime('%d-%m-%Y')
    view = Button(frame1, text=f'SUMMARY  {str(current_date)}', font=(
        "times new roman", 20, "bold"), fg='#060c5c', bg='white', command=lambda: [])
    view.place(x=25, y=15, width=451, height=35)

    # ++++++++++++++++++++++++++++  SUMMARY  ++++++++++++++++++++++++++++
    summaryFrame = Frame(frame1, bg='#060c5c')
    summaryFrame.place(x=25, y=58, width=451, height=280)
    # ====================== IFID =================================
    IFIDlbl = Label(summaryFrame, text="IFID", fg='#060c5c',
                    bg="white", font=("times new roman", 10, "bold"))
    IFIDlbl.place(x=0, y=0, width=149, height=30)
    ifid_txt = Label(summaryFrame, text=ifid, fg='#060c5c',
                     bg="white", font=("times new roman", 15, "bold"))
    ifid_txt.place(x=151, y=0, width=299, height=30)
    # ====================== START TIME =========================
    strt = Label(summaryFrame, text="STARTED AT", fg='#060c5c',
                 bg="white", font=("times new roman", 10, "bold"))
    strt.place(x=0, y=32, width=149, height=32)
    strt_txt = Label(summaryFrame, text=started_at, fg='#060c5c',
                     bg="white", font=("times new roman", 15, "bold"))
    strt_txt.place(x=151, y=32, width=299, height=32)
    # ====================== STOP TIME ============================
    stp = Label(summaryFrame, text="STOPPED AT", fg='#060c5c',
                bg="white", font=("times new roman", 10, "bold"))
    stp.place(x=0, y=66, width=149, height=32)
    stp_txt = Label(summaryFrame, text=stoped_at, fg='#060c5c',
                    bg="white", font=("times new roman", 15, "bold"))
    stp_txt.place(x=151, y=66, width=299, height=32)

    # ====================== TOTAL TIME ============================
    ttl = Label(summaryFrame, text="TOTAL TIME", fg='#060c5c',
                bg="white", font=("times new roman", 10, "bold"))
    ttl.place(x=0, y=100, width=149, height=32)
    ttl_txt = Label(summaryFrame, text=ttl_string, fg='#060c5c',
                    bg="white", font=("times new roman", 15, "bold"))
    ttl_txt.place(x=151, y=100, width=299, height=32)
    # ====================== IDLE TIME ============================
    idle = Label(summaryFrame, text="IDLE TIME", fg='#060c5c',
                 bg="white", font=("times new roman", 10, "bold"))
    idle.place(x=0, y=134, width=149, height=32)
    ttl_idltime =  idle_time_str
    idle_txt = Label(summaryFrame, text=ttl_idltime, fg='#060c5c',
                     bg="white", font=("times new roman", 15, "bold"))
    idle_txt.place(x=151, y=134, width=299, height=32)

    # ====================== TOTAL WORKING TIME ============================
    ttlwrk = Label(summaryFrame, text="TOTAL WORK TIME", fg='#060c5c',
                   bg="white", font=("times new roman", 10, "bold"))
    ttlwrk.place(x=0, y=168, width=149, height=35)
    ttlwrk_txt = Label(summaryFrame, text=ttl_work, fg='#060c5c',
                       bg="white", font=("times new roman", 15, "bold"))
    ttlwrk_txt.place(x=151, y=168, width=299, height=35)

    # ====================== SHIFT CONDITION ============================
    hr = str(ttl_work).split(':')[0]
    mn = str(ttl_work).split(':')[1]
    shift = Label(summaryFrame, text="", fg='white', bg="#060c5c",
                  font=("times new roman", 17, "bold"))
    shift.place(x=0, y=210, width=452, height=35)
    if (int(hr) >= 6 and int(mn) >= 45) or int(hr) >= 7:
        ttlwrk_txt.config(fg="green")
        shift.config(text='SHIFT COMPLETED', bg="#004511")
    else:
        ttlwrk_txt.config(fg="red")
        shift.config(text='SHORT IN SHIFT TIME', bg="#a80505")

    # +++++++++++++++  RESTART BUTTON  +++++++++++++++++
    restrt = Button(summaryFrame, text='Restart', cursor="hand2", font=('Calibri', 15, 'bold',), fg='#060c5c', bg='white',
                    command=lambda: [Restart()])
    restrt.place(x=0, y=250, width=451, height=35)


def on_close():
    response = messagebox.askokcancel( 'Exit' , 'Are you sure want to exit?')
    if response:
        app.destroy()


# ------------------------------ Main Function ------------------------------
if __name__ == '__main__':
    L_UI()

