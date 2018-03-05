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
    fileno = 90

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
            print('output: {}'.format(output))
        except:
            continue

        cv2.imshow('window', screen)
        screen = cv2.resize(screen, settings.IMAGE_RESOLUTION)

        speed_accel = spd.get()
        print('speed_accel: {}'.format(speed_accel))

        # m_screen = cv2.flip(screen, 1)
        # m_output = [-output[0], output[1]]

        if speed_accel[0] != 0:
            training_data.append([screen, speed_accel, output])
            # training_data.append([m_screen, speed_accel, m_output])

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
