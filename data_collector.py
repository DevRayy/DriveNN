import numpy as np
from grabscreen import grab_screen
import cv2
import time
from input import Input
import os
import threading
import random
import settings

inp = Input()
thread = threading.Thread(target=inp.run)
thread.start()

if os.path.isfile(settings.TRAINING_DATA_FILENAME):
    print('File exists, loading previous data!')
    training_data = list(np.load(settings.TRAINING_DATA_FILENAME))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():
    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)

    index = 0;
    while True:
        last_time = time.time()
        screen = grab_screen(region=settings.SCREEN_BOUNDARIES)
        # cv2.imshow('window', screen)
        screen = cv2.resize(screen, settings.IMAGE_RESOLUTION)
        output = inp.get()

        m_screen = cv2.flip(screen, 1)
        m_output = [-output[0], output[1]]

        if output[1] < 0.9 or random.randrange(10) > 7:
            training_data.append([screen, output])
            training_data.append([m_screen, m_output])
            print(output)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        print('loop took {} seconds'.format(time.time() - last_time))

        index = index + 1
        if index % 500 == 0:
            print(len(training_data))
            np.save(settings.TRAINING_DATA_FILENAME, training_data)

main()
