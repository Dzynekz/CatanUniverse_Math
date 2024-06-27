import itertools
import math
import pandas as pd
from deck import Deck

def number_of_attempts_needed(cards_of_type, all_cards):
    x = cards_of_type/ all_cards
    y = 1 / x
    return math.ceil(y)

def knights_probability(deck: Deck) -> int:
    cards = deck.get_number_of_cards()
    knights = deck.get_number_of_knights()
    answer = number_of_attempts_needed(knights,cards)
    print('probablity of knight: ' + str(answer))
    return answer

def vp_probability(deck: Deck) -> int:
    cards = deck.get_number_of_cards()
    vp = deck.get_number_of_vp()
    answer = number_of_attempts_needed(vp,cards)
    print('probablity of vp: ' + str(answer))
    return answer

def combination_of_possible_wins():
    possible_combinations = {
        'village': [0, 1, 2, 3, 4, 5],
        'city': [0, 1, 2, 3, 4],
        'mostRoads': [0, 1],
        'mostPorts': [0, 1],
        'mostKnights': [0, 1],
        'victoryPointCards': [0, 1, 2, 3, 4, 5]
    }

    combinations = list(itertools.product(*possible_combinations.values()))

    # Konwersja do DataFrame
    combinations_all = pd.DataFrame(combinations, columns=possible_combinations.keys())

    combinations_all['points'] = combinations_all.apply(lambda row: row['village'] + row['city'] * 2 + row['mostRoads'] * 2 + row['mostPorts'] * 2 + row['mostKnights'] * 2 + row['victoryPointCards'], axis=1)

    possible_wins = combinations_all[combinations_all['points'].isin([15, 16])].reset_index()

    return possible_wins

def add_resource_cost_of_wins(df, deck: Deck):
    '''A lot of problems here:
        - no RoadBuilding card implemented
        - no monopol, yearofplenty cards
        - dont know how to calculate roads needed per city - for now its 8 roads always **
        - dont know how to do ports I assume that mostPorts means you have to add 4 another roads
        - substract -4, -2 or 0 because of first 2 villages and roads'''
    df['wood'] = df['village'] + df['city'] + max(df['mostRoads'] * 12, 8) + df['mostPorts'] * 4 - 4
    df['brick'] = df['village'] + df['city'] + max(df['mostRoads'] * 12, 8) + df['mostPorts'] * 4 - 4
    df['sheep'] = df['village'] + df['city'] + df['mostKnights'] * knights_probability(deck) + df['victoryPointCards'] * vp_probability(deck) -2
    df['grain'] = df['village'] + df['city'] * 3 + df['mostKnights'] * knights_probability(deck) +  df['victoryPointCards'] * vp_probability(deck) -2
    df['ore'] = df['city'] * 3 + df['mostKnights'] * knights_probability(deck) +  df['victoryPointCards'] * vp_probability(deck)
    df['used_resources'] = df['wood'] + df['brick'] + df['sheep'] + df['grain'] + df['ore']
    return df

def compare_resources(win, win2) -> bool:
    resources = ['wood','brick','sheep','grain','ore']
    return all(win[res] < win2[res] for res in resources)

def removing_worse_wins(df):
    '''If some win needs more of every resource than the other win, that means he is worse in everything'''
    drop = set()
    for i, win in df.iterrows():
        for j in range(i + 1, len(df)):
            win2 = df.iloc[j]
            if compare_resources(win, win2):
                drop.add(j)
    df = df.drop(drop)
    return df

def resources_drop_chance(board: dict) -> dict:
    probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    resource_probability = {}
    for resource, numbers in board.items():
        resource_probability[resource] = sum(probabilities[number] for number in numbers)
    return resource_probability

def calculate_rounds_needed(df, resource_probabilities):
    pass
