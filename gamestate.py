from player import Player

class GameState():
    def __init__(self) -> None:
        self.players = []
    
    def add_player(self, name: str) -> None:
        new_player = Player(name)
        self.players.append(new_player)
    
    '''def get_player_with_most_roads(self) -> Player:
        if not self.players:
            return None
        return max(self.players, key=lambda player: player.buildings['roads'])'''