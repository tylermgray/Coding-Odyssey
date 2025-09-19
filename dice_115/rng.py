## Dice Rolls & RNG Seeding

from __future__ import annotations
import random

def seed_rng(seed: int | None = None) -> None:
    random.seed(seed)

def roll_d6(bonus: int = 0) -> int:
    return min(6, random.randint(1, 6) + bonus)
