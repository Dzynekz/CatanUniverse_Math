from player import Player
from board import Board

class GameState():
    def __init__(self) -> None:
        self.players = []
        self.round = 1
        self.player_with_longest_road = None
        self.player_with_most_knights = None

    def add_round(self) -> None:
        self.round +=1

    def add_board(self) -> dict:
        board = Board()
        return board
    
    def add_player(self, name: str, color: str) -> None:
        new_player = Player(name, color)
        self.players.append(new_player)
        return new_player
    
    def get_player(self, name: str) -> Player:
        for player in self.players:
            if player.name == name:
                return player
    
    def get_player_with_longest_road(self) -> Player:
        return self.player_with_longest_road 
    
    def get_player_with_most_knights(self) -> Player:
        return self.player_with_most_knights

    def player_with_longest_roads_update(self, player: Player) -> None:        
        if self.player_with_longest_road is None or player.get_buildings('roads') > self.player_with_longest_road.get_buildings('roads'):
            old_player = self.player_with_longest_road
            self.player_with_longest_road = player
            if old_player:
                old_player.points -= 2
            player.points += 2

    def player_with_most_knights_update(self, player: Player) -> None:
        if self.player_with_most_knights is None or player.get_knights() > self.player_with_most_knights.get_knights():
            old_player = self.player_with_most_knights
            self.player_with_most_knights = player
            if old_player:
                old_player.points -= 2
            player.points += 2
