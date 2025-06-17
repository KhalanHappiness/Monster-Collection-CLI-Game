import random
from models import Session, Player, PlayerMonster, MonsterSpecies

RARITY_MULTIPLIER = {
    "Common": 0.8,
    "Uncommon": 0.5,
    "Rare": 0.25,
    "Epic": 0.1
}

def calculate_catch_rate(rarity, player_level):
    base_rate = RARITY_MULTIPLIER.get(rarity, 0.2)
    return min(0.95, base_rate + (player_level * 0.01))

def catch_monster(player_id, species_id):
    session = Session()
    player = session.get(Player, player_id)
    species = session.get(MonsterSpecies, species_id)

    rate = calculate_catch_rate(species.rarity, player.level)
    if random.random() < rate:
        monster = PlayerMonster(
            player_id=player.id,
            species_id=species.id,
            level=1,
            current_hp=species.base_hp
        )
        session.add(monster)
        session.commit()
        return True
    return False

def level_up_monster(monster_id):
    session = Session()
    monster = session.get(PlayerMonster, monster_id)
    monster.level += 1
    monster.current_hp += 5  # or a formula
    monster.experience = 0
    session.commit()
    return {"level": monster.level, "hp": monster.current_hp}

def get_player_collection(player_id):
    session = Session()
    return session.query(PlayerMonster).filter_by(player_id=player_id).all()