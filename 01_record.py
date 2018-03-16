import threading
import time

import cv2
import numpy as np

import settings
from utils.input_gamepad import InputGamepad
from vision_gaming.identify import raw_image, match_number
from vision_gaming.job import Job
from vision_gaming.process import resize, binary_threshold, show_screen
from vision_gaming.vision_system import VisionSystem as VS

# starting file index
fileno = 0
data = []
start_time = time.time()

controller = InputGamepad()
threading.Thread(target=controller.run).start()

system = VS(wait=settings.RECORDING_DELAY)
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

while True:
    if system.fresh and system.get_results().get('speedometer') > 0:
        main_camera = system.get_results().get('main_camera')
        speed = system.get_results().get('speedometer') / settings.RECORDING_TARGET_SPEED
        controller_state = controller.get()
        data.append([main_camera, speed, controller_state])

        if len(data) % (settings.ROWS_PER_FILE / 20) == 0:
            print('{}/{}'.format(len(data), settings.ROWS_PER_FILE))

        if len(data) % settings.ROWS_PER_FILE == 0:
            np.save(settings.TRAINING_DATA_FILENAME.format(fileno), data)
            print('File {} saved. Took {} seconds'.format(settings.TRAINING_DATA_FILENAME.format(fileno),
                                                          time.time() - start_time))
            fileno = fileno + 1
            data.clear()
            start_time = time.time()

        time.sleep(settings.RECORDING_DELAY)



