from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con, win32gui

time.sleep(1)

#click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(0.1,0.35))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

win_uma = win32gui.FindWindow(None, "umamusume")

def takescreen(hwnd,width,height,filename):
    #hwnd is window handle
    #width, height are in pixels
    #filename is name of screenshot file
    
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
   
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)    
    saveDC.SelectObject(saveBitMap)    
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        #PrintWindow Succeeded
        im.save(filename)

#sample usage
hwnd = win32gui.FindWindow(None, 'Chrome')
takescreen(hwnd,1024,768,'screenshot.png')

#best debugging line known to mankind
print("helo world")

#while keyboard.is_pressed('q') == False:

    #if pyautogui.locateOnScreen('comparision_pngs/button.png', grayscale=True, confidence=0.7) != None:
    #    click(np.random.randint(852,1053),np.random.randint(854,896))
    #    time.sleep(np.random.uniform(2,7))

#script start

#training options
def go_into_train_options():
    if pyautogui.locateOnScreen('comparision_pngs\button_oguri_train.png', grayscale=True, confidence=0.7) != None:
        click(np.random.randint(859,1043),np.random.randint(773,834))
        time.sleep(np.random.uniform(3,8))

