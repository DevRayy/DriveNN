import time

import numpy as np

import pcars
from pcars import Pcars
import settings
from models import inception_v3 as googlenet
from models import inception_v3_raw as googlenet_raw
from utils import normalize, apply_mask
from utils.virtual_gamepad import VirtualGamepad
from vision_gaming.identify import raw_image
from vision_gaming.job import Job
from vision_gaming.process import resize
from vision_gaming.vision_system import VisionSystem as VS

WIDTH = settings.TARGET_RESOLUTION[0]
HEIGHT = settings.TARGET_RESOLUTION[1]

print('Creating virtual gamepad...')
gamepad = VirtualGamepad()

print('Loading model...')
model = googlenet(width=WIDTH, height=HEIGHT, game_state_len=settings.GAME_STATE_LEN)
model.load(settings.MODEL_NAME)

print('Running visual system...')
system = VS(wait=settings.DRIVING_DELAY)
main_camera_job = Job(screen_rect=settings.MAIN_CAMERA_RECT,
                      process=[resize(settings.TARGET_RESOLUTION)],
                      identify=raw_image())
system.register_job('main_camera', main_camera_job)
system.run()

cars = Pcars()

print('Starting...')
for i in list(range(5))[::-1]:
    print(i + 1)
    time.sleep(1)

while True:
    if system.fresh:
        main_camera = system.get_results().get('main_camera')
        cars.snapshot()
        game_state = apply_mask(normalize(cars.get_data()))

        prediction = model.predict({'main_camera': main_camera.reshape(-1, WIDTH, HEIGHT, 3),
                                    'game_state': np.array([game_state]).reshape(-1, settings.GAME_STATE_LEN)})[0]
        print('Prediction: {}'.format(prediction))
        gamepad.set_x(prediction[0]+1)
        gamepad.set_z(prediction[1])

        time.sleep(settings.DRIVING_DELAY)
