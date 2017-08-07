from inputs import get_gamepad, DeviceManager

X = 0
Z = 0
_RZ = 0
_LZ = 0

def save_x(state):
    global X
    X = state/32767.0

def save_rz(state):
    global _RZ
    _RZ = state/255.0
    calculate_z()

def save_lz(state):
    global _LZ
    _LZ = state/255.0
    calculate_z()

def calculate_z():
    global Z
    Z = _RZ - _LZ

while True:
    print 'X: {}\tLZ: {}\tRZ: {}\tZ: {}'.format(X, _LZ, _RZ, Z)
    events = get_gamepad()
    for event in events:
        if event.code == 'ABS_X':
            save_x(event.state)
        elif event.code == 'ABS_RZ':
            save_rz(event.state)
        elif event.code == 'ABS_Z':
            save_lz(event.state)
