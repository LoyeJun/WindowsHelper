from ast import Try
from pickle import TRUE
import tkinter as tk
import time
import pyperclip
from PIL import Image, ImageTk
import pyautogui
from io import BytesIO
from pyscreeze import screenshot
import win32clipboard
import threading
import os
import webbrowser
import shutil
import pygame  
import pygame.camera  
from pywinauto import Desktop
import pyautogui
from tkinter import messagebox as msgbox

window = tk.Tk()
window.title("WindowsHelp")
window.attributes("-topmost",1)
window.attributes("-alpha",1)
window.state("normal")
window.overrideredirect(True)
window.config(background ='#131417') #0 161 214 00a1d6 #13 14 17
window.x=0



def mouse():
    x, y = pyautogui.position()
    if window.winfo_screenwidth()-50 < x < window.winfo_screenwidth() and window.winfo_screenheight()/2-210/2 < y < window.winfo_screenheight()/2+210/2:
        window.x=window.x+(45-window.x)/10
    else:
        window.x=window.x+(0-window.x)/8
    window.after(5,mouse)
    window.geometry('70x210+'+str(int(window.winfo_screenwidth()-25-window.x))+'+'+str(int(window.winfo_screenheight()/2-210/2)))
window.after(5,mouse)
def send_msg_to_clip(type_data, msg):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(type_data, msg)
    win32clipboard.CloseClipboard()
def paste_img(file_img):
    image = Image.open(file_img)
    output = BytesIO()
    image.save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    send_msg_to_clip(win32clipboard.CF_DIB, data)
window.usb_drive= None
def copy_usb_to_desktop():  
    # 检测U盘  
    window.usb_drive = None
    for drive in os.listdir("/Volumes"):  
        if drive != "Macintosh HD":  
            window.usb_drive = "/Volumes/" + drive
            break
def gettime():
    t.dstr.set(time.strftime('%H:%M:%S'))
    t.after(1,gettime) #1000=1second
def btn1_clicked(title,content):
    msgbox.showinfo(title,content)

class tools():
    def run():
        copy_usb_to_desktop()
        window.after(5,tools.Upan)
    def bilibili():
        url = "https://space.bilibili.com/1106294102" 
        webbrowser.open(url)
    def screenshot():
        screenshot = pyautogui.screenshot()
        name='screenshot/'+'WindowsHelp_screenshot_'+time.strftime('%Y_%m_%d-%H_%M_%S')+"-%03d" % (time.time() * 1000 % 1000)+'.png'
        try:
            new_directory = 'screenshot/'  
            os.mkdir(new_directory)
        except:
            pass
        screenshot.save(name)
        image_path = name
        paste_img(image_path)
    def clock():
        t = tk.Tk()
        t.dstr = tk.StringVar()
        t.geometry('400x200')
        t.attributes("-topmost",1)
        t.title('Time Display')
        btn1_clicked("Time", "我也不知道为什么这样子啊awa！")
        t.config(background ='#52c8df')
        ti = tk.Label(t,textvariable=t.dstr,fg='#303153',background='#52c8df',font=('Cascadia Code',30)).pack(side='left',expand=1,fill ='both')
        # gettime()
        t.update()
        t.mainloop()
        t.after(1,gettime)
    def desktop():
        # top_windows = Desktop(backend="uia").windows()
        # for w in top_windows:
        #     print(w.window_text())
        pyautogui.keyDown('winleft')
        pyautogui.press('d')
        pyautogui.keyUp('winleft')
    def Upan():
        if window.usb_drive is None:
            btn1_clicked("No USB drive detected.","No USB drive detected.")
            return
        # 复制U盘到桌面
        desktop_path = os.path.expanduser("C:/Users")
        shutil.copytree(window.usb_drive, desktop_path + "/USB")
        btn1_clicked("USB drive copied to desktop.","USB drive copied to desktop.")
    def camera():
        pygame.init()  
        pygame.camera.init()  
  
        # 列出可用的摄像头  
        cameras = pygame.camera.list_cameras()
  
        # 选择要使用的摄像头（这里假设选择第一个摄像头，索引为0）  
        camera = pygame.camera.Camera(cameras[0], (640, 480))  
        camera.start()  
  
        # 创建一个用于显示摄像头的窗口  
        screen = pygame.display.set_mode((640, 480))  
  
        # 不断循环，捕获和显示摄像头的图像  
        running = True  
        btn1_clicked('Successful','Camera:'+str(cameras[0]))
        while running:  
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    running = False  
              
            # 捕获一帧图像  
            image = camera.get_image()  
      
            # 将图像显示在窗口上  
            screen.blit(image, (0, 0))  
            pygame.display.flip()  
  
        # 停止摄像头并退出Pygame  
        camera.stop()  
        pygame.quit()
window.after(5,tools.Upan)

text = tk.Label(window,text="<",bg='#131417',fg="white",font=('letter-spacing',15))
text.pack(side='left')

a=tk.PhotoImage(file='assets/bilibili.png')
bilibili = tk.Button(window,text='',width=30, height=30,image=a,command=tools.bilibili).pack()
b=tk.PhotoImage(file='assets/screenshot.png')
screenshot = tk.Button(window,text='',width=30, height=30,image=b,command=tools.screenshot).pack()
c=tk.PhotoImage(file='assets/clock.png')
screenshot = tk.Button(window,text='',width=30, height=30,image=c,command=tools.clock).pack()
d=tk.PhotoImage(file='assets/desktop.png')
screenshot = tk.Button(window,text='',width=30, height=30,image=d,command=tools.desktop).pack()
e=tk.PhotoImage(file='assets/Upan.png')
screenshot = tk.Button(window,text='',width=30, height=30,image=e,command=tools.Upan).pack()
f=tk.PhotoImage(file='assets/camera.png')
screenshot = tk.Button(window,text='',width=30, height=30,image=f,command=tools.camera).pack()
        


window.update()
window.mainloop()