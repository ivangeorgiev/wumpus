
from random import choice

def create_tunnel(cave_from, cave_to):
    """Create a tunnel between cave_from and cave_to"""
    caves[cave_from].append(cave_to)
    caves[cave_to].append(cave_from)
    
def visit_cave(cave_number):
    """Mark a cave as visited"""
    visited_caves.append(cave_number)
    unvisited_caves.remove(cave_number)
    
def pick_cave(cave_list):
    """Pick a cave from a list. The cave should 
    have less than 3 tunnels."""
    cave_number = choice(cave_list)
    while len(caves[cave_number]) >= 3:
        cave_number = choice(cave_list)
    return cave_number
    
def print_caves(label=""):
    """Print out the current cave structure."""
    print('-----'+str(label)+'-----------')
    for number in cave_numbers:
        print(number, ":", caves[number])
    print('-----------------')

def setup_caves(cave_numbers):
    """Create the starting list of cave tunnels."""
    for cave in cave_numbers:
        caves.append([])

def link_caves():
    visit_cave(0)

    # Generate traversable cave system
    while unvisited_caves != []:
        i = pick_cave(visited_caves)

        next_cave = choice(unvisited_caves)
        visit_cave(next_cave)
        create_tunnel(i, next_cave)
           
        
def finish_tunnels():
    """Make sure there are three tunnels going out
    of a cave by adding one way tunnels."""
    for cave_number in cave_numbers:
        while len(caves[cave_number]) < 3:
            passage_to = cave_number
            while passage_to == cave_number or passage_to in caves[cave_number]:
                passage_to = choice(cave_numbers)
            caves[cave_number].append(passage_to)
        caves[cave_number].sort()
            
            
########################################################################################
def print_location(player_location):
    print("You are in cave", player_location)
    print("From here you can enter caves ", caves[player_location])
    if (wumpus_location in caves[player_location]):
        print("I smell a wumpus!")

def get_next_location():
    print("Which cave next "+str(caves[player_location])+"?")
    player_input = input(">")
    
    if (not player_input.isdigit()) or (int(player_input)not in caves[player_location]) :
        print(player_input, "is not a cave you can enter")
        return None
    else:
        return int(player_input)

########################################################################################

NUM_CAVES = 20

cave_numbers = range(0, NUM_CAVES)
caves = []
unvisited_caves = list(cave_numbers)
visited_caves = []
setup_caves(cave_numbers)
link_caves()    
finish_tunnels()
print_caves("Final")

# Initialize player and wumpus locations
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)

while player_location == wumpus_location :
    player_location = choice(cave_numbers)
    
# Welcome the player
print("Welcome to Hunt the Wumpus!")
print("There are", NUM_CAVES, " caves")
print("To play, just type the number")
print("of the cave you wish to enter next");
print()

# The game loop
while True:
    print_location(player_location)
    player_location = get_next_location()
    if player_location is None:
        continue
    elif player_location == wumpus_location:
        print("Aargh! You got eaten by a wumpus!")
        break
