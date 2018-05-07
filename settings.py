#BRNO, Ford Focus RS

# GLOBAL
MODEL_HUMAN_NAME = 'kart_speed'
TRAINING_DATA_FILENAME = 'data_recorded/kart_speed/raw-{}.npy'
NORMALIZED_TRAINING_DATA_FILENAME = 'data_recorded/kart_speed/normalized-{}.npy'
METADATA_FILENAME = 'data_recoded/kart_speed/meta.json'
MAIN_CAMERA_RECT = (3, 350, 1020, 640)
TARGET_RESOLUTION = (508, 145)

# RECORDING
RECORDING_DELAY = 0.01
ROWS_PER_FILE = 1000

# PREPARING
MASK = [1, # raw_state.mLocalVelocity[0],
        1, # raw_state.mLocalVelocity[1],
        1, # raw_state.mLocalVelocity[2],
        1, # raw_state.mAngularVelocity[0],
        1, # raw_state.mAngularVelocity[1],
        1, # raw_state.mAngularVelocity[2],
        1, # raw_state.mLocalAcceleration[0],
        1, # raw_state.mLocalAcceleration[1],
        1, # raw_state.mLocalAcceleration[2],
        1, # raw_state.mWorldVelocity[0],
        1, # raw_state.mWorldVelocity[1],
        1, # raw_state.mWorldVelocity[2],
        1, # raw_state.mWorldAcceleration[0],
        1, # raw_state.mWorldAcceleration[1],
        1, # raw_state.mWorldAcceleration[2],
        1, # raw_state.players()[0].mWorldPosition[0],
        1, # raw_state.players()[0].mWorldPosition[1],
        1  # raw_state.players()[0].mWorldPosition[2]
]
GAME_STATE_LEN = sum(MASK)

# LEARNING
FIRST_FILE_NO = 0
LAST_FILE_NO = 25
LEARNING_RATE = 1e-3
EPOCHS = 50
BATCH_SIZE = 5
TESTING_DATA_FRACTION = 0.05

# DRIVING
DRIVING_DELAY = 0.03

MODEL_NAME = 'model_trained/{}-{}.ann'.format(MODEL_HUMAN_NAME, EPOCHS)
