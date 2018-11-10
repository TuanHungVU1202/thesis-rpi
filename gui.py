from tkinter import *
from tkinter import messagebox
import index
import os
import sys
import paho.mqtt.client as paho

mqttClient = paho.Client("RPi")

host = "hung-laptop"
port = 3000

#setup general parameters for tkinter
window = Tk()
window.title("Welcome to My Home")
window.geometry('600x150')

#setup textbox
enter_txt = Entry(window, show="*", width=12)
enter_txt.grid(column=79, row=80)

def on_connect(mosq, obj, rc):
   print("on_connect() "+str(rc))
   
def face_recognize():
    index.main()

def clicked():
    messagebox.showinfo('Message title', 'Message content')

def restart_app():
    os.execl(sys.executable, sys.executable, * sys.argv)

def close_door():
    mqttClient.on_connect = on_connect
    print("Connecting to " + host)
    mqttClient.connect(host, port, 60)
    mqttClient.publish("toEsp/control/device/3", "off")

def submit_pass():
    import gui_admin
    print ("Password is: " + enter_txt.get())
    #TODO: change password here
    if enter_txt.get() == "1":
        gui_admin.main()
    
#TODO: stream camera to webserver
    
face_btn = Button(window,text='Start Face Recognition', command=face_recognize)
face_btn.grid(column=30,row=30)
close_btn = Button(window,text='Close door', command=close_door)
close_btn.grid(column=30,row=40)
owner_btn = Button(window,text='Ring the bell', command=clicked)
owner_btn.grid(column=0,row=0)
restart_btn = Button(window,text='RESTART!', command=restart_app)
restart_btn.grid(column=50,row=50)

#setting up for admin button
sudo_btn = Button(window,text='Log in as ADMIN!', command=submit_pass)
sudo_btn.grid(column=80,row=80)
 
window.mainloop()
