# Vacuum Cleaner Problem

def vacuum_cleaner(room1, room2, position):
    print("Initial State:")
    print("Room A:", room1)
    print("Room B:", room2)
    print("Vacuum Position:", position)

    # Clean Room A
    if position == "A":
        if room1 == "Dirty":
            print("Room A is dirty -> Cleaning Room A")
            room1 = "Clean"

        print("Moving from Room A to Room B")
        position = "B"

        if room2 == "Dirty":
            print("Room B is dirty -> Cleaning Room B")
            room2 = "Clean"

    # Clean Room B
    else:
        if room2 == "Dirty":
            print("Room B is dirty -> Cleaning Room B")
            room2 = "Clean"

        print("Moving from Room B to Room A")
        position = "A"

        if room1 == "Dirty":
            print("Room A is dirty -> Cleaning Room A")
            room1 = "Clean"

    print("\nFinal State:")
    print("Room A:", room1)
    print("Room B:", room2)
    print("Vacuum Position:", position)


# Example
vacuum_cleaner("Dirty", "Dirty", "A")
