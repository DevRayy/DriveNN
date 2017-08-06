import numpy as np
from PIL import ImageGrab
import cv2
import time

def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    while (True):
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 768)))
        new_screen = process_img(screen)
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        # cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # processed_img = cv2.Canny(original_image, threshold1=50, threshold2=300)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)
    processed_img = roi(processed_img, [vertices])

    return processed_img


def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


main()