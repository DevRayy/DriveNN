import carseour
import settings


def is_running():
    return carseour.live().mGameState == 2


def get_data(include_gps=True):
    state = carseour.snapshot()
    data = [
        state.mLocalVelocity[0] / settings.TARGET_SPEED,
        state.mLocalVelocity[1] / settings.TARGET_SPEED,
        state.mLocalVelocity[2] / settings.TARGET_SPEED,
        state.mAngularVelocity[0],
        state.mAngularVelocity[1],
        state.mAngularVelocity[2],
        state.mLocalAcceleration[0] / settings.ACCELERATION_NORM,
        state.mLocalAcceleration[1] / settings.ACCELERATION_NORM,
        state.mLocalAcceleration[2] / settings.ACCELERATION_NORM,
    ]
    if include_gps:
        data.append(state.mWorldVelocity[0] / settings.TARGET_SPEED)
        data.append(state.mWorldVelocity[1] / settings.TARGET_SPEED)
        data.append(state.mWorldVelocity[2] / settings.TARGET_SPEED)
        data.append(state.mWorldAcceleration[0] / settings.ACCELERATION_NORM)
        data.append(state.mWorldAcceleration[1] / settings.ACCELERATION_NORM)
        data.append(state.mWorldAcceleration[2] / settings.ACCELERATION_NORM)
        data.append(state.players()[0].mWorldPosition[0] / settings.TRACK_BOUNDS)
        data.append(state.players()[0].mWorldPosition[1] / settings.TRACK_BOUNDS)
        data.append(state.players()[0].mWorldPosition[2] / settings.TRACK_BOUNDS)
        data.append(state.players()[0].mCurrentLapDistance / settings.LAP_LENGTH)

    return data
