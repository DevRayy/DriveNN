import numpy as np
from grabscreen import grab_screen
from PIL import Image
import cv2
import time
from input import Input
import os
import threading
import random
import settings
import pytesseract
from speedometer import Speedometer

inp = Input()
thread = threading.Thread(target=inp.run)
thread.start()




def main():
    fileno = 0

    spd = Speedometer()
    speed_thread = threading.Thread(target=spd.run)
    speed_thread.start()

    if os.path.isfile(settings.TRAINING_DATA_FILENAME.format(fileno)):
        print('File exists, loading previous data!')
        training_data = list(np.load(settings.TRAINING_DATA_FILENAME))
    else:
        print('File does not exist, starting fresh!')
        training_data = []

    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)

    index = 0
    while True:
        last_time = time.time()

        try:
            screen = grab_screen(region=settings.SCREEN_BOUNDARIES)
            output = inp.get()
        except:
            continue

        # cv2.imshow('window', screen)
        screen = cv2.resize(screen, settings.IMAGE_RESOLUTION)

        speed = spd.get()

        m_screen = cv2.flip(screen, 1)
        # cv2.imshow('window', m_screen)
        m_output = [-output[0], output[1]]

        if speed != 0 and (output[1] < 0.98 or random.randrange(10) > 5):
            training_data.append([screen, speed, output])
            training_data.append([m_screen, speed, m_output])
            print(speed)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        print('{}: loop took {} seconds'.format(index, time.time() - last_time))

        index = index + 1
        if index % 2000 == 0:
            print(len(training_data))
            np.save(settings.TRAINING_DATA_FILENAME.format(fileno), training_data)
            fileno = fileno + 1
            training_data = []

main()
