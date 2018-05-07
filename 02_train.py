from random import shuffle, random
import numpy as np

import settings
import pcars
from models import inception_v3 as googlenet
from models import inception_v3_raw as googlenet_raw
from utils import apply_mask as mask

WIDTH = settings.TARGET_RESOLUTION[0]
HEIGHT = settings.TARGET_RESOLUTION[1]

print('Loading model...')
model = googlenet(width=WIDTH, height=HEIGHT, game_state_len=settings.GAME_STATE_LEN)
model.save(settings.MODEL_NAME)

print('Loading data (this might take a while)...')
recorded_data = np.load(settings.NORMALIZED_TRAINING_DATA_FILENAME)
print('Shuffling training data...')
shuffle(recorded_data)

print('Preparing to run...')
fraction = int(len(recorded_data) * settings.TESTING_DATA_FRACTION)
training_data = recorded_data[:-fraction]
testing_data = recorded_data[-fraction:]

camera_input = np.array([i[0] for i in training_data]).reshape(-1, WIDTH, HEIGHT, 3)
game_state_input = np.array([mask(i[1], settings.MASK) for i in training_data]).reshape(-1, settings.GAME_STATE_LEN)
controls_input = [i[2] for i in training_data]

camera_input_test = np.array([i[0] for i in testing_data]).reshape(-1, WIDTH, HEIGHT, 3)
game_state_input_test = np.array([mask(i[1], settings.MASK) for i in testing_data]).reshape(-1, settings.GAME_STATE_LEN)
controls_input_test = [i[2] for i in testing_data]

print('Learning started!')
model.fit({'main_camera': camera_input, 'game_state': game_state_input}, {'controller': controls_input},
          n_epoch=settings.EPOCHS,
          batch_size=settings.BATCH_SIZE,
          validation_set=({'main_camera': camera_input_test, 'game_state': game_state_input_test}, {'controller': controls_input_test}),
          snapshot_step=500,
          show_metric=True,
          run_id=settings.MODEL_NAME)

model.save(settings.MODEL_NAME)

# run this to start tensorboard
# tensorboard --logdir=C:\\foo