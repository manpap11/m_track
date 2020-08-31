import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import all_track as allt
import sin_track as sint

root = tk.Tk()
root.title('SimpleServo')

def popup():
    messagebox.showinfo('More Info', 'SimpleServo by manpap11\nUsed:\n->Python 3.8.2\n->Tkinter\n->OpenCV-python 4.3.0')

def optw():
    top = tk.Toplevel()
    top.title('Options')

def logw():
    top = tk.Toplevel()
    top.title('Logs')


#Button and Label declarations
f2 = tk.LabelFrame(root, text='More Features')
l1 = tk.Label(root, text='SimpleServo')
l2 = tk.Label(root, text='SimpleServo is a simple tracking program that allows you\nto track multiple object in a video\nor track a single object using your Webcam.\n(I am not a UI developer as you can see)\n----------------------------------------------')
l3 = tk.Label(root, text='Select video to track:')
#SOS1-complete the filedialog for custom imports
imp_btn = tk.Button(root, text='Import', command=allt.main)
l4 = tk.Label(root, text='Use your Webcam for tracking an Object:')
#SOS2
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
