from models.player_monster import PlayerMonster
from models.base import Session

def calculate_stats(base_hp, base_attack, base_defense, level):
    hp = base_hp + (level * 5)
    attack = base_attack + (level * 2)
    defense = base_defense + (level * 2)
    return {"hp": hp, "attack": attack, "defense": defense}

def level_up_monster(monster_id):
    session = Session()
    monster = session.query(PlayerMonster).get(monster_id)

    if not monster:
        print("Monster not found.")
        return {}

    monster.level += 1
    stats = calculate_stats(
        monster.species.base_hp,
        monster.species.base_attack,
        monster.species.base_defense,
        monster.level
    )
    monster.current_hp = stats["hp"]
    session.commit()

    print(f"{monster.species.name} leveled up to {monster.level}!")
    return stats
