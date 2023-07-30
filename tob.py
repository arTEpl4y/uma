import time
import keyboard
import numpy as np
import random
import autoit
from ctypes import windll
from PIL import Image
import cv2 as cv
import win32api
import win32con
import win32gui
import win32com
import win32ui

time.sleep(2)
# best debugging line known to mankind
print("helo world")

def savess(hwnd,filename): # take and save screenshot
    
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
   
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)    
    saveDC.SelectObject(saveBitMap)    
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)
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
        im.save(filename)

def takess(hwnd):  # show cloned game window using cv2

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)
    bmpstr = saveBitMap.GetBitmapBits(True)

    img = np.frombuffer(bmpstr, dtype='uint8')
    img.shape = (height, width, 4)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return cv.cvtColor(img, cv.COLOR_RGBA2RGB)

def click(x, y):
    hWnd = win32gui.FindWindow(None, "umamusume")

    lParam = win32api.MAKELONG(x, y-39)

    win32api.PostMessage(hWnd, win32con.BM_CLICK, win32con.MK_LBUTTON, lParam)
    time.sleep(0.1)
    win32api.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

# script start
win_uma = win32gui.FindWindow(None, "umamusume")
left, top, right, bottom = win32gui.GetWindowRect(win_uma)
width = right - left - 16
height = bottom - top - 39

savess(win_uma,"ss.png")

while (True):

    ss = takess(win_uma)
    cv.imshow('cv2 - umamusume', ss)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break