# nuke.py
import time
from init import init

mc = init()

if mc:
    print("\n-- GLOBAL nuke CONFIGURATION")
    spam_message = input("Enter the message to spam in chat: ").strip()
    if not spam_message:
        spam_message = "THE VOID CONSUMES ALL!"

    print("\n[WARNING] Global Purge Activated. Wiping entire world file coordinates...")
    mc.postToChat("!!! CRITICAL: UNLEASHING TOTAL WORLD ERASED !!!")
    
    AIR = 0
    BEDROCK = 7
    
    # Minecraft Pi standard world boundaries
    X_MIN, X_MAX = -128, 128
    Z_MIN, Z_MAX = -128, 128
    Y_MIN, Y_MAX = -64, 64  # Total height limit

    mc.setBlock(0, 0, 0, BEDROCK)
    mc.player.setTilePos(0, 1, 0) # Teleport player safely on top of it

    try:
        while True:
            # Instantly slice and delete the entire world map
            # We loop through X slices to prevent the API from overloading and crashing
            for x_slice in range(X_MIN, X_MAX, 32): 
                mc.setBlocks(
                    x_slice, Y_MIN, Z_MIN,
                    x_slice + 31, Y_MAX, Z_MAX,
                    AIR
                )
            
            mc.setBlock(0, 0, 0, BEDROCK)
            mc.postToChat(spam_message)
            
            # Pause for 2 seconds before executing the sweep again
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nPurge loop halted.")
        mc.postToChat("Purge sequence terminated.")
