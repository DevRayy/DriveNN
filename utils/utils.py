import numpy as np
import settings


def apply_mask(state, mask):
    ret = []
    for i in range(len(state)):
        if mask[i] == 1:
            ret.append(state[i])
    return ret


def normalize(game_state, thresholds=None):
    if thresholds is None:
        thresholds = np.load(settings.METADATA_FILENAME)
    ret = [0] * len(game_state)
    for i in range(len(game_state)):
        ret[i] = game_state[i] / thresholds[i]
    return ret


def highlight_road(image, road_value=255):
    height, width, depth = image.shape
    print(height, width, depth)

    for i in range(0, height):
        for j in range(0, width):
            R, G, B = image[i, j]
            if is_gray(R, G, B):
                image[i, j] = [road_value]
            else:
                image[i, j] = [0, 0, 0]
    return image


def is_gray(R, G, B):
    eps = 25
    return abs(R-G) < eps and abs(G-B) < eps and abs(R-B) < eps
