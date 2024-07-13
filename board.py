import networkx as nx
import matplotlib.pyplot as plt
from searching_for_resources import board_resources
from searching_for_numbers import board_numbers
from buildings import Building, Village, City, Road
from player import Player
from collections import deque

class Board():
    ROWS = 12

    def __init__(self) -> None:
        self.hexagons = {}
        self.graph = nx.Graph()
        vertex = 1
        in_row_vertex = 3
        for i in range(1,self.ROWS):
            if i < 7:
                if i%2 !=0:
                    for j in range(1, in_row_vertex+1):             
                        left_child = vertex + in_row_vertex  
                        right_child = vertex + in_row_vertex + 1 
                        self.graph.add_edge(vertex, left_child)
                        self.graph.add_edge(vertex, right_child)
                        vertex += 1
                    in_row_vertex += 1
                else:
                    for j in range(1, in_row_vertex+1):
                        child = vertex + in_row_vertex
                        self.graph.add_edge(vertex, child)
                        vertex += 1
            else:
                if i%2 !=0:
                    for j in range(1, in_row_vertex+1):
                        if j == 1:
                            child = vertex + in_row_vertex
                            self.graph.add_edge(vertex, child)
                            self.graph[vertex][child]['road'] = None
                        elif j == in_row_vertex:
                            child = vertex + in_row_vertex -1
                            self.graph.add_edge(vertex, child)
                            self.graph[vertex][child]['road'] = None
                        else:    
                            left_child = vertex + in_row_vertex - 1  # Calculate the left child
                            right_child = vertex + in_row_vertex  # Calculate the right child
                            self.graph.add_edge(vertex, left_child)
                            self.graph.add_edge(vertex, right_child)
                            self.graph[vertex][left_child]['road'] = None
                            self.graph[vertex][right_child]['road'] = None
                        vertex += 1
                    in_row_vertex -= 1
                else:
                    for j in range(1, in_row_vertex+1):
                        child = vertex + in_row_vertex
                        self.graph.add_edge(vertex, child)
                        self.graph[vertex][child]['road'] = None
                        vertex += 1

        for node in self.graph.nodes:
            self.graph.nodes[node]['building_type'] = None
            self.graph.nodes[node]['player'] = None

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

        for i in range(19):
            self.hexagons[f'H{i+1}']= {
                        'resource': board_resources['resource_type'][i],
                        'number': board_numbers['number'][i],
                        'fields': fields[i]}
            
    def show(self, gamestate):
        from gamestate import GameState
        if not isinstance(gamestate, GameState):
            raise TypeError("gamestate must be an instance of GameState")
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
        
        player_colors = {None: 'lightblue'}
        for player in gamestate.players:
            player_colors[player.name] = player.color
        # Generate colors for nodes based on players
        node_colors = []
        node_shapes = []
        for node in self.graph.nodes:
            player = self.graph.nodes[node]['player']
            building_type = self.graph.nodes[node]['building_type']

            if player is not None:
                node_colors.append(player_colors[player])
                if building_type == 'village':
                    node_shapes.append('o')  # Circle for village
                elif building_type == 'city':
                    node_shapes.append('s')  # Square for city
                else:
                    node_shapes.append('o')  # Default shape
            else:
                node_colors.append('lightblue')  # Default color for unassigned nodes
                node_shapes.append('o')  # Default shape

        # Generate colors for edges based on players
        edge_colors = []
        for edge in self.graph.edges:
            road = self.graph.edges[edge].get('road')
            edge_colors.append(player_colors.get(road, 'black'))  # Default color for unassigned roads
        
        plt.figure(figsize=(12, 8))
        for shape in set(node_shapes):
            nx.draw(self.graph, pos, with_labels=True, node_color=[node_colors[i] for i in range(len(node_shapes)) if node_shapes[i] == shape], 
                edge_color=edge_colors, node_size=500, font_size=10, font_color='black', nodelist=[node for i, node in enumerate(self.graph.nodes) if node_shapes[i] == shape], node_shape=shape) 
        plt.show()

    def get_hexagon(self, hex):
            for key, value in self.hexagons.items():
                if key == hex:
                    print(f'{key}: {value}')
    
    def assign_player_node(self, node: int, player_name, building_type):
        if (self.graph.nodes[node]['player'] == None) or (self.graph.nodes[node]['player'] == player_name and building_type == 'city'):
            self.graph.nodes[node]['player'] = player_name 
            self.graph.nodes[node]['building_type'] = building_type
        else:
            print("Someone already took it!")

    def assing_player_edge(self, node1: int, node2: int, player_name):
        if (node1, node2) in self.graph.edges or (node2, node1) in self.graph.edges:
            if self.graph.edges[node1, node2].get('road') is None:
                self.graph.edges[node1, node2]['road'] = player_name
            else:
                print("Someone already took it!")
        else:
            print("No edge exists between the specified nodes!")
    
    def check_build_possibility(self, node: int, player_name, gamestate) -> bool:
        from gamestate import GameState
        if gamestate.round == 1: #### First 6 rounds have different rules
            return True
        
        has_road = any(
            (node, neighbor) in self.graph.edges and self.graph.edges[node, neighbor].get('road') == player_name 
            for neighbor in self.graph.neighbors(node)
            )
        
        if not has_road:
            print("You dont have a road to this node")
            return False

        for neighbor in self.graph.neighbors(node):
            if self.graph.nodes[neighbor]['building_type']:
                print("There is already a building near")
                return False
        return True
    
    def check_road_possibility(self, node1: int, node2: int, player_name) -> bool:
        if self.graph.edges[node1, node2].get('road'):
            print("There is a road already here")
            return False

        if self.graph.nodes[node1]['player'] == player_name or self.graph.nodes[node2]['player'] == player_name:
            return True
        
        has_road = any(
        (node1, neighbor) in self.graph.edges and self.graph.edges[node1, neighbor].get('road') == player_name
        for neighbor in self.graph.neighbors(node1)
        ) or any((node2, neighbor) in self.graph.edges and self.graph.edges[node2, neighbor].get('road') == player_name
        for neighbor in self.graph.neighbors(node2)
        )
        if not has_road:
            print("You dont have a roads nearby")
            return False
        return True
    

    def add_building(self, building: Building, game_state, player: Player, node1, node2=0):
        if isinstance(building, Village):
            if self.check_build_possibility(node1, player.name, game_state):                
                if player.have_enough_resources(Village.COST):
                    if player.buildings['villages'] < player.MAX_VILLAGES:
                        player.use_resources(Village.COST)                   
                        player.buildings['villages'] += 1
                        player.points += 1
                        self.assign_player_node(node1, player.name, 'village')
                    else:
                        return "You dont have any villages left"
                else:
                    return 'Not enough resources'

        elif isinstance(building, City):
            if self.check_build_possibility(node1, player.name, game_state): 
                if player.have_enough_resources(City.COST):                  
                    if player.buildings['cities'] < player.MAX_CITIES and self.graph.nodes[node1]['building_type'] == 'village':   
                        player.use_resources(City.COST)           
                        player.buildings['cities'] += 1
                        player.buildings['villages'] -= 1
                        player.points += 1
                        self.assign_player_node(node1, player.name, 'city')
                    elif self.graph.nodes[node1]['building_type'] != 'village':
                        print('You need to build a village first')
                else:
                    print('Not enough resources')
        elif isinstance(building, Road):    
            if self.check_road_possibility(node1, node2, player.name):
                if player.have_enough_resources(Road.COST):
                    player.use_resources(Road.COST)
                    player.buildings['roads'] += 1
                    self.assing_player_edge(node1, node2, player.name)
                    road = game_state.player_with_longest_roads_update(self, player)
                    player.longest_road = road
                else:
                    print('Not enough resources')
        else:
            print('Invalid building type')

        
    def dfs_longest_path(self, graph, start, visited, current_length):
        longest_path = []
        longest_length = current_length

        for neighbor in graph.neighbors(start):
            if (start, neighbor) not in visited:
                visited.add((start, neighbor))
                visited.add((neighbor, start))
                path, length = self.dfs_longest_path(graph, neighbor, visited, current_length + 1)
                if length > longest_length:
                    longest_path = path
                    longest_length = length
                # Remove edge from visited after the recursive call
                visited.remove((start, neighbor))
                visited.remove((neighbor, start))

        return [start] + longest_path, longest_length
    
    def find_longest_path_in_component(self, graph, component):
        longest_path = []
        longest_length = 0
        for node in component:
            path, length = self.dfs_longest_path(graph, node, set(), 0)
            if length > longest_length:
                longest_path = path
                longest_length = length
        return longest_path, longest_length

    def find_longest_path_by_player(self, player):
        player_edges = [(u, v) for u, v, attr in self.graph.edges(data=True) if attr.get('road') == player.name]

        if not player_edges:
            return [], 0

        player_graph = nx.Graph()
        player_graph.add_edges_from(player_edges)

        components = list(nx.connected_components(player_graph))
        longest_path = []
        longest_length = 0

        for component in components:
            path, length = self.find_longest_path_in_component(player_graph, component)
            if length > longest_length:
                longest_path = path
                longest_length = length

        return longest_path, longest_length


    # method prints longest path of given tree
    '''def LongestPathLength(self):
 
        # first DFS to find one end point of longest path
        node, _ = self.BFS(0)
 
        # second DFS to find the actual longest path
        node_2, long_dis  = self.BFS(node)
 
        print('Longest path is from', node, 'to', node_2, 'of length', long_dis )'''