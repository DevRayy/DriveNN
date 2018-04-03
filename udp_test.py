import carseour

# get a live view of the game - this is backed straight from the game's memory, and is updated for each rendered frame
game = carseour.live()

while True:
    # get a snapshot of the state of the game - this reads the memory and copies it before returning the object.
    game = carseour.snapshot()

    # print current speed of vehicle
    print((game.mSpeed / 27.875577926635742) * 100)