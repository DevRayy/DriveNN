# test_model.py

from grabscreen import grab_screen
from PIL import Image
import cv2
import time
import numpy as np
from alexnet import alexnet
from inception import inception_v3 as googlenet
from gamepad import Gamepad
import settings
import pytesseract
from speedometer import Speedometer
import threading

WIDTH = settings.IMAGE_RESOLUTION[0]
HEIGHT = settings.IMAGE_RESOLUTION[1]
LR = settings.LEARNING_RATE
EPOCHS = settings.EPOCHS
MODEL_NAME = 'driveNN-{}-{}-{}-epochs.model'.format(LR, 'googlenet',EPOCHS)

g = Gamepad()

model = googlenet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    last_time = time.time()

    spd = Speedometer()
    speed_thread = threading.Thread(target=spd.run)
    speed_thread.start()

    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        screen = grab_screen(region=settings.SCREEN_BOUNDARIES)

        speed_accel = spd.get()
        speed_accel = [speed_accel[0], speed_accel[1]]

        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        screen = cv2.resize(screen, (WIDTH, HEIGHT))
        predict = model.predict({'input': screen.reshape(-1, WIDTH, HEIGHT, 3), 'speed': np.array([speed_accel]).reshape(-1, 2)})[0]
        # predict = model.predict([screen.reshape(WIDTH, HEIGHT, 3), speed])[0]
        print(predict)
        g.set_x(predict[0])
        g.set_z(predict[1]*0.7)

        time.sleep(0.1)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
