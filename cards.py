class Card():
    def __init__(self) -> None:
        pass

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
