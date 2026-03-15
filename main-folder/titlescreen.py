# Main Menu, this sucks, had 3 functions at the start, now it's all in one
def title_screen_options():
    import sys
    import os
    valid_command = False
    while valid_command == False: 
        # Main menu text
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to Placeholder Text-Based RPG Game')
        print("Type 'play' to start the game")
        print("Type 'help' to open the help menu")
        print("Type 'quit' to close the game") 
        option = input('>').lower()
        # play option
        if option == 'play':
            valid_command = True
            print('do you wish to [Start a New Game (new)]')
            print('or do you wish to [Load Game (load)]')
            answer = input('>').lower()
            
            # Load game
            if answer == 'load':
                return 'load'
            
            # New game
            elif answer == 'new':
                print('are you sure, doing this will wipe your save file? Y/N')
                yes_no = input('>').lower()
                
                # Wipe save file
                if yes_no == 'y':
                    return 'wipe'
                
                # Not wipe save file
                elif yes_no == 'n':   
                    valid_command = False
            
            else:
                print("invalid command, command must be 'new' or 'load'")
                valid_command = False
        
        # Help menu, still not very helpfull
        if option == 'help':
            valid_command = False
            print(""" 
================================================================================================================================                
| Note: all commands must be typed exactly or you will get a 'invalid command' prompt.                                         |
|                                                                                                                              |
| Commands: ['look' or 'examine'] to get a name, description and items that can be picked up;                                  |
|                                                                                                                              |
| ['status' or 'stats'] to see the status menu;                                                                                |
|                                                                                                                              |
| ['take' or 'get'] to get the items you see using ['look' or 'examine'],                                                      |
|                                                                                                                              |
| after typing one of the 'take' commands you must type the name of the item;                                                  |
|                                                                                                                              |
| ['switch', 'change', 'equip' or 'swap'] to change current weapon, after typing the command you must enter the weapon's name; |
|                                                                                                                              |
| ['move', 'go', 'travel'] to move, after typing the command you must also                                                     |
| type one of the four cardinal directions ['north', 'south', 'east' or 'west];                                                |
|                                                                                                                              |
| ['quit'] to quit the game, it will also auto save before exiting;                                                            |
|                                                                                                                              |
| ['save'] to save the game;                                                                                                   |
|                                                                                                                              |
| Note 2: you can use 'Enter' to skip 1 turn.                                                                                  |
================================================================================================================================
""")
            input('>')
        
        # Quit
        if option == 'quit':
            valid_command = True
            sys.exit()
        
        else:
            print("no such command, valid commands: 'play', 'help', 'quit'")
            valid_command = False
