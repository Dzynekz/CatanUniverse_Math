class Deck():
    def __init__(self) -> None:
        self.cards = self._initialize_deck()
        self.knights = 14
        self.victorypoints = 5
        self.yearofplenty = 2
        self.roadbuilding = 2
        self.monopolty = 2

    def _initialize_deck(self) -> list:
        cards = []
        for _ in range(25):
            card = Unknown()
            cards.append(card)
        return cards
    
    def __str__(self) -> str:
        return (f"Deck: {len(self.cards)} cards remaining")

    def get_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()


class Card():
    COST = {'sheep':1, 'grain':1, 'ore':1}

    def __init__(self) -> None:
        pass

class Unknown(Card):
    '''You don't know what kind of card other players have'''
    def __init__(self) -> None:
        super().__init__()   

class VictoryPoint(Card):
    '''Gives one victory point'''
    def __init__(self) -> None:
        super().__init__()

class Knight(Card):
    '''Gives knight.
    If you have most knights in game (starting from 3) you get 2 points'''
    def __init__(self) -> None:
        super().__init__()
    
class RoadBuilding(Card):
    '''Gives 2 roads
     If you have most roads in game (starting from 3) you get 2 points'''
    def __init__(self) -> None:
        super().__init__()

class YearOfPlenty(Card):
    '''You can take any 2 recources cards from the supply stacks'''
    def __init__(self) -> None:
        super().__init__()

class Monopoly(Card):
    '''You can choose one resource and take all of it from other players hands'''
    def __init__(self) -> None:
        super().__init__()
