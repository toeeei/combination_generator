from collections.abc import Iterable
import pandas as pd
import itertools

def is_subset(iter_a: Iterable, iter_b: Iterable) -> bool:
    for element_a in iter_a:
        if element_a in iter_b:
            pass
        else:
            return False
    return True

def keys_to_values(l: list, d: dict) -> list:
    return_values = []
    for element in l:
        return_values.append(d[element])
    return return_values

def generate_combinations(skill_cards: dict[int, int], requirement_cards: list[str], lower_limit: int, upper_limit: int) -> pd.DataFrame:
    df = pd.DataFrame()
    df["key_combinations"] = sorted(list(itertools.combinations(skill_cards, 5)))
    df["value_combinations"] = df["key_combinations"].apply(lambda x: keys_to_values(x, skill_cards))
    df["sum"] = df["value_combinations"].apply(sum)
    df = df[df["sum"].between(lower_limit, upper_limit)]
    df["requirement"] = df["key_combinations"].apply(lambda x: is_subset(requirement_cards, list(x)))

    return df.sort_values("sum")