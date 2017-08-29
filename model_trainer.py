import numpy as np
from alexnet import alexnet
from inception import inception_v3 as googlenet
from random import shuffle
import settings

WIDTH = settings.IMAGE_RESOLUTION[0]
HEIGHT = settings.IMAGE_RESOLUTION[1]
LR = settings.LEARNING_RATE
EPOCHS = settings.EPOCHS
MODEL_NAME = 'driveNN-{}-{}-{}-epochs.model'.format(LR, 'googlenet', EPOCHS)

model = googlenet(width=WIDTH, height=HEIGHT, lr=LR, output=2)

train_data = []
print('Loading training data')
for i in range(12):
    print('Loading file {}'.format(i))
    train_data.extend(np.load(settings.TRAINING_DATA_FILENAME.format(i)))
print('Shuffling training data')
shuffle(train_data)

train = train_data[:-500]
test = train_data[-500:]

X1 = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
X2 = np.array([i[1] for i in train]).reshape(-1, 1)
Y = [i[2] for i in train]

test_x1 = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
test_x2 = np.array([i[1] for i in test]).reshape(-1, 1)
test_y = [i[2] for i in test]

model.fit({'input': X1, 'speed': X2}, {'targets': Y}, n_epoch=EPOCHS, batch_size=32, validation_set=({'input': test_x1, 'speed': test_x2}, {'targets': test_y}),
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming/log

model.save(MODEL_NAME)