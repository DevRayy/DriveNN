import settings
import numpy as np
import pcars
from utils import normalize


recorded_data = []
for i in range(settings.FIRST_FILE_NO, settings.LAST_FILE_NO + 1):
    filename = settings.TRAINING_DATA_FILENAME.format(i)
    print('Loading file {} ...'.format(filename))
    recorded_data.extend(np.load(filename))

print("Calculating thresholds...")
maxes = [-999999] * pcars.DATA_LEN
mins = [999999] * pcars.DATA_LEN
for frame in recorded_data:
    screen = frame[0]
    game_state = frame[1]
    controller_state = frame[2]
    for i in range(pcars.DATA_LEN):
        if game_state[i] > maxes[i]:
            maxes[i] = game_state[i]
        if game_state[i] < mins[i]:
            mins[i] = game_state[i]

thresholds = [0] * pcars.DATA_LEN
for i in range(pcars.DATA_LEN):
    thresholds[i] = maxes[i] if abs(maxes[i]) > abs(mins[i]) else mins[i]

print("Saving thresholds...")
np.save(settings.METADATA_FILENAME, thresholds)

print("Normalizing...")
for i in range(len(recorded_data)):
    recorded_data[i][1] = normalize(recorded_data[i][1], thresholds)

print("Saving...")
np.save(settings.NORMALIZED_TRAINING_DATA_FILENAME, recorded_data)
