import time

class MysteryGame():
    def __init__(self):
        self.running = True
        self.inventory = []
        self.locations = {
            "study": {
                "description": "A dimly lit study with a desk covered in papers.",
                "actions": {
                    "search the desk": self.search_desk,
                    "look at the bookshelf": self.look_bookshelf,
                    "examine the rug": self.examine_rug,
                    "go back": lambda: self.handle_input("go entryway"),
                    
                }
            },
            "kitchen": {
                "description": "A cozy kitchen with a few dishes in the sink.",
                "actions": {
                    "look in the fridge": self.look_fridge,
                    "examine the countertops": self.examine_countertops,
                    "check the pantry": self.check_pantry,
                    "go back": lambda: self.handle_input("go entryway"),
                }
            },
            "bedroom": {
                "description": "A messy bedroom with clothes strewn everywhere.",
                "actions": {
                    "search the closet": self.search_closet,
                    "examine the body": self.examine_body,
                    "check the nightstand": self.check_nightstand,
                    "go back": lambda: self.handle_input("go entryway"),
                }
            },
            "entryway": {
                "description": "The entryway, with a coat rack and a mirror.",
                "actions": {
                    "look at the coat rack": self.look_coat_rack,
                    "check the mirror": self.check_mirror,
                    "examine the door": self.examine_door,
                    "choose a room": lambda: self.main_menu(),
                }
            },
        }
        self.current_location = "entryway"

    def show_intro(self):
        intro_messages = [
            "You are called to investigate the murder of an unknown man found in a neighborhood home.",
            "You arrive at the scene and find yourself in the entryway of the house.",
            "You need to explore the house to gather clues and solve the mystery."
        ]
        for message in intro_messages:
            print(message)
            time.sleep(2) 
   
    def show_location(self):
        print(f"\nYou are in the {self.current_location}.")
        print(self.locations[self.current_location]["description"])

    def main_menu(self):
        while True:
            print("\nWhere would you like to go?")
            for location in self.locations:
                print(f"- {location.capitalize()}")
            choice = input("\nType your choice: ").strip().lower()
            if choice in self.locations:
                self.enter_location(choice)
                break 
            else:
                print("Invalid choice. Try again.")

    def enter_location(self, location):
        self.current_location = location
        print(f"\n{self.locations[location]['description']}")
        self.action_menu(location)

    def action_menu(self, location):
         while True:
            print("\nWhat would you like to do?")
            for action in self.locations[location]["actions"]:
                print(f"- {action.capitalize()}")
            choice = input("\nType your action: ").strip().lower()
            if choice in self.locations[location]["actions"]:
                self.locations[location]["actions"][choice]()
                break 
            else:
                print("Invalid choice. Try again.")
            self.action_menu(self.current_location)

    
 # ----------------------------- STUDY ACTIONS ---------------------------------------   
    # DESK PUZZLE -------------------------------
    def search_desk(self):
        pass
    
    # BOOK PUZZLE -------------------------------
    def look_bookshelf(self):
        print("\nYou see a collection of dusty books. One book stands out.")
        choice = input("Pull the largest book? (yes/no): ").strip().lower()
        if choice == "yes":
            self.book_puzzle()
        else:
            print("You leave the bookshelf as it is.")
        self.action_menu(self.current_location)
    def book_puzzle(self):
        print("\nA hidden compartment opens, revealing a coded message!")
        answer = input("Solve the puzzle: What is 5 + 3? ").strip()
        if answer == "8":
            print("Correct! You found a clue: 'The truth lies beneath.'")
        else:
            print("Incorrect. The message remains a mystery.")
        self.action_menu(self.current_location)
    
    # RUG CLUE -------------------------------
    def examine_rug(self):
        pass

 # ----------------------------- KITCHEN ACTIONS ---------------------------------------   
    def look_fridge(self):
        pass
    def examine_countertops(self):
        pass
    def check_pantry(self):
        pass

 # ----------------------------- BEDROOM ACTIONS ---------------------------------------   
    def search_closet(self):
        pass
    def examine_body(self):
        pass
    def check_nightstand(self):
        pass

 # ----------------------------- ENTRYWAY ACTIONS ---------------------------------------   
    def look_coat_rack(self):
        pass
    def check_mirror(self):
        pass
    def examine_door(self):
        pass
# ----------------------------- MAIN COMMANDS ---------------------------------------

    def handle_input(self, command):
        if command == "look":
            self.show_location()
        elif command.startswith("go "):
            new_location = command.split(" ", 1)[1]
            if new_location in self.locations:
                self.enter_location(new_location)  
            else:
                print("You can't go there.")
        elif command == "quit":
            self.running = False
        else:
            print("Invalid command.")

    def start(self):
        self.show_intro()
        self.show_location()
        self.action_menu(self.current_location)
        while self.running:
            command = input("\nWhat do you want to do? ").strip().lower()
            self.handle_input(command)
            break

if __name__ == "__main__":
    game = MysteryGame()
    game.start()