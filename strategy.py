import itertools
import pandas as pd

possible_combinations = {
    'Village': [0, 1, 2, 3, 4, 5],
    'City': [0, 1, 2, 3, 4],
    'MostRoads': [0, 1],
    'MostPorts': [0, 1],
    'MostKnights': [0, 1],
    'VictoryPointCards': [0, 1, 2, 3, 4, 5]
}

combinations = list(itertools.product(*possible_combinations.values()))

# Konwersja do DataFrame
combinations_all = pd.DataFrame(combinations, columns=possible_combinations.keys())

combinations_all['points'] = combinations_all.apply(lambda row: row['Village'] + row['City'] * 2 + row['MostRoads'] * 2 + row['MostPorts'] * 2 + row['MostKnights'] * 2 + row['VictoryPointCards'], axis=1)

win_conditions = combinations_all[combinations_all['points'].isin([15, 16])].reset_index()


def get_best_moves():
    """
    Zwraca kombinacje ruchów prowadzące do wygranej.
    """
    return 0