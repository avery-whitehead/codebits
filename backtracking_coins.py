from typing import Optional


def solver(
    coins: list[int], total: int, chosen_coins: list[int]
) -> Optional[list[list[int]]]:
    if total == 0:
        return [chosen_coins]
    if total < 0 or not coins:
        return []

    pick = coins[0]
    use = solver(coins, total - pick, chosen_coins + [pick])
    notuse = solver(coins[1:], total, chosen_coins)

    if use is not None and notuse is not None:
        return use + notuse
    if use is not None:
        return use
    if notuse is not None:
        return notuse
    return []


print(solver([1, 2, 5, 10, 20, 50, 100, 200], 200, []))
