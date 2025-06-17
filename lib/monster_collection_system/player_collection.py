from models.player_monster import PlayerMonster
from models.base import Session

def get_player_collection(player_id):
    session = Session()
    monsters = session.query(PlayerMonster).filter_by(player_id=player_id).all()

    collection = []
    for m in monsters:
        collection.append({
            "name": m.species.name,
            "level": m.level,
            "type": m.species.type,
            "hp": m.current_hp,
            "rarity": m.species.rarity,
            "abilities": m.species.abilities
        })
    return collection