import ctypes

import keyboard as keyboard
import pyautogui as pyautogui
from PIL import ImageGrab
from PIL.Image import Image
import numpy as np
import time
import cv2
import threading
from random import *


timeOfKryPress = [0.5, 0.3, 0.6, 0.4]
Movement = ('d', 'a')
movementIndex = 0

def DoMovement():
    global Movement, movementIndex, stopThread
    while True:
        if stopThread:
            break

        print(str(Movement[movementIndex]))
        keyboard.press(Movement[movementIndex])
        time.sleep(timeOfKryPress[randint(0, 3)])
        keyboard.release(Movement[movementIndex])

        movementIndex = movementIndex + 1
        if movementIndex == len(Movement):
             movementIndex = 0


def CompareImage(open_cv_imageNewFrame, open_cv_imageOldFrame):
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


def get_id(self):
    # returns id of the respective thread
    if hasattr(self, '_thread_id'):
        return self._thread_id
    for id, thread in threading._active.items():
        if thread is self:
            return id


def KillThread(thread):
    thread_id = get_id(thread)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                     ctypes.py_object(SystemExit))


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

print("ready")

grab_positionYellow = (
    mousepositionLEftTop[0], mousepositionLEftTop[1], mousepositionRightBottom[0], mousepositionRightBottom[1])

valueToIncreasePictureSize = 0
valueToMovePicture = 160
grab_positionInfoBox = (
    mousepositionLEftTop[0]+valueToMovePicture-valueToIncreasePictureSize, mousepositionLEftTop[1]-valueToIncreasePictureSize,
    mousepositionRightBottom[0]+valueToMovePicture+valueToIncreasePictureSize, mousepositionRightBottom[1]+valueToIncreasePictureSize)

YellowFrame = ConvertImgae(ImageGrab.grab(bbox=grab_positionYellow))
infoFrame = ImageGrab.grab(bbox=grab_positionInfoBox)
InfoBoxFrame = ConvertImgae(infoFrame)

isMovementThreadAlive = False
pokemonList = ["[S]", "[E]"]
while not keyboard.is_pressed("ctrl+ö"):
    if keyboard.is_pressed("ctrl+o"):
        print("pause")
        stopThread = True
        isMovementThreadAlive = False
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("ctrl+o"):
                print("end of pause")
                time.sleep(0.2)
                break
            if keyboard.is_pressed("ctrl+l"):
                print("edit pokemon List enter pokemon name or exit")
                time.sleep(0.2)
                input = input()
                while not input == "exit":
                    pokemonList.append(input)
                    input = input()

    thread = None
    frame = ImageGrab.grab(bbox=grab_positionInfoBox)
    newInfoBoxFrame = ConvertImgae(frame)
    if not CompareImage(InfoBoxFrame, newInfoBoxFrame):
        if not isMovementThreadAlive:
            stopThread = False
            isMovementThreadAlive = True
            thread = threading.Thread(target=DoMovement)
            thread.start()
    else:
        if isMovementThreadAlive:
            stopThread = True
            isMovementThreadAlive = False
        if CompareImage(ConvertImgae(ImageGrab.grab(bbox=grab_positionYellow)), YellowFrame):
            for i in range(0, 2):
                pyautogui.click()
                time.sleep(0.2)




