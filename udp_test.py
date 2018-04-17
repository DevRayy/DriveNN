import carseour

# get a live view of the game - this is backed straight from the game's memory, and is updated for each rendered frame
import time

game = carseour.live()

while True:
    # get a snapshot of the state of the game - this reads the memory and copies it before returning the object.
    game = carseour.snapshot()

    # print current speed of vehicle
    # print(game.mGameState)
    # print("===========================================================================")
    # print("mSpeed \t\t{:.2f}".format(game.mSpeed))
    # print("mLocalVelocity \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}".format(game.mLocalVelocity[0], game.mLocalVelocity[1], game.mLocalVelocity[2]))
    # print("mWorldVelocity \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}".format(game.mWorldVelocity[0], game.mWorldVelocity[1], game.mWorldVelocity[2]))
    # print("mAngularVelocity \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}".format(game.mAngularVelocity[0], game.mAngularVelocity[1], game.mAngularVelocity[2]))
    print("mLocalAcceleration \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}".format(game.mLocalAcceleration[0], game.mLocalAcceleration[1], game.mLocalAcceleration[2]))
    # print("mWorldAcceleration \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}".format(game.mWorldAcceleration[0], game.mWorldAcceleration[1], game.mWorldAcceleration[2]))
    print("player0 mWorldPosition \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}".format(game.players()[0].mWorldPosition[0], game.players()[0].mWorldPosition[1], game.players()[0].mWorldPosition[2]))
    # print("player0 mCurrentLapDistance{:.2f}".format(game.players()[0].mCurrentLapDistance))
    # print("===========================================================================")

    time.sleep(1)