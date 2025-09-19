## Combat and Round Logic

from __future__ import annotations
from typing import Dict, Any
from .io_utils import save_json, SAVES_DIR, append_log

def start_new_game(player_name: str, character_id: str, characters: Dict[str, Any], weapons: Dict[str, Any]) -> Dict[str, Any]:
    from .models import make_player
    state = {
        "player": make_player(player_name, character_id, characters, weapons),
        "progress": {"seed": None}
    }
    append_log(f"NEW GAME: {state['player']['name']} as {state['player']['character']}")
    save_json(SAVES_DIR / "save.json", state)
    return state

def load_game() -> Dict[str, Any] | None:
    from .io_utils import load_json, SAVES_DIR
    data = load_json(SAVES_DIR / "save.json")
    return data or None
