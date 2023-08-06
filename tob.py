from ctypes import windll
from pyautogui import *
import keyboard
import pyautogui
import time
import numpy as np
import random
import win32api
import win32con
import win32gui
import win32ui

time.sleep(2)

def click(x, y):    # click
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.35))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def train_options():    # training options
    if pyautogui.locateOnScreen('comparision_pngs/button_train_oguri.png', grayscale=True, confidence=0.7) != None:
        click(np.random.randint(870, 1032), np.random.randint(780, 834))
        time.sleep(np.random.uniform(3, 8))

def click_train_wisdom():   #commence wisdom training
    click(np.random.randint(1119, 1181), np.random.randint(831, 892))
    time.sleep(np.random.uniform(0.8, 1.5))
    click(np.random.randint(1119, 1181), np.random.randint(821, 882))
    
print("witaj swiecie")  # best debugging line known to mankind

#script start
train_options()
click_train_wisdom()