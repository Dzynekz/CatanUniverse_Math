from cards import Card, Unknown

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
    
    def get_number_of_cards(self):
        return len(self.cards)
    
    def get_number_of_knights(self):
        return self.knights
    
    def get_number_of_vp(self):
        return self.victorypoints

