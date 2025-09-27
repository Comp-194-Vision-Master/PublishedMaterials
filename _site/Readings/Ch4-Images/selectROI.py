""" ---------------------------------------------------------------------------------------------------
File: selectROI.py
Author: Susan Fox
Date: Fall 2025

This file contains a demo program that can select, and save, a regin of interest, using the mouse.
This involves a callback function, which is a new concept, as well as the use of global variables and
a displayed copy of the original image.
---------------------------------------------------------------------------------------------------
"""

import cv2


# --------------------------------------------------------------------------------------------------
# Declares global variables for the callback to use to communicate with the main program

startPt = None
endPt = None
selected = False

# --------------------------------------------------------------------------------------------------
# Mouse callback function
# We can detect several mouse events with OpenCV:
# * mouse moving: any movement of the mouse
# * mouse left button down: when the user depresses the left mouse button
# * mouse left button up: when the user releases the left mouse button
# * similar for other mouse buttons, if your mouse has them
# The callback function is called every time one of these actions happens

def selectROI(event, x, y, flags, param):
    """This is a mouse callback function. This is a special kind of function that is connected by OpenCV,
    in this case, to movement and clicking of the mouse button. This function isn't called by our main
    program, instead it is attached to the mouse, and then it gets called in its own thread (in parallel
    with our main program. It sets global variables to values that are shared with the main program,
    so the program can see the result of this function being called."""
    global startPt, endPt, selected

    if event == cv2.EVENT_LBUTTONUP:
        # If user just clicked and released the left mouse button...
        if startPt is None:
            startPt = (x, y)
        else:
            endPt = (x, y)
            selected = True


def runSelection(mainImg):
    """Takes in an image, and sets up a loop to view it while the user selects regions with the mouse.
    It displays a copy of the original image with a rectangle drawn on it to show the user's selected
    region, """
    global startPt, endPt, selected

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', selectROI)
    while True:
        workingCopy = mainImg.copy()
        if selected:
            print(startPt, endPt)
            cv2.rectangle(workingCopy, startPt, endPt, (0, 255, 255), 2)
        cv2.imshow("Image", workingCopy)
        x = cv2.waitKey(10)
        if x > 0:
            if chr(x) == 'q':
                break
            elif chr(x) == ' ':
                selected = False
                startPt = None
                endPt = None



img = cv2.imread("BallFinding/Pink/PinkBG1Mid.jpg")
runSelection(img)
