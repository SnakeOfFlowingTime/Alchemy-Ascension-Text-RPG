import zones
# Interaction
def title_screen_options():
    import sys
    option = input('>').lower()
    if option == 'play':
        if start_game() == 'load':
            return 'load'
    if option == 'help':
        help_menu()
    if option == 'quit':
        sys.exit()
    while option not in ['play', 'help', 'quit']:
        print('please enter a valid option')
        option = input('>').lower()
        if option == 'play':
            if start_game() == 'load':
                return 'load'
        if option == 'help':
            help_menu()
        if option == 'quit':
            sys.exit()

# Main menu
def title_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to Placeholder Text-Based RPG Game')
    print("Type 'play' to start the game")
    print("Type 'help' to open the help menu")
    print("Type 'quit' to close the game")
    if title_screen_options() == 'load':
        return 'load'

# Help menu
def help_menu():
    print("use 'go' to move, 'take' to take items, 'look' to survey the surroundings")
    print("Type 'back' to go back to the main menu")
    if input('>').lower() == 'back':
        title_screen()

# Game start
def start_game():
    print('do you wish to [Start a New Game (new)]')
    print('or do you wish to [Load Game (load)]')
    answer = input('>').lower()
    if answer == 'load':
        return 'load'
    elif answer == 'new':
        print('are you sure, doing this will wipe your save file? Y/N')
        yes_no = input('>').lower()
        if yes_no == 'y':
            print(zones.zones['town square'].name + '\n' + zones.zones['town square'].description)
            return 'y'       
        elif yes_no == 'n':
            title_screen()
            return 'n'       
        else:
            print('invalid command')
            input('>')
            title_screen()
            return 'invalid command'
    else:
        print('invalid command')
        title_screen()
        return 'invalid command'