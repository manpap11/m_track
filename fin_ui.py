import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import all_track as allt
import sin_track as sint

root = tk.Tk()
root.title('SimpleSurvo')

def app_sen(num):
    allt.gsens = num

def app_clr(clr):
    if clr == 'Green':
        allt.gclr = (0, 255, 0)
    elif clr == 'Red':
        allt.gclr = (255, 0, 0)
    else:
        allt.gclr = (0, 0, 255)

def app_speed(num):
    allt.gdelay = num

def app_default():
    allt.gsens = 800
    allt.gclr = (0, 255, 0)
    allt.gdelay = 50

def imp_vid():
    root.filename = filedialog.askopenfilename(initialdir="/m_track", title="Select A File", filetypes=(("avi files", "*.avi"), ("all files", "*.*")))
    allt.main(root.filename)

def popup():
    messagebox.showinfo('More Info', 'SimpleSurvo by manpap11\nUsed:\n->Python 3.8.2\n->Tkinter\n->OpenCV-python 4.3.0')

def optw():
    top = tk.Toplevel()
    top.title('Options')
    top.geometry('250x130')

    #Label init
    t1 = tk.Label(top, text='Sensitivity:')
    t1.grid(row=0, column=0)
    t2 = tk.Label(top, text='Outline Color:')
    t2.grid(row=1, column=0)
    t4 = tk.Label(top, text='Video Speed:')
    t4.grid(row=3, column=0)
    #Option function init
    sen_e = tk.Entry(top, width=5)
    sen_e.grid(row=0, column=1)
    #clr = Color for the out_color
    clr = tk.StringVar()
    clr.set('Green')
    out_color = tk.OptionMenu(top, clr, 'Red', 'Green', 'Blue')
    out_color.grid(row=1, column=1)
    vid_speed = tk.Entry(top, width=5)
    vid_speed.grid(row=3, column=1)
    #Apply and default buttons
    sen_btn = tk.Button(top, text='Apply', command=lambda: app_sen(sen_e.get()))
    sen_btn.grid(row=0, column=2)
    clr_btn = tk.Button(top, text='Apply', command=lambda: app_clr(clr))
    clr_btn.grid(row=1, column=2)
    speed_btn = tk.Button(top, text='Apply', command=lambda: app_speed(vid_speed.get()))
    speed_btn.grid(row=3, column=2)
    default_btn = tk.Button(top, text='Default', command=app_default, padx=30)
    default_btn.grid(row=4, column=1, columnspan=2)


def logw():
    top = tk.Toplevel()
    top.title('Logs')
    top.geometry('200x100')
    log1 = tk.Label(top, text='(Coming Soon...)')
    log1.pack()


#Button and Label declarations
f2 = tk.LabelFrame(root, text='More Features')
l1 = tk.Label(root, text='SimpleSurvo')
l2 = tk.Label(root, text='SimpleSurvo is a simple tracking program that allows you\nto track multiple objects in a video\nor track a single object using your Webcam.\n----------------------------------------------')
l3 = tk.Label(root, text='Select video to track:')
#SOS1-complete the filedialog for custom imports
imp_btn = tk.Button(root, text='Import', command=imp_vid)
l4 = tk.Label(root, text='Use your Webcam for tracking an Object:')
#SOS2-find smth about camera brightness
web_btn = tk.Button(root, text='Live Play', command=sint.main)
opt_btn = tk.Button(f2, text='Options', command=optw)
log_btn = tk.Button(f2, text='Logs', command=logw)
info_btn = tk.Button(f2, text='Info', command=popup)

l1.config(font=('Courier', 40))

#Grid placements
f2.grid(row=4, column=0, columnspan=3)
l1.grid(row=0, column=0, columnspan=2)
l2.grid(row=1, column=0, columnspan=2)
l3.grid(row=2, column=0)
imp_btn.grid(row=2, column=1)
l4.grid(row=3, column=0)
web_btn.grid(row=3, column=1)
opt_btn.pack()
log_btn.pack()
info_btn.pack()

root.mainloop()
