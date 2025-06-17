import random
from monster_collection_system.constants import RARITY_CATCH_RATES
from models.player_monster import PlayerMonster
from models.monster_species import MonsterSpecies
from models.base import Session

def calculate_catch_rate(species_rarity, player_level):
    base_rate = RARITY_CATCH_RATES.get(species_rarity, 0.1)
    bonus = min(player_level * 0.01, 0.1)  # max 10% bonus
    return min(base_rate + bonus, 1.0)

def catch_monster(player_id, species_id, player_level=1):
    session = Session()
    species = session.query(MonsterSpecies).get(species_id)

    if not species:
        print("Monster species not found.")
        return False

    catch_chance = calculate_catch_rate(species.rarity, player_level)

    if random.random() <= catch_chance:
        new_monster = PlayerMonster(
            player_id=player_id,
            species_id=species_id,
            level=1,
            experience=0,
            current_hp=species.base_hp
        )
        session.add(new_monster)
        session.commit()
        print(f"You caught {species.name}!")
        return True
    else:
        print(f"{species.name} escaped!")
        return False