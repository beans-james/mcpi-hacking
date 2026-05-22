import sys

def menu():
    print("  beans-james/mcpi-hacking  ")
    print("0 -> Exit")
    print("1 -> Run Diamond Body Script (diabody.py)")
    print("2 -> Run Midas Touch Script (midas.py)")
    print("3 -> Run Instant Mega Spawner (spawner.py)")
    
    choice = input("Select an option: ").strip()

    if choice == "0":
        print("Goodbye!")
        sys.exit()  
    elif choice == "1":
        print("\nLaunching Diabody...")
        import diabody
    elif choice == "2":
        print("\nLaunching Midas Touch...")
        import midas
    elif choice == "3":
        print("\nLaunching Mega Spawner...")
        import spawner
    else:
        print("Invalid choice! Try again.")
        menu()

if __name__ == "__main__":
    menu()
