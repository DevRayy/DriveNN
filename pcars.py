import carseour

DATA_LEN = 18


class Pcars:
    def __init__(self):
        self.raw_state = carseour.snapshot()

    def snapshot(self):
        self.raw_state = carseour.snapshot()

    def is_running(self):
        return carseour.live().mGameState == 2

    def get_data(self):
        return [
            self.raw_state.mLocalVelocity[0],
            self.raw_state.mLocalVelocity[1],
            self.raw_state.mLocalVelocity[2],
            self.raw_state.mAngularVelocity[0],
            self.raw_state.mAngularVelocity[1],
            self.raw_state.mAngularVelocity[2],
            self.raw_state.mLocalAcceleration[0],
            self.raw_state.mLocalAcceleration[1],
            self.raw_state.mLocalAcceleration[2],
            self.raw_state.mWorldVelocity[0],
            self.raw_state.mWorldVelocity[1],
            self.raw_state.mWorldVelocity[2],
            self.raw_state.mWorldAcceleration[0],
            self.raw_state.mWorldAcceleration[1],
            self.raw_state.mWorldAcceleration[2],
            self.raw_state.players()[0].mWorldPosition[0],
            self.raw_state.players()[0].mWorldPosition[1],
            self.raw_state.players()[0].mWorldPosition[2]
        ]
