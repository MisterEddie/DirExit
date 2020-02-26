from PIL import Image
import time
import os

def showGraphic(boolean):
    if boolean:
        im = Image.open('floorplan_left.png')
        im.show()

    else:
        im = Image.open('floorplan_right.png')
        im.show()

    time.sleep(1)

while True:
    showGraphic(True)
    time.sleep(1)
    showGraphic(False)
    time.sleep(1)
