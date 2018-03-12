import threading
import cv2
import numpy as np
import time

import settings
from input import Input
from vision_gaming.job import Job
from vision_gaming.process import resize, show_screen, binary_threshold
from vision_gaming.identify import raw_image, match_number
from vision_gaming.vision_system import VisionSystem as VS

# starting file index
fileno = 0
data = []
start_time = time.time()

controller = Input()
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
    if system.is_fresh:
        main_camera = system.get_results().get('main_camera')
        speed = system.get_results().get('speedometer')
        controller_state = controller.get()
        data.append([main_camera, speed, controller_state])

        if len(data) % settings.ROWS_PER_FILE == 0:
            np.save(settings.TRAINING_DATA_FILENAME.format(fileno), data)
            print('File {} saved. Took {} seconds'.format(settings.TRAINING_DATA_FILENAME.format(fileno),
                                                          time.time() - start_time))
            fileno = fileno + 1
            data.clear()
            start_time = time.time()

        time.sleep(settings.RECORDING_DELAY)



