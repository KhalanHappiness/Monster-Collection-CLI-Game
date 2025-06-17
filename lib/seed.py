from models import MonsterSpecies
from models.base import Session

def seed_monsters():
    session = Session()

    # Prevent re-seeding if data already exists
    if session.query(MonsterSpecies).first():
        print("Monster species already seeded. Skipping.")
        return

    species_list = [
        {"name": "Flamewyrm", "type": "Fire", "base_hp": 45, "base_attack": 60, "base_defense": 40, "rarity": "Common", "abilities": "Fire Blast"},
        {"name": "Aquafin", "type": "Water", "base_hp": 50, "base_attack": 55, "base_defense": 45, "rarity": "Common", "abilities": "Water Pulse"},
        {"name": "Vinewhip", "type": "Grass", "base_hp": 40, "base_attack": 50, "base_defense": 50, "rarity": "Common", "abilities": "Vine Whip"},
        {"name": "Sparkbolt", "type": "Electric", "base_hp": 35, "base_attack": 65, "base_defense": 30, "rarity": "Rare", "abilities": "Thunderbolt"},
        {"name": "Rockgrinder", "type": "Rock", "base_hp": 60, "base_attack": 70, "base_defense": 60, "rarity": "Uncommon", "abilities": "Rock Slide"},
        {"name": "Thunderwing", "type": "Electric", "base_hp": 55, "base_attack": 75, "base_defense": 40, "rarity": "Rare", "abilities": "Thunder Punch"},
        {"name": "Megabolt", "type": "Electric", "base_hp": 70, "base_attack": 90, "base_defense": 60, "rarity": "Epic", "abilities": "Mega Thunder"},
        {"name": "Rockjaw", "type": "Rock", "base_hp": 50, "base_attack": 65, "base_defense": 55, "rarity": "Uncommon", "abilities": "Bite"},
        {"name": "Flareclaw", "type": "Fire", "base_hp": 45, "base_attack": 70, "base_defense": 35, "rarity": "Rare", "abilities": "Flame Claw"},
        {"name": "Aquashield", "type": "Water", "base_hp": 60, "base_attack": 50, "base_defense": 70, "rarity": "Uncommon", "abilities": "Water Shield"},
        {"name": "Leafdancer", "type": "Grass", "base_hp": 40, "base_attack": 55, "base_defense": 45, "rarity": "Common", "abilities": "Leaf Dance"},
        {"name": "Voltstrike", "type": "Electric", "base_hp": 50, "base_attack": 80, "base_defense": 40, "rarity": "Rare", "abilities": "Volt Strike"},
        {"name": "Stonehorn", "type": "Rock", "base_hp": 65, "base_attack": 75, "base_defense": 65, "rarity": "Epic", "abilities": "Horn Attack"},
        {"name": "Firetail", "type": "Fire", "base_hp": 40, "base_attack": 60, "base_defense": 40, "rarity": "Common", "abilities": "Tail Whip"},
        {"name": "Hydrofin", "type": "Water", "base_hp": 55, "base_attack": 60, "base_defense": 50, "rarity": "Common", "abilities": "Hydro Pump"},
    ]

    for data in species_list:
        monster = MonsterSpecies(**data)
        session.add(monster)

    session.commit()
    print("Monster species seeded successfully.")

if __name__ == "__main__":
    seed_monsters()
