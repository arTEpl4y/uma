from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
from ctypes import windll
from PIL import Image
import cv2 as cv
import win32api
import win32con
import win32gui
import win32ui

time.sleep(2)
# best debugging line known to mankind
print("helo world")


def takess(hwnd, width, height):  # taking screenshot

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    bmpstr = saveBitMap.GetBitmapBits(True)

    img = np.frombuffer(bmpstr, dtype='uint8')
    img.shape = (height, width, 4)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return cv.cvtColor(img, cv.COLOR_RGBA2RGB)


# script start
win_uma = win32gui.FindWindow(None, "umamusume")
left, top, right, bottom = win32gui.GetWindowRect(win_uma)
width = right - left
height = bottom - top

while (True):
    ss = takess(win_uma, width, height)

    cv.imshow('cv2 - umamusume', ss)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

# def go_into_train_options():
#     if pyautogui.locateOnScreen('comparision_pngs\button_oguri_train.png', grayscale=True, confidence=0.7) != None:
#         click(np.random.randint(859, 1043), np.random.randint(773, 834))
#         time.sleep(np.random.uniform(3, 8))
