import time
from init import init

mc = init()

# Block ID definitions
AIR = 0
STONE = 1
WOOD = 17
LEAVES = 18
GLASS = 20
DOOR_WOOD = 64
WOOD_PLANKS = 5

def spawn_tree(x, y, z, height=5):
    """Generates a structured tree with a trunk and a round leaf canopy."""
    # 1. Build the trunk
    for i in range(height):
        mc.setBlock(x, y + i, z, WOOD)
        
    # 2. Build the leaf canopy (3 layers)
    leaf_center_y = y + height
    
    # Layer 1 (Bottom of leaves - wide)
    for lx in range(-2, 3):
        for lz in range(-2, 3):
            # Don't put leaves in the very corners so it looks rounder
            if abs(lx) == 2 and abs(lz) == 2:
                continue
            mc.setBlock(x + lx, leaf_center_y, z + lz, LEAVES)
            
    # Layer 2 (Middle of leaves - medium)
    for lx in range(-1, 2):
        for lz in range(-1, 2):
            mc.setBlock(x + lx, leaf_center_y + 1, z + lz, LEAVES)
            
    # Layer 3 (Top of leaves - single block tip)
    mc.setBlock(x, leaf_center_y + 2, z, LEAVES)

def spawn_house(x, y, z):
    """Builds a single detailed 5x5x5 house with a roof."""
    # Build a hollow box out of cobblestone/wood planks
    for hx in range(5):
        for hy in range(5):
            for hz in range(5):
                # Check if we are on the outer walls
                if hx == 0 or hx == 4 or hz == 0 or hz == 4:
                    if hy == 0:
                        mc.setBlock(x + hx, y + hy, z + hz, STONE) # Foundation
                    else:
                        mc.setBlock(x + hx, y + hy, z + hz, WOOD_PLANKS) # Walls
                else:
                    mc.setBlock(x + hx, y + hy, z + hz, AIR) # Hollow inside
                    
    # Cut out a door (front wall)
    mc.setBlock(x + 2, y + 1, z, AIR)
    mc.setBlock(x + 2, y + 2, z, AIR)
    mc.setBlock(x + 2, y + 1, z, DOOR_WOOD) # Simple bottom door block
    
    # Add windows (sides)
    mc.setBlock(x, y + 2, z + 2, GLASS)
    mc.setBlock(x + 4, y + 2, z + 2, GLASS)
    
    # Build a simple peaked roof (A-frame shape)
    for rx in range(5):
        mc.setBlock(x + rx, y + 5, z + 1, WOOD)
        mc.setBlock(x + rx, y + 5, z + 2, WOOD)
        mc.setBlock(x + rx, y + 5, z + 3, WOOD)
        mc.setBlock(x + rx, y + 6, z + 2, WOOD)

def spawn_village(start_x, start_y, start_z, number_of_houses=3):
    """Spawns a line of houses separated by space to create a village street."""
    current_x = start_x
    for i in range(number_of_houses):
        mc.postToChat(f"Building House {i+1}...")
        spawn_house(current_x, start_y, start_z)
        # Advance X coordinate by 7 blocks (5 for house + 2 for yard space)
        current_x += 7
        time.sleep(0.5)

if mc:
    x, y, z = mc.player.getTilePos()
    
    print("\n-- INSTANT BUILDER")
    print("1 -> Spawn a Giant Forest around you")
    print("2 -> Spawn a Quick Village")
    choice = input("What do you want to build? (1 or 2): ").strip()
    
    if choice == "1":
        mc.postToChat("Growing a rapid forest...")
        # Spawns 4 trees in a square layout around the player
        spawn_tree(x + 5, y, z, height=6)
        spawn_tree(x - 5, y, z, height=5)
        spawn_tree(x, y, z + 5, height=7)
        spawn_tree(x, y, z - 5, height=4)
        mc.postToChat("Forest complete!")
    elif choice == "2":
        mc.postToChat("Constructing a village...")
        # Spawns a row of 3 houses slightly in front of the player
        spawn_village(x + 5, y, z + 2, number_of_houses=3)
        mc.postToChat("Village complete!")
