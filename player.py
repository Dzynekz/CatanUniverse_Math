from buildings import Building, Village, City, Road
from cards import Deck, Card, Unknown, Knight, VictoryPoint, Monopoly, YearOfPlenty, RoadBuilding

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
        self.cards = []

    def get_name(self) -> str:
        return self.name
    
    def get_points(self) -> int:
        return self.points
    
    def get_buildings(self, building) -> int:
        return self.buildings[building]
    
    def get_recources(self) -> int:
        return self.resources
    
    def get_knights(self) -> int:
        return self.knights
    
    def get_cards(self) -> list:
        return self.cards
    
    def add_resources(self, resource, quantity):
        '''Not sure if resources shouldn't be a different class'''
        if resource in self.resources:
            self.resources[resource] += quantity
    
    def use_resources(self, resources_needed: dict) -> bool:
        for key, value in resources_needed.items():
            if self.resources[key] < value:              
                return False
        for key, value in self.resources.items():
            if key in resources_needed:
                self.resources[key] -= resources_needed[key]
        return True
               
    def add_building(self, building: Building, game_state) -> None:
        if isinstance(building, Village):
            if self.use_resources(Village.COST):
                if self.buildings['villages'] < self.MAX_VILLAGES:
                    self.buildings['villages'] += 1
                    self.points += 1
            else:
                print('Not enough resources')
        elif isinstance(building, City):
            if self.use_resources(City.COST):
                if self.buildings['cities'] < self.MAX_CITIES and self.buildings['villages'] > 0:
                    self.buildings['cities'] += 1
                    self.buildings['villages'] -= 1
                    self.points += 1
                elif self.buildings['villages'] == 0:
                    print('You dont have a village, cant built a city')
            else:
                print('Not enough resources')
        elif isinstance(building, Road):    
            if self.use_resources(Road.COST):
                self.buildings['roads'] += 1
                game_state.player_with_longest_roads_update(self)
            else:
                print('Not enough resources')
    
    def add_card(self, deck: Deck) -> None:
        if self.use_resources(Card.COST):
            card = deck.get_card()
            if card is None:
                print("There is no cards left in deck")
            else:
                self.cards.append(card)

    def use_card(self, card_type, game_state, resource_monopoly = 0, resource_year_of_plenty = {}):
            if len(self.cards) > 0:
                self.cards.pop()
                if isinstance(card_type, Knight):
                    self.knights += 1
                    game_state.player_with_most_knights_update(self)
                elif isinstance(card_type, VictoryPoint):
                    self.points += 1
                elif isinstance(card_type, YearOfPlenty):
                    for key, value in resource_year_of_plenty:
                        self.resources[key] += value
                elif isinstance(card_type, RoadBuilding):
                    self.buildings['roads'] += 2
                elif isinstance(card_type, Monopoly):
                    for player in game_state.players:
                        if player == self:
                            pass
                        else:
                            self.resources[resource_monopoly] += player.resources[resource_monopoly]
                            player.resources[resource_monopoly] = 0
            else:
                print("You don't have any cards")

        


    
    
    

                
