# CODe Zombies
_A Python Call of Duty Zombies text game project for Coding Odyssey 1._



-----------------
## FEATURES
-----------------

- Select main character:    **Dempsey**         **Nikolai**                     **Richtofen**               **Takeo**
- Fight enemies:            **Zombies**         **Nova-6 Crawlers**             **Hell-Hounds**             **Parasites**           **Denizens**            **Vermin**  **Keepers**
- Future Fight bosses:      **Margwa**          **Mangler** **Abomination**     **Amalgam**                 **George A. Romero**    **Cosmic Silverback**   **Panzer**  **Brutus**  **Avogadro**
- Future Wants/Activities:       **Mystery Box**     **Boarding Window System**      **Pack-a-Punch System**     **Point System**        **Round Increase System**             **Normal enemy health increases each round**        **Random chance for Power-Ups (Double Points, Nuke, Max Ammo, Max Health, etc.)** 
- Far Future:                   **Ammo Mods after first P-a-P | Napalm Burst(Fire), Dead Wire(Shock), Cryo Freeze(Freeze), Brain Rot(Poison), Shatter Blast(Explosive), Shadow Rift(Void)**


### GOALS

- Overall
- Describe Project (Single Sentence)
- Time Left

-----------------
## File Structure
-----------------

dice-zombies/
├── data/
│   ├── enemies.json        # Enemy stats & traits
│   ├── weapons.json        # Weapon definitions
│   ├── characters.json     # Playable characters
├── saves/
│   └── save.json           # Autosave data
├── logs/                   # Session logs (optional)
├── dice_115/
│   ├── __init__.py
│   ├── main.py             # Entry point
│   ├── ui.py               # Input/output prompts
│   ├── models.py           # Player & enemy data structures
│   ├── logic.py            # Combat, rounds, box, boarding
│   ├── io_utils.py         # Save/load, logs
│   ├── rng.py              # Dice rolls, random helpers
├── DESIGN.md               # This document
├── README.md               # Instruction/info document


------------------
## HOW TO RUN
------------------
```bash
python -m dice_115.main
