# test_model.py

from grabscreen import grab_screen
import cv2
import time
from alexnet import alexnet
from gamepad import Gamepad
import settings

WIDTH = settings.IMAGE_RESOLUTION(0)
HEIGHT = settings.IMAGE_RESOLUTION(1)
LR = settings.LEARNING_RATE
EPOCHS = settings.EPOCHS
MODEL_NAME = 'driveNN-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

g = Gamepad()

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    last_time = time.time()

    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        screen = grab_screen(region=settings.SCREEN_BOUNDARIES)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        screen = cv2.resize(screen, (WIDTH, HEIGHT))
        # cv2.imshow('', screen)
        predict = model.predict([screen.reshape(WIDTH, HEIGHT, 3)])[0]
        print(predict)
        g.set_x(predict[0])
        g.set_z(predict[1])

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
