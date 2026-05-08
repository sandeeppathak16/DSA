from itertools import combinations


def fight(
    player_hp, 
    player_damage, 
    player_armor, 
    boss_hp, 
    boss_damage, 
    boss_armor
):

    player_attack = max(1, player_damage - boss_armor)
    boss_attack = max(1, boss_damage - player_armor)

    while player_hp > 0 and boss_hp > 0:

        boss_hp -= player_attack

        if boss_hp <= 0:
            return True

        player_hp -= boss_attack

    return False


def solve():
    weapons = [
        ['Dagger', 8, 4, 0],
        ['Shortsword', 10, 5, 0],
        ['Warhammer', 25, 6, 0],
        ['Longsword', 40, 7, 0],
        ['Greataxe', 74, 8, 0],
    ]

    armors = [
        ['', 0, 0, 0],
        ['Leather', 13, 0, 1],
        ['Chainmail', 31, 0, 2],
        ['Splintmail', 53, 0, 3],
        ['Bandedmail', 75, 0, 4],
        ['Platemail', 102, 0, 5],
    ]

    rings = [
        ['Damage +1', 25, 1, 0],
        ['Damage +2', 50, 2, 0],
        ['Damage +3', 100, 3, 0],
        ['Defense +1', 20, 0, 1],
        ['Defense +2', 40, 0, 2],
        ['Defense +3', 80, 0, 3],
    ]
    
    ring_combinations = [[]]

    for ring in rings:
        ring_combinations.append([ring])

    for combo in combinations(rings, 2):
        ring_combinations.append(list(combo))

    min_win_cost = float('inf')

    max_lose_cost = float('-inf')

    for weapon in weapons:
        for armor in armors:
            for ring_combo in ring_combinations:

                cost = weapon[1] + armor[1]
                damage = weapon[2] + armor[2]
                total_armor = weapon[3] + armor[3]

                for ring in ring_combo:
                    cost += ring[1]
                    damage += ring[2]
                    total_armor += ring[3]

                player_wins = fight(
                    player_hp=100,
                    player_damage=damage,
                    player_armor=total_armor,
                    boss_hp=103,
                    boss_damage=9,
                    boss_armor=2
                )

                if player_wins:
                    min_win_cost = min(min_win_cost, cost)
                else:
                    max_lose_cost = max(max_lose_cost, cost)

    return min_win_cost, max_lose_cost