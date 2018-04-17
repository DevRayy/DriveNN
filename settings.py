#BRNO, Ford Focus RS

# GLOBAL
MODEL_HUMAN_NAME = 'kart_car_gps'
TRAINING_DATA_FILENAME = 'data_recorded/img_car_gps_kart-{}.npy'
MAIN_CAMERA_RECT = (3, 350, 1020, 640)
TARGET_RESOLUTION = (508, 145)
TARGET_SPEED = 0.28 * 100.0 #km/h
ACCELERATION_NORM = 20
TRACK_BOUNDS = 250
LAP_LENGTH = 5400.0

# RECORDING
RECORDING_DELAY = 0.01
ROWS_PER_FILE = 1000

# LEARNING
FIRST_FILE_NO = 0
LAST_FILE_NO = 25
LEARNING_RATE = 1e-3
EPOCHS = 150
BATCH_SIZE = 5
TESTING_DATA_FRACTION = 0.05

# DRIVING
DRIVING_DELAY = 0.03

MODEL_NAME = 'model_trained/{}-{}.ann'.format(MODEL_HUMAN_NAME, EPOCHS)
