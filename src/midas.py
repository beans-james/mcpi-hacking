import time
from init import init

mc = init()

if mc:
    mc.postToChat("King Midas has entered the game! Everything turns to gold.")
    print("Midas script running... Press Ctrl+C in the terminal to stop.")
    
    # Block ID for Gold Block is 41
    GOLD_BLOCK = 41
    AIR = 0
    
    try:
        while True:
            # Get player's current block position
            x, y, z = mc.player.getTilePos()
            
            # Look at the block directly underneath the player's feet
            block_beneath = mc.getBlock(x, y - 1, z)
            
            # Turn it to gold, unless it's already gold or empty air
            if block_beneath != GOLD_BLOCK and block_beneath != AIR:
                mc.setBlock(x, y - 1, z, GOLD_BLOCK)
                
            # Check if the player right-clicked a block using a Sword
            block_hits = mc.events.pollBlockHits()
            for hit in block_hits:
                hx, hy, hz = hit.pos.x, hit.pos.y, hit.pos.z
                mc.setBlock(hx, hy, hz, GOLD_BLOCK)
                mc.postToChat("Touched by gold!")
                
            # Small pause so it doesn't melt your CPU
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nMidas script stopped.")
        mc.postToChat("Midas spell broken.")
