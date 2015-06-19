
from random import choice

NUM_CAVES = 20

cave_numbers = range(0, NUM_CAVES)
caves = [] # cave transitions/passages
unvisited_caves = []
for i in cave_numbers:
    caves.append([])
    unvisited_caves.append(i)

visited_caves = [0]
unvisited_caves.remove(0)

# Generate traversable cave system
while unvisited_caves != []:
    i = choice(visited_caves)
    if len(caves[i]) > 3:
        continue
    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)
    
    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)
    
    print('-----', next_cave, '-----------')
    print('visited: ', visited_caves)
    print('unvisited: ', unvisited_caves)
    for number in cave_numbers:
        print(number, ":", caves[number])
    print('-----------------')

# Extend passages so each cave has at least 3 exits
for i in cave_numbers:
    while len(caves[i]) < 3:
        passage_to = i
        while passage_to == i or passage_to in caves[i]:
            passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
    caves[i].sort()
        
print('---------------------')
for number in cave_numbers:
    print(number, ":", caves[number])
print('-----------------')

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
    print("You are in cave", player_location)
    print("From here you can enter caves ", caves[player_location])
    if (wumpus_location in caves[player_location]):
        print("I smell a wumpus!")
    
    print("Which cave next "+str(caves[player_location])+"?")
    player_input = input(">")
    
    if (not player_input.isdigit()) or (int(player_input)not in caves[player_location]) :
        print(player_input, "is not a cave you can enter")
        continue
    player_location = int(player_input)
    if player_location == wumpus_location:
        print("Aargh! You got eaten by a wumpus!")
        break
