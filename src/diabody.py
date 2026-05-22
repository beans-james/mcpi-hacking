from init import init

mc = init()

if mc:
    # Get the player's current position
    x, y, z = mc.player.getTilePos()

    mc.setBlock(x, y - 1, z, 57)
    mc.setBlock(x, y + 2, z, 57)
