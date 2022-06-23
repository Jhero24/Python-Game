# Jeremy Robinson and the Tiny dog Adventure

# A dictionary for the simplified dog text game
# The dictionary links a room to other rooms.
# Define dictionary
rooms = {'Living room': {'name': 'Living room', 'east': 'Bedroom', 'north': 'Kitchen', 'west': 'Basement',
                         'south': 'Playroom', 'contents': [],
                         'text': 'Woof.'},

         'Playroom': {'name': 'the Playroom', 'east': 'Sun room', 'north': 'Living room',
                      'contents': ['Tennis Ball of Hope'],
                      'text': 'Bark.'},

         'Sun room': {'name': 'Sun room', 'west': 'Playroom', 'contents': ['The pet of courage'],
                      'text': 'Sniff Sniff'},

         'Basement': {'name': 'Basement', 'east': 'Living room', 'contents': ['Collar of Justice'],
                      'text': 'WOOF WOOF.'},

         'Kitchen': {'name': 'the Kitchen', 'east': 'Laundry room', 'south': 'Living room',
                     'contents': ['Treat of Yumminess'],
                     'text': 'BARK BARK.'},

         'Laundry room': {'name': 'Laundry room', 'west': 'Kitchen', 'contents': ['Socks of Smelliness'],
                          'text': 'woof!'},

         'Bedroom': {'name': 'Bedroom', 'west': 'Living room', 'north': 'Closet', 'contents': ['The Bed of Sleeping'],
                     'text': 'Bark Bark.'},

         'Closet': {'name': 'Closet', 'South': 'Bedroom', 'contents': ['The Vacuum'],
                    'text': 'Bark.'},
         }

directions = ['north', 'south', 'east', 'west']
current_room = rooms['Living room']
carrying = []


# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Welcome to tiny dog adventure")
    print("Collect 6 items to defeat the evil vacuum cleaner")
    print("Move commands: north, south, east, west")
    print("Add to Inventory: get 'item name'")


while True:
    # display current location
    print()
    print('Tiny dog is in the {}.'.format(current_room['name']))
    print("inventory:", carrying)
    print(current_room['text'])

    if current_room['contents']:
        item = current_room["contents"]
        if item not in carrying:
            print('Tiny dog sees a: {}'.format(', '.join(current_room['contents'])))
    # getting the user input
    command = input('What should Tiny Dog do?').strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            print(' You cannot go that way tiny dog')
    # quitting the game
    elif command.lower() in ('quit'):
        print('Thank you for playing')
        break
    # gather objects
    elif command.lower().split()[0] == 'get':
        user_item = command
        if user_item == "get " + item[0]:
            carrying.append(item)
            print(item, "collected")
        else:
            print("That item is not here.")
    # bad command
    else:
        print("invalid command")

    if current_room["name"] == "Closet":
        if len(carrying) == 6:
            print("You win")
        else:
            print("You lose")
        break

