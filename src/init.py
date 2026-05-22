from mcpi.minecraft import Minecraft

def init():
    """
    Initializes the connection to the Minecraft game instance.
    Returns the Minecraft object so you can interact with the world.
    """
    print("Connecting to Minecraft...")
    try:
        # Connects to the default host (localhost) and port (4711)
        mc = Minecraft.create()
        print("Connected successfully! Go wild.")
        return mc
    except Exception as e:
        print("Could not connect to Minecraft.")
        print("Make sure Minecraft is running with a compatible mod (like RaspberryJuice) and a world is loaded.")
        print(f"Error details: {e}")
        return None
