from inputs import get_gamepad


class InputGamepad:
    def __init__(self):
        self.X = 0
        self.Z = 0
        self._RZ = 0
        self._LZ = 0

    def _save_x(self, state):
        self.X = state/32767.0

    def _save_rz(self, state):
        self._RZ = state/255.0
        self._calculate_z()

    def _save_lz(self, state):
        self._LZ = state/255.0
        self._calculate_z()

    def _calculate_z(self):
        self.Z = self._RZ - self._LZ

    def get(self):
        return [self.X, self.Z]

    def run(self):
        while True:
            # print 'X: {}\tLZ: {}\tRZ: {}\tZ: {}'.format(self._X, self._LZ, self._RZ, self.Z)
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_X':
                    self._save_x(event.state)
                elif event.code == 'ABS_RZ':
                    self._save_rz(event.state)
                elif event.code == 'ABS_Z':
                    self._save_lz(event.state)
