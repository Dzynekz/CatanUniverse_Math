from player import Player

class GameState():
    def __init__(self) -> None:
        self.players = []
        self.player_with_longest_road = None
        self.player_with_most_knights = None
    
    def add_player(self, name: str) -> None:
        new_player = Player(name)
        self.players.append(new_player)
    
    def get_player(self, name: str) -> Player:
        for player in self.players:
            if player.name == name:
                return player
    
    def get_player_with_longest_road(self) -> Player:
        return self.player_with_longest_road 

    def player_with_longest_roads_update(self, player: Player) -> None:        
        if self.player_with_longest_road is None or player.get_buildings('roads') > self.player_with_longest_road.get_buildings('roads'):
            old_player = self.player_with_longest_road
            self.player_with_longest_road = player
            if old_player:
                old_player.points -= 2
            player.points += 2

    def player_with_most_knights_update(self) -> Player:
        pass





    
    '''def get_player_with_most_roads(self) -> Player:
        if not self.players:
            return None
        return max(self.players, key=lambda player: player.buildings['roads'])'''