from room import Room
from player import Player
from world import World
from graph_class import Graph
from queue_stack import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

################################ MY CODE ################################
############################### Functions ###############################

def bfs(self, starting_vertex):
    queue = Queue()
    visited_vertices = set()

    queue.enqueue({
        'current_vertex': starting_vertex,
        'path': [starting_vertex]
    })

    while queue.size() > 0:
        current_obj = queue.dequeue()
        current_path = current_obj['path']
        current_vertex = current_obj['current_vertex']

        if current_vertex not in visited_vertices:

            # if current_vertex == destination_vertex:
            #     return current_path

            visited_vertices.add(current_vertex)

            # Find the neighboring rooms of the current room and add them to the queue

            # If any of the neighboring rooms has an exit direction of '?' then return that path / add it to the traversal path / move to that room and do another dft.

            for neighbor_vertex in self.get_neighbors(current_vertex):
                new_path = list(current_path)
                new_path.append(neighbor_vertex)

                queue.enqueue({
                    'current_vertex': neighbor_vertex,
                    'path': new_path
                    })



def dft(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """

    # Create an empty Stack and push the starting_vertex onto it
    stack = Stack()
    stack.push(starting_vertex)

    # Create an empty set to track visited verticies
    visited_vertices = set()
    
    # while stack is not empty:
    while stack.size() > 0:
        # Get the current vertex (pop from stack)
        current_vertex = stack.pop()

        # Check to see if the current vertex has not been visited. If it hasn't been visited:
        if current_vertex not in visited_vertices:
            # Mark the current vertex as being visited (Add the current vertex to a visted_set)
            visited_vertices.add(current_vertex)


            # Get the exits of that room ***THERE IS A FUNCTION IN THE ROOM CLASS TO GET THE EXITS

            # For each of the exits in the room, if the value of the exit is '?' then add that key to the stack and/or traversal_path

            # Move to the new room
            # Create a variable for the new room number

            # When you move to that unexplored room you need to add the old room to the value of the opposite direction of the new room and add the new room to the direction that you moved when coming from the old room.
                # i.e.
                # if moved north:
                    # old_room[north] = new_room_number
                    # new_room[south] = old_room_number
                # if moved south:
                    # old_room[south] = new_room_number
                    # new_room[north] = old_room_number
                # if moved east:
                    # old_room[east] = new_room_number
                    # new_room[west] = old_room_number
                # if moved west:
                    # old_room[west] = new_room_number
                    # new_room[east] = old_room_number
                #*** THERE IS A FUNCTION IN THE ROOM CLASS THAT WILL CONNECT ROOMS FOR YOU ***#

            # If the new room is not in the visited rooms then repeat.
            # If you reach a room that does not have a '?' in any direction then do a breadth first search to find a path that reaches a direction with a '?'. Then add that path to the queue and move there and perform another dft.

############################### Code That Just Runs ###############################
swapped_directions = {"n":"s", "s": "n", "e": "w", "w":"e"}

previous_directions = []

rooms_i_visited = {}

rooms_i_visited[player.current_room.id] = player.current_room.get_exits()
print("Rooms_i_visited: ", rooms_i_visited)

initial_room = player.current_room.id
exits = player.current_room.get_exits()

previous_room = None

print("exits:", exits)


while len(rooms_i_visited) < len(world.rooms):
    if player.current_room.id not in rooms_i_visited:
        rooms_i_visited[player.current_room.id] = player.current_room.get_exits()
        last_direction_traversed = previous_directions[-1]
        rooms_i_visited[player.current_room.id].remove(last_direction_traversed)

    while len(rooms_i_visited[player.current_room.id]) < 1:
        last_direction_traversed = previous_directions.pop()
        traversal_path.append(last_direction_traversed)
        player.travel(last_direction_traversed)
    
    direction_to_exit = rooms_i_visited[player.current_room.id].pop(0)
    traversal_path.append(direction_to_exit)
    previous_directions.append(swapped_directions[direction_to_exit])
    
    player.travel(direction_to_exit)

    if (len(world.rooms) - len(rooms_i_visited)) == 1:
        rooms_i_visited[player.current_room.id] = player.current_room.get_exits()
        





############################### END OF MY CODE ###############################



print(f'This is the starting room: {world.starting_room}')

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")






#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")





# Do a DFT to get to the end of the line.
# Then do BFS when stuck (at a point where there are no question marks) to find an empty room.

# Do BFS without moving the player.
    # Only move them when a path is found.
