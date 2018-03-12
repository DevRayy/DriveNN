import pyvjoy


class VirtualGamepad:

    def __init__(self):
        self._MAX_VJOY = 32767
        self._joy = pyvjoy.VJoyDevice(1)
        # TODO reset other axes

    def set_x(self, value):
        # TODO CLAMP -1 1
        self._joy.set_axis(pyvjoy.HID_USAGE_X, int((value+1) * self._MAX_VJOY/2.0))

    def set_z(self, value):
        # TODO CLAMP -1 1
        self._joy.set_axis(pyvjoy.HID_USAGE_Z, int((value+1) * self._MAX_VJOY/2.0))