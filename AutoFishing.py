import ctypes

import keyboard as keyboard
import pyautogui as pyautogui
from PIL import ImageGrab
from PIL.Image import Image
import numpy as numpy
import time
import cv2
import threading

rot = 255
colorOfPointToWatch = ()
grab_positionStandard = [1920, 1030, 1060, 749]
count = 0



def CompareImage(open_cv_imageNewFrame, open_cv_imageOldFrame):
    if open_cv_imageNewFrame.shape == open_cv_imageOldFrame.shape:
        difference = cv2.subtract(open_cv_imageOldFrame, open_cv_imageNewFrame)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
    return False

def ConvertImgae(Frame):
    Frame = Frame.convert("RGB")
    open_cv_imageNewFrame = numpy.array(Frame)
    return open_cv_imageNewFrame[:, :, ::-1].copy()

def getMousePositionAtControl():
    while True:
        if keyboard.is_pressed("ctrl"):
            mousePositionYellowColor = pyautogui.position()
            break
    time.sleep(0.5)
    print("ready")
    return mousePositionYellowColor


def getPicturePos():
    while True:
        if keyboard.is_pressed("ctrl"):
            mousepositionLEftTop = pyautogui.position()
            break
    print("stage 1")
    time.sleep(0.5)
    print("stage 2")

    while True:
        if keyboard.is_pressed("ctrl"):
            mousepositionRightBottom = pyautogui.position()
            break

    grab_picturePos = (
        mousepositionLEftTop[0], mousepositionLEftTop[1], mousepositionRightBottom[0], mousepositionRightBottom[1])
    time.sleep(0.5)
    print("ready")
    return grab_picturePos
def GetGreenPos(img):
    global count,colorOfPointToWatch
    count = 0
    wasConditionTrueYet = False
    grab_position = [0,0]
    img = img.convert('RGB')
    x = img.size[1]/2
    for y in range(0, img.size[0]):
        r, g, b = img.getpixel((y, x))
        if rot == r and g > 170 and b < 50:
            count += 1
            if not wasConditionTrueYet:
                wasConditionTrueYet = True
                r, g, b = img.getpixel((y, x))
                colorOfPointToWatch = (r,g,b)
                print(str(r)+","+str(g)+","+str(b))
                print(str(y) + "    " + str(x))
                grab_position[0] = y
                grab_position[1] = x
        elif wasConditionTrueYet:
            break

    return grab_position

def getYellowColor ():
    global grab_YellowColorPosition
    img = ImageGrab.grab()
    ImgArray = img.load()
    return ImgArray[grab_YellowColorPosition.x, grab_YellowColorPosition.y]

grab_fishingMinigame = getPicturePos()
img = ImageGrab.grab(bbox= grab_fishingMinigame)
grab_YellowColorPosition = getMousePositionAtControl()
yellowColor = getYellowColor()
pokemonList = ["[S]", "[E]"]
firstgrab = True
minigameAppeared = False
pos = [0,0]


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

    if getYellowColor() == yellowColor:
        for i in range(0, 2):
            pyautogui.click()
            time.sleep(0.2)
        continue

    newFishingMinigameFrame = ImageGrab.grab(bbox=grab_fishingMinigame)
    pixelImage = newFishingMinigameFrame.convert("RGB")
    ImgArray = pixelImage.load()
    if not minigameAppeared:
        pos = GetGreenPos(newFishingMinigameFrame)
        if pos != [0,0]:
            minigameAppeared = True
    if minigameAppeared:
        for i in range(0,count-10):
            x = pos [0] + i
            y = pos[1]
            r, g, b = pixelImage.getpixel((x, y))
            if not (rot == r and g > 170 and b < 50):
                keyboard.press_and_release("space")
                time.sleep(0.5)
                minigameAppeared = False
                break
























