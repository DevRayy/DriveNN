from random import shuffle
import numpy as np

import settings
from models import inception_v3 as googlenet, alexnet

WIDTH = settings.TARGET_RESOLUTION[0]
HEIGHT = settings.TARGET_RESOLUTION[1]

print('Loading model...')
model = googlenet(width=WIDTH,
                  height=HEIGHT,
                  lr=settings.LEARNING_RATE)
model.save(settings.MODEL_NAME)

recorded_data = []
for i in range(settings.FIRST_FILE_NO, settings.LAST_FILE_NO + 1):
    filename = settings.TRAINING_DATA_FILENAME.format(i)
    print('Loading file {} ...'.format(filename))
    recorded_data.extend(np.load(filename))
print('Shuffling training data...')
shuffle(recorded_data)

print('Preparing to run...')
fraction = int(len(recorded_data) * settings.TESTING_DATA_FRACTION)
training_data = recorded_data[:-fraction]
testing_data = recorded_data[-fraction:]

camera_input = np.array([i[0] for i in training_data]).reshape(-1, WIDTH, HEIGHT, 3)
speed_input = np.array([i[1] for i in training_data]).reshape(-1, 1)
controls_input = [i[2] for i in training_data]

camera_input_test = np.array([i[0] for i in testing_data]).reshape(-1, WIDTH, HEIGHT, 3)
speed_input_test = np.array([i[1] for i in testing_data]).reshape(-1, 1)
controls_input_test = [i[2] for i in testing_data]

print('Learning started!')
model.fit({'main_camera': camera_input, 'speed': speed_input}, {'controller': controls_input},
          n_epoch=settings.EPOCHS,
          batch_size=settings.BATCH_SIZE,
          validation_set=({'main_camera': camera_input_test, 'speed': speed_input_test}, {'controller': controls_input_test}),
          snapshot_step=500,
          show_metric=True,
          run_id=settings.MODEL_NAME)

model.save(settings.MODEL_NAME)

# run this to start tensorboard
# tensorboard --logdir=C:\\foo