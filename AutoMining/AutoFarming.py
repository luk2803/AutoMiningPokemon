import keyboard as keyboard
import pyautogui as pyautogui
from PIL import ImageGrab
from PIL.Image import Image
import numpy as np
import time
import cv2

def CompareImage (open_cv_imageNewFrame, open_cv_imageOldFrame):
    if open_cv_imageNewFrame.shape == open_cv_imageOldFrame.shape:
        difference = cv2.subtract(open_cv_imageOldFrame, open_cv_imageNewFrame)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
    return False

def ConvertImgae(Frame):
    Frame = Frame.convert("RGB")
    open_cv_imageNewFrame = np.array(Frame)
    return open_cv_imageNewFrame[:, :, ::-1].copy()

while True:
    if keyboard.is_pressed("ctrl"):
        mousepositionLEftTop = pyautogui.position()
        break
print("stage 1")
time.sleep(1)
print("stage 2")

while True:
    if keyboard.is_pressed("ctrl"):
        mousepositionRightBottom = pyautogui.position()
        break

grab_positionYellow = (
    mousepositionLEftTop[0], mousepositionLEftTop[1], mousepositionRightBottom[0], mousepositionRightBottom[1])
print("ready")

Movement = ('d', 'a')
movementIndex = 0
YellowFrame = ConvertImgae(ImageGrab.grab(bbox=grab_positionYellow))
while not keyboard.is_pressed("ctrl+ö"):

        newYellowFrame = ConvertImgae(ImageGrab.grab(bbox=grab_positionYellow))
        while not CompareImage(newYellowFrame, YellowFrame) and not keyboard.is_pressed("ctrl+ö"):
            keyboard.press(Movement[movementIndex])
            time.sleep(0.5)
            keyboard.release(Movement[movementIndex])

            movementIndex = movementIndex+1
            newYellowFrame = ConvertImgae(ImageGrab.grab(bbox=grab_positionYellow))
            if movementIndex == len(Movement):
                movementIndex = 0

        for i in range(0,2):
            pyautogui.click()
            time.sleep(0.2)










