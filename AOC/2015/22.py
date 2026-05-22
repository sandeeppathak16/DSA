from heapq import heappush, heappop


def solve(hard_mode=False):
    boss_hp = 71
    boss_damage = 10

    pq = []

    initial_state = (
        0,
        50,
        500,
        boss_hp,
        0,
        0,
        0,
        True
    )

    heappush(pq, initial_state)

    visited = set()

    while pq:
        (
            mana_spent,
            player_hp,
            player_mana,
            boss_hp,
            shield,
            poison,
            recharge,
            player_turn
        ) = heappop(pq)

        state_key = (
            player_hp,
            player_mana,
            boss_hp,
            shield,
            poison,
            recharge,
            player_turn
        )

        if state_key in visited:
            continue

        visited.add(state_key)

        if hard_mode and player_turn:
            player_hp -= 1

            if player_hp <= 0:
                continue

        armor = 0

        if shield > 0:
            armor = 7
            shield -= 1

        if poison > 0:
            boss_hp -= 3
            poison -= 1

        if recharge > 0:
            player_mana += 101
            recharge -= 1

        if boss_hp <= 0:
            return mana_spent

        if player_turn:

            spells = []

            if player_mana >= 53:
                spells.append("magic_missile")

            if player_mana >= 73:
                spells.append("drain")

            if player_mana >= 113 and shield == 0:
                spells.append("shield")

            if player_mana >= 173 and poison == 0:
                spells.append("poison")

            if player_mana >= 229 and recharge == 0:
                spells.append("recharge")

            for spell in spells:

                n_hp = player_hp
                n_mana = player_mana
                n_boss = boss_hp

                n_shield = shield
                n_poison = poison
                n_recharge = recharge

                cost = 0

                if spell == "magic_missile":
                    cost = 53
                    n_boss -= 4

                elif spell == "drain":
                    cost = 73
                    n_boss -= 2
                    n_hp += 2

                elif spell == "shield":
                    cost = 113
                    n_shield = 6

                elif spell == "poison":
                    cost = 173
                    n_poison = 6

                elif spell == "recharge":
                    cost = 229
                    n_recharge = 5

                heappush(
                    pq,
                    (
                        mana_spent + cost,
                        n_hp,
                        n_mana - cost,
                        n_boss,
                        n_shield,
                        n_poison,
                        n_recharge,
                        False
                    )
                )

        else:
            damage = max(1, boss_damage - armor)

            player_hp -= damage

            if player_hp > 0:
                heappush(
                    pq,
                    (
                        mana_spent,
                        player_hp,
                        player_mana,
                        boss_hp,
                        shield,
                        poison,
                        recharge,
                        True
                    )
                )