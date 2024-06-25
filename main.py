from gamestate import GameState
from buildings import Village, City, Road

def main():
    game_state = GameState()
    
    # Dodawanie graczy dynamicznie
    game_state.add_player("Player 1")
    game_state.add_player("Player 2")
    game_state.add_player("Player 3")