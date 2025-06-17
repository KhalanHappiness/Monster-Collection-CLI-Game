TYPE_EFFECTIVENESS = {
    "Fire": {"strong_against": ["Grass", "Air"], "weak_against": ["Water", "Rock"]},
    "Water": {"strong_against": ["Fire", "Rock"], "weak_against": ["Electric", "Grass"]},
    "Grass": {"strong_against": ["Water", "Rock"], "weak_against": ["Fire", "Air"]},
    "Electric": {"strong_against": ["Water", "Air"], "weak_against": ["Rock", "Grass"]},
    "Rock": {"strong_against": ["Electric", "Fire"], "weak_against": ["Water", "Grass"]},
    "Air": {"strong_against": ["Grass"], "weak_against": ["Electric", "Fire"]},
    "Earth": {"strong_against": ["Electric", "Rock"], "weak_against": ["Water", "Grass"]},
}

def get_type_effectiveness(attacker_type: str, defender_type: str) -> float:
    if attacker_type == defender_type:
        return 1.0
    if defender_type in TYPE_EFFECTIVENESS.get(attacker_type, {}).get("strong_against", []):
        return 2.0
    if defender_type in TYPE_EFFECTIVENESS.get(attacker_type, {}).get("weak_against", []):
        return 0.5
    return 1.0