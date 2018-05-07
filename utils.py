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
