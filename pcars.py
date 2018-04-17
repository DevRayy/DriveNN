import carseour
import settings

CAR_DATA_LEN = 9
GPS_DATA_LEN = 9


class Pcars:
    def __init__(self):
        self.raw_state = carseour.snapshot()

    def snapshot(self):
        self.raw_state = carseour.snapshot()

    def is_running(self):
        return carseour.live().mGameState == 2

    def car_data(self):
        return [
            self.raw_state.mLocalVelocity[0] / settings.TARGET_SPEED,
            self.raw_state.mLocalVelocity[1] / settings.TARGET_SPEED,
            self.raw_state.mLocalVelocity[2] / settings.TARGET_SPEED,
            self.raw_state.mAngularVelocity[0],
            self.raw_state.mAngularVelocity[1],
            self.raw_state.mAngularVelocity[2],
            self.raw_state.mLocalAcceleration[0] / settings.ACCELERATION_NORM,
            self.raw_state.mLocalAcceleration[1] / settings.ACCELERATION_NORM,
            self.raw_state.mLocalAcceleration[2] / settings.ACCELERATION_NORM
        ]

    def gps_data(self):
        return [
            self.raw_state.mWorldVelocity[0] / settings.TARGET_SPEED,
            self.raw_state.mWorldVelocity[1] / settings.TARGET_SPEED,
            self.raw_state.mWorldVelocity[2] / settings.TARGET_SPEED,
            self.raw_state.mWorldAcceleration[0] / settings.ACCELERATION_NORM,
            self.raw_state.mWorldAcceleration[1] / settings.ACCELERATION_NORM,
            self.raw_state.mWorldAcceleration[2] / settings.ACCELERATION_NORM,
            self.raw_state.players()[0].mWorldPosition[0] / settings.TRACK_BOUNDS,
            self.raw_state.players()[0].mWorldPosition[1] / settings.TRACK_BOUNDS,
            self.raw_state.players()[0].mWorldPosition[2] / settings.TRACK_BOUNDS
        ]
