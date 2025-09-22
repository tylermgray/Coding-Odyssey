## Save/load helpers

from __future__ import annotations
import json, os, pathlib, time

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SAVES_DIR = ROOT / "saves"
LOGS_DIR = ROOT / "logs"

def ensure_dirs() -> None:
    for p in (DATA_DIR, SAVES_DIR, LOGS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def load_json(path: pathlib.Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_json(path: pathlib.Path, data: dict) -> None:
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    tmp.replace(path)

def append_log(line: str) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    p = LOGS_DIR / f"session-{time.strftime('%Y%m%d')}.txt"
    with p.open("a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}] {line}\n")

