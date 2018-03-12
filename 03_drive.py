import cv2
import time
import numpy as np

import settings
from gamepad import Gamepad
from models import inception_v3 as googlenet
from vision_gaming.job import Job
from vision_gaming.process import resize, show_screen, binary_threshold
from vision_gaming.identify import raw_image, match_number
from vision_gaming.vision_system import VisionSystem as VS

WIDTH = settings.TARGET_RESOLUTION[0]
HEIGHT = settings.TARGET_RESOLUTION[1]

print('Creating virtual gamepad...')
gamepad = Gamepad()

print('Loading model...')
model = googlenet(width=WIDTH,
                  height=HEIGHT,
                  lr=settings.LEARNING_RATE)
model.load(settings.MODEL_NAME)

print('Running visual system...')
system = VS(wait=settings.DRIVING_DELAY)
main_camera_job = Job(screen_rect=settings.MAIN_CAMERA_RECT,
                      process=[resize(settings.TARGET_RESOLUTION)],
                      identify=raw_image())
system.register_job('main_camera', main_camera_job)
templates = [cv2.imread('templates/{}.jpg'.format(i), 1) for i in range(0, 10)]
speedometer_job = Job(screen_rect=settings.SPEEDOMETER_RECT,
                      process=[binary_threshold(200, 255)],
                      identify=match_number(templates, range(0, 10)))
system.register_job('speedometer', speedometer_job)
system.run()

print('Starting...')
for i in list(range(5))[::-1]:
    print(i + 1)
    time.sleep(1)

while True:
    if system.fresh:
        main_camera = system.get_results().get('main_camera')
        speed = system.get_results().get('speedometer') / settings.DRIVING_TARGET_SPEED

        prediction = model.predict({'main_camera': main_camera.reshape(-1, WIDTH, HEIGHT, 3),
                                    'speed': np.array([speed])})[0]
                                    # 'speed': np.array([speed]).reshape(-1, 2)})[0]
                                    # FIXME remove above when confirmed working
        print('Prediction: {}'.format(prediction))
        gamepad.set_x(prediction[0])
        gamepad.set_z(prediction[1])

        time.sleep(settings.DRIVING_DELAY)
