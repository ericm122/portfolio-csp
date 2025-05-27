import random
import time
print("Welcome to Fisch.")
print("\n")
fishlist = ["Carp", "Bluegill", "Largemouth Bass", "Crimsonfish", "Ms. Angler"]
caughtfishlist = []

def fish():
    print ("shake...")
    time.sleep(2)
    print ("shake...")
    time.sleep(2)

    cast_fish = random.randint(0, 755)
    print("\n")
    if cast_fish <= 400:
        caughtfishlist.append("Carp")
        print("🎣 You caught a common Carp!")
        print("\n")
    elif cast_fish <= 600:
        caughtfishlist.append("Bluegill")
        print("🎣 You caught a rare Bluegill!")
        print("\n")
    elif cast_fish <= 700:
        caughtfishlist.append("Largemouth Bass")
        print("🎣 You caught a legendary Largemouth Bass!")
        print("\n")
    elif cast_fish <= 750:
        caughtfishlist.append("Crimsonfish")
        print("🔥 You caught the mythical Crimsonfish!")
        print("\n")
    elif cast_fish <= 755:
        caughtfishlist.append("Ms. Angler")
        print("🌟 Wow! You caught the secret Ms. Angler fish!")
        print("\n")
    else:
        print("🐟 The fish got away!")
        print("\n")

def check_fish():
    if not caughtfishlist:
        print("You haven't caught any fish yet.")
    else:
        print("You've caught:")
        for fish in caughtfishlist:
            print("-" + fish)

def sort_rarity(fish_list):
    if not fish_list:
        print("No fish to sort.")


    sorted_fish = []

    for fish in ["Carp", "Bluegill", "Largemouth Bass", "Crimsonfish", "Ms. Angler"]:  
        for caught in fish_list:
            if caught == fish:
                sorted_fish.append(caught)
    print("\n")
    print("Sorted by rarity:")
    for fish in sorted_fish:
        print("-", fish)

while True:
    print("What would you like to do?")
    print("""1. Go Fishing 🎣
2. Check Your Fishes 🐟
3. Sort by Rarity 📊
4. Quit

""")


    activity = int(input("Choose an activity (1-4): "))
    print("\n")
    if activity == 1:
        fish()
    elif activity == 2:
        check_fish()
    elif activity == 3:
        sort_rarity(caughtfishlist)
    elif activity == 4:
        print("Thanks for playing Fisch. Goodbye!")
        break
    else:
        print("Invalid input. Please choose a number from 1 to 4.")
