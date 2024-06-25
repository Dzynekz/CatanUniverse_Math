class Building:
    def __init__(self, cost) -> None:
        self.cost = cost

class Village(Building):
    COST = {'wood':1,'brick':1,'sheep':1, 'grain':1}

    def __init__(self) -> None:
        super().__init__(Village.COST)

class City(Building):
    COST = {'wood':1,'brick':1,'sheep':1, 'grain':3,'ore':3}

    def __init__(self) -> None:
        super().__init__(City.COST)

class Road(Building):
    COST = {'wood':1,'brick':1}

    def __init__(self) -> None:
        super().__init__(Road.COST)

# Przykład użycia:
#village = Village()
#print(village.cost)  # Wyświetlenie kosztu wioski

        