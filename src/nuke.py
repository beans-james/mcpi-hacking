import time
from init import init

mc = init()

if mc:
    print("\n-- NUKE CONFIGURATION")
    spam_message = input("Enter the message to spam in chat: ").strip()
    if not spam_message:
        spam_message = "THE WORLD IS BEING PURGED!"

    print("\nNuke script activated. Press Ctrl+C in this terminal to stop.")
    mc.postToChat("!!! CRITICAL SYSTEM WARNING: NUKE ACTIVATED !!!")
    
    # Block definitions
    AIR = 0
    BEDROCK = 7
    
    # Define the radius of destruction (how far out from the player it clears)
    # Note: Setting this too high (e.g., over 50) might crash the Pi or the server.
    RADIUS = 30 

    try:
        while True:
            # Get the current player position to center the nuke
            px, py, pz = mc.player.getTilePos()
            
            # We clear blocks from way down below (py - 20) to high in the sky (py + 40)
            mc.setBlocks(
                px - RADIUS, py - 20, pz - RADIUS,
                px + RADIUS, py + 40, pz + RADIUS,
                AIR
            )
            
            # Places exactly one block of bedrock right under the player's feet
            mc.setBlock(px, py - 1, pz, BEDROCK)
            
            mc.postToChat(spam_message)
            
            # Wait 2 seconds before running the loop again
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nNuke script deactivated.")
        mc.postToChat("Nuke sequence aborted.")
