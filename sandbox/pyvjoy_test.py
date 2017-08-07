import pyvjoy

MAX_VJOY = 32767
j = pyvjoy.VJoyDevice(1)
X = 0.5

while True:
    j.data.wAxisX = int(X * MAX_VJOY)
    # self.j.data.wAxisY = int(Y * self.MAX_VJOY)
    # self.j.data.wAxisZ = int(Z * self.MAX_VJOY)
    # self.j.data.wAxisXRot = int(XRot * self.MAX_VJOY)
    j.update()
    j.set_axis