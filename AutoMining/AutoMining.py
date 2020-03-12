import keyboard as keyboard
import pyautogui as pyautogui
from PIL import ImageGrab
from PIL.Image import Image
import numpy as np
import time
import cv2

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def CompareImage (open_cv_imageNewFrame, open_cv_imageOldFrame):
    if open_cv_imageNewFrame.shape == open_cv_imageOldFrame.shape:
        difference = cv2.subtract(open_cv_imageOldFrame, open_cv_imageNewFrame)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
    return False


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
oldFrame = None
isMiningUp = True
while not keyboard.is_pressed("ctrl+ö"):
    grab_position = (
    mousepositionLEftTop[0], mousepositionLEftTop[1], mousepositionRightBottom[0], mousepositionRightBottom[1])
    newFrame = ImageGrab.grab(bbox=grab_position).convert("RGB")
    if oldFrame.__eq__(None):
        oldFrame = newFrame
    open_cv_imageNewFrame = np.array(newFrame)
    open_cv_imageNewFrame = open_cv_imageNewFrame[:, :, ::-1].copy()

    open_cv_imageOldFrame = np.array(oldFrame)
    open_cv_imageOldFrame = open_cv_imageOldFrame[:, :, ::-1].copy()

    oldFrame = newFrame


    if not CompareImage(open_cv_imageNewFrame, open_cv_imageOldFrame):
        isMiningUp = not isMiningUp
        if isMiningUp:
            keyboard.press_and_release('space')



