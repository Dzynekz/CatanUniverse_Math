from buildings import Building, Village, City, Road

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

    def get_name(self) -> str:
        return self.name
    
    def add_building(self, building: Building, game_state) -> None:
        if isinstance(building, Village):
            if self.buildings['villages'] < self.MAX_VILLAGES:
                self.buildings['villages'] += 1
                self.points += 1
        elif isinstance(building, City):
            if self.buildings['cities'] < self.MAX_CITIES and self.buildings['villages'] > 0:
                self.buildings['cities'] += 1
                self.buildings['villages'] -= 1
                self.points += 1
        elif isinstance(building, Road):    
            self.buildings['roads'] += 1
            game_state.player_with_longest_roads_update(self)

    
    def get_buildings(self, building) -> int:
        return self.buildings[building]
    
    def get_recources(self, recourse) -> int:
        return self.resources[recourse]
    

                
