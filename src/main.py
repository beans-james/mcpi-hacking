# main.py
from init import init

# Initialize and get the minecraft world object
mc = init()

# Check if the connection was successful before running commands
if mc:
    # Get the player's current position
    x, y, z = mc.player.getTilePos()
    
    # Post a message to the in-game chat
    mc.postToChat("Hello from Python!")
    
    # Spawn a diamond block right above your head
    mc.setBlock(x, y + 2, z, 57)
