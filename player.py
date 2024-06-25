from buildings import Building, Village, City, Road
import gamestate

class Player():
    MAX_VILLAGES = 5
    MAX_CITIES = 4
    MAX_ROADS = 15
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.points = 0
        self.victory_point_cards = 0
        self.knights = 0
        self.buildings = {
            'villages': 0,
            'cities': 0,
            'roads': 0
        }
        self.resources = {'wood': 0, 'brick': 0, 'sheep': 0, 'grain': 0, 'ore': 0}
    
    def add_building(self, building: Building) -> None:
        if isinstance(building, Village):
            if self.buildings['villages'] < Player.MAX_VILLAGES:
                self.buildings['villages'] += 1
                self.points += 1
        elif isinstance(building, City):
            if self.buildings['cities'] < Player.MAX_CITIES and self.buildings['villages'] > 0:
                self.buildings['cities'] += 1
                self.buildings['villages'] -= 1
                self.points += 1
        elif isinstance(building, Road):    
            self.buildings['roads'] += 1
            '''If you have the most roads in a game and more than 3 you get +2 points,
                at the same time, if someone will surpass you, you lose 2 points'''

                
