import sys

def menu():
    print("  beans-james/mcpi-hacking  ")
    print("0 -> Exit")
    print("1 -> Run Diamond Body Script (diabody.py)")
    print("2 -> Run Midas Touch Script (midas.py)")
    
    choice = input("Select an option (0-2): ").strip()

    if choice == "0":
        print("Goodbye!")
        sys.exit()  
    elif choice == "1":
        print("\nLaunching Diabody...")
        import diabody
    elif choice == "2":
        print("\nLaunching Midas Touch...")
        import midas
    else:
        print("Invalid choice! Try again.")
        menu()

if __name__ == "__main__":
    menu()
