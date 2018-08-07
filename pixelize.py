import cv2
import numpy as np

import settings


def highlight_road(image):
    height, width, depth = image.shape
    print(height, width, depth)

    for i in range(0, height):
        for j in range(0, width):
            R, G, B = image[i, j]
            if is_gray(R, G, B):
                image[i, j] = [255, 255, 255]
            else:
                image[i, j] = [0, 0, 0]

    return image


def is_gray(R, G, B):
    eps = 25;
    if abs(R-G) < eps and abs(G-B) < eps and abs(R-B) < eps:
        return True
    else:
        return False


WIDTH = settings.TARGET_RESOLUTION[0]
HEIGHT = settings.TARGET_RESOLUTION[1]

data = np.load('data_recorded/kart_chesterfield/raw-10.npy')
frame = data[150]
image = frame[0]

highlight_road(image)