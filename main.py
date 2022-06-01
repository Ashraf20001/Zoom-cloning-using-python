from vidstream import *
import tkinter as tk
import threading
import socket

local_ip_address=socket.gethostbyname(socket.gethostname())

server=StreamingServer(local_ip_address,9999)
receiver=AudioReceiver(local_ip_address,8888)
def Start_listening():
    t1=threading.Thread(target=server.start_server)
    t2=threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

def Start_Camera_Stream():
    camera_client=CameraClient(text_target_ip.get('1.0','end-1c'),7777)
    t3=threading.Thread(target=camera_client.start_stream)
    t3.start()

def Start_Screen_Sharing():
    screen_client=ScreenShareClient(text_target_ip.get('1.0','end-1c'),7777)
    t4=threading.Thread(target=screen_client.start_stream)
    t4.start()

def Start_Audio_Stream():
    audio_client=AudioSender(text_target_ip.get('1.0','end-1c'),7777)
    t5=threading.Thread(target=audio_client.start_stream)
    t5.start()


window=tk.Tk()
window.title("Ashraf Video v 0.0.3")
window.geometry('300x200')

label_target_ip=tk.Label(window,text="Target ip")
label_target_ip.pack()

text_target_ip=tk.Text(window,height=1)
text_target_ip.pack()

btn_listen=tk.Button(window,text="Start listening",width=25,command=Start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_camera=tk.Button(window,text="Start Camera Stream",width=25,command=Start_Camera_Stream)
btn_camera.pack(anchor=tk.CENTER,expand=True)

btn_screen=tk.Button(window,text="Start Screen Sharing",width=25,command=Start_Screen_Sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio=tk.Button(window,text="Start audio stream",width=25,command=Start_Audio_Stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop()
