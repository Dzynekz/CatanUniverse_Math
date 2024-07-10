import networkx as nx
import matplotlib.pyplot as plt
from searching_for_resources import board_resources
from searching_for_numbers import board_numbers

G = nx.Graph()

rows = 12 
vertex = 1
in_row_vertex = 3
for i in range(1,rows):
    if i < 7:
        if i%2 !=0:
            for j in range(1, in_row_vertex+1):             
                left_child = vertex + in_row_vertex  
                right_child = vertex + in_row_vertex + 1 
                G.add_edge(vertex, left_child)
                G.add_edge(vertex, right_child)
                vertex += 1
            in_row_vertex += 1
        else:
            for j in range(1, in_row_vertex+1):
                child = vertex + in_row_vertex
                G.add_edge(vertex, child)
                vertex += 1
    else:
        if i%2 !=0:
            for j in range(1, in_row_vertex+1):
                if j == 1:
                    child = vertex + in_row_vertex
                    G.add_edge(vertex, child)
                    G[vertex][child]['road'] = None
                elif j == in_row_vertex:
                    child = vertex + in_row_vertex -1
                    G.add_edge(vertex, child)
                    G[vertex][child]['road'] = None
                else:    
                    left_child = vertex + in_row_vertex - 1  # Calculate the left child
                    right_child = vertex + in_row_vertex  # Calculate the right child
                    G.add_edge(vertex, left_child)
                    G.add_edge(vertex, right_child)
                    G[vertex][left_child]['road'] = None
                    G[vertex][right_child]['road'] = None
                vertex += 1
            in_row_vertex -= 1
        else:
            for j in range(1, in_row_vertex+1):
                child = vertex + in_row_vertex
                G.add_edge(vertex, child)
                G[vertex][child]['road'] = None
                vertex += 1

for node in G.nodes:
    G.nodes[node]['building_type'] = None
    G.nodes[node]['player'] = None

fields = [
        [1,4,5,8,9,13],
        [2,5,6,9,10,14],
        [3,6,7,10,11,15],
        [8,12,13,17,18,23],
        [9,13,14,18,19,24],
        [10,14,15,19,20,25],
        [11,15,16,20,21,26],
        [17,22,23,28,29,34],
        [18,23,24,29,30,35],
        [19,24,25,30,31,36],
        [20,25,26,31,32,37],
        [21,26,27,32,33,38],
        [29,34,35,39,40,44],
        [30,35,36,40,41,45],
        [31,36,37,41,42,46],
        [32,37,38,42,43,47],
        [40,44,45,48,49,52],
        [41,45,46,49,50,53],
        [42,46,47,50,51,54]
        ]

hexagons = {}
for i in range(19):
    hexagons[f'H{i+1}']= {
                'resource': board_resources['resource_type'][i],
                'number': board_numbers['number'][i],
                'fields': fields[i]}

pos = {
    1: (2, 5), 2: (4, 5), 3: (6, 5),
    4: (1, 4), 5: (3, 4), 6: (5, 4), 7: (7, 4),
    8: (1, 3), 9: (3, 3), 10: (5, 3), 11: (7, 3),
    12: (0, 2), 13: (2, 2), 14: (4, 2), 15: (6, 2), 16: (8, 2),
    17: (0, 1), 18: (2, 1), 19: (4, 1), 20: (6, 1), 21: (8, 1),
    22: (-1, 0), 23: (1, 0), 24: (3, 0), 25: (5, 0), 26: (7, 0), 27: (9, 0),
    28: (-1, -1), 29: (1, -1), 30: (3, -1), 31: (5, -1), 32: (7, -1), 33: (9, -1),
    34: (0, -2), 35: (2, -2), 36: (4, -2), 37: (6, -2), 38: (8, -2),
    39: (0, -3), 40: (2, -3), 41: (4, -3), 42: (6, -3), 43: (8, -3),
    44: (1, -4), 45: (3, -4), 46: (5, -4), 47: (7, -4),
    48: (1, -5), 49: (3, -5), 50: (5, -5), 51: (7, -5),
    52: (2, -6), 53: (4, -6), 54: (6, -6)
}
    
# Define player colors
player_colors = {
    'player1': 'red',
    'player2': 'blue',
    'player3': 'green',
    'player4': 'yellow'
}
# Assign players to nodes for testing
G.nodes[1]['player'] = 'player1'
G.nodes[5]['player'] = 'player2'
G.nodes[10]['player'] = 'player3'
G.nodes[15]['player'] = 'player4'
# Generate colors for nodes based on players
node_colors = []
for node in G.nodes:
    player = G.nodes[node]['player']
    if player is not None:
        node_colors.append(player_colors[player])
    else:
        node_colors.append('lightblue')  # Default color for unassigned nodes



# Define road colors
road_colors = {
    'player1': 'red',
    'player2': 'blue',
    'player3': 'green',
    'player4': 'yellow',
    None: 'black'  # Default color for unassigned roads
}
# Assign roads to edges for testing
G.edges[1, 5]['road'] = 'player1'
G.edges[5, 9]['road'] = 'player2'
G.edges[10, 14]['road'] = 'player3'
G.edges[15, 20]['road'] = 'player4'
# Generate colors for edges based on players
edge_colors = []
for edge in G.edges:
    road = G.edges[edge].get('road')
    edge_colors.append(road_colors.get(road, 'black'))  # Default color for unassigned roads



plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=500, font_size=10, font_color='black')
plt.show()
