from __future__ import annotations
from typing import Dict, Any

def make_player(name: str, character_id: str, characters: Dict[str, Any], weapons: Dict[str, Any]) -> Dict[str, Any]:
    char = characters[character_id]
    starter_weapon = weapons["pistol"]["colt_1911"]
    return {
        "name": name,
        "character": char["name"],
        "favored_type": char["favored_weapon"],
        "weapon": starter_weapon,
        "base_hp": 150,
        "max hp": 250,
        "round": 1,
        "points": 0
    }