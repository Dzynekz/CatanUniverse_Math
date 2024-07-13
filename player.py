from buildings import Building, Village, City, Road
from cards import Card, Unknown, Knight, VictoryPoint, Monopoly, YearOfPlenty, RoadBuilding
from deck import Deck

class Player():
    MAX_VILLAGES = 5
    MAX_CITIES = 4
    MAX_ROADS = 15
    
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color
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
        self.longest_road = 0

    def get_name(self) -> str:
        return self.name
    
    def get_color(self) -> str:
        return self.color
    
    def get_points(self) -> int:
        return self.points
    
    def get_buildings(self, building) -> int:
        return self.buildings[building]
    
    def get_resources(self) -> int:
        return self.resources
    
    def get_knights(self) -> int:
        return self.knights
    
    def get_cards(self) -> list:
        return self.cards
    
    def get_longest_road(self) -> int:
        return self.longest_road
    
    def add_resources(self, resource, quantity):
        '''Not sure if resources shouldn't be a different class'''
        if resource in self.resources:
            self.resources[resource] += quantity
    
    def have_enough_resources(self, resources_needed: dict) -> bool:
        for key, value in resources_needed.items():
            if self.resources[key] < value:              
                return False
        return True
    
    def use_resources(self, resources_needed: dict) -> None:
        for key, _ in self.resources.items():
            if key in resources_needed:
                self.resources[key] -= resources_needed[key]

    def add_card(self, deck: Deck) -> None:
        if self.use_resources(Card.COST):
            card = deck.get_card()
            if card is None:
                print("There is no cards left in deck")
            else:
                self.cards.append(card)               

    def use_card(self, card_type, game_state, resource_monopoly = 0, resource_year_of_plenty = {}):
            '''remember to change info about remainings cards in deck i.e. knights'''
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

        


    
    
    

                
