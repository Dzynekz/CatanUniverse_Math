from player import Player
from board import Board

class GameState():
    def __init__(self) -> None:
        self.players = []
        self.round = 1
        self.player_with_longest_road = None
        self.longest_road = 2
        self.player_with_most_knights = None

    def add_round(self) -> None:
        self.round +=1
    
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
    
    def player_with_longest_roads_update(self, board: Board,player: Player):   
        _, road = board.find_longest_path_by_player(player)

        if road > player.longest_road:
            player.longest_road = road

        if road > self.longest_road and self.player_with_longest_road != player:
            self.player_with_longest_road = player
            self.longes_road = road
        return road

        

    def player_with_most_knights_update(self, player: Player) -> None:
        if self.player_with_most_knights is None or player.get_knights() > self.player_with_most_knights.get_knights():
            old_player = self.player_with_most_knights
            self.player_with_most_knights = player
            if old_player:
                old_player.points -= 2
            player.points += 2
